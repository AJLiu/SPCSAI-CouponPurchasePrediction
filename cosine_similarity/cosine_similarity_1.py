import numpy as np
import pandas as pd
import patsy
# from scipy.spatial import distance

__author__ = 'MES'

coupon_purchase_log = pd.read_csv("../data/coupon_detail_train.csv")
coupon_list_train = pd.read_csv("../data/coupon_list_train.csv")
coupon_list_test = pd.read_csv("../data/coupon_list_test.csv")
user_list = pd.read_csv("../data/user_list.csv")

train = coupon_purchase_log.merge(coupon_list_train)
train = train[["COUPON_ID_hash","USER_ID_hash",
               "GENRE_NAME","PRICE_RATE","CATALOG_PRICE","DISCOUNT_PRICE",
               "USABLE_DATE_MON","USABLE_DATE_TUE","USABLE_DATE_WED","USABLE_DATE_THU",
               "USABLE_DATE_FRI","USABLE_DATE_SAT","USABLE_DATE_SUN","USABLE_DATE_HOLIDAY",
               "USABLE_DATE_BEFORE_HOLIDAY","ken_name","small_area_name"]]

coupon_list_test['USER_ID_hash'] = "dummyuser"
coupon_characteristics = coupon_list_test[["COUPON_ID_hash","USER_ID_hash",
               "GENRE_NAME","PRICE_RATE","CATALOG_PRICE","DISCOUNT_PRICE",
               "USABLE_DATE_MON","USABLE_DATE_TUE","USABLE_DATE_WED","USABLE_DATE_THU",
               "USABLE_DATE_FRI","USABLE_DATE_SAT","USABLE_DATE_SUN","USABLE_DATE_HOLIDAY",
               "USABLE_DATE_BEFORE_HOLIDAY","ken_name","small_area_name"]]

train = train.append(coupon_characteristics)

# replace all NA values with 1
train = train.fillna(1)

# bin the prices into categories
train['PRICE_RATE'] = pd.cut(train['PRICE_RATE'], [-0.01, 20, 40, 60, 80, 100],
                   labels=["cheap", "moderate", "expensive", "high", "luxury"])
train['CATALOG_PRICE'] = pd.cut(train['CATALOG_PRICE'], [-0.01, 0, 1000, 10000, 50000, 100000, np.inf],
                   labels=["free", "cheap", "moderate", "expensive", "high", "luxury"])
train['DISCOUNT_PRICE'] = pd.cut(train['DISCOUNT_PRICE'], [-0.01, 0, 1000, 10000, 50000, 100000, np.inf],
                   labels=["free", "cheap", "moderate", "expensive", "high", "luxury"])


# Turn features into 1's and 0's
train2 = train.drop(['COUPON_ID_hash', 'USER_ID_hash'], axis=1)
all_columns = "+".join(train2.columns)
train2 = patsy.dmatrix(all_columns + " - 1", train2, return_type='dataframe')

# Combine it with the first two columns (hashes)
train1 = train[['COUPON_ID_hash', 'USER_ID_hash']]
train = pd.concat([train1, train2], axis=1)

# Split it into test and train data frames
test_coupons = train.loc[train['USER_ID_hash'] == 'dummyuser']
test_coupons = test_coupons.drop(['USER_ID_hash'], axis=1)
train = train.loc[train['USER_ID_hash'] != 'dummyuser']

# take mean of each column for each user
user_preferences = train.groupby('USER_ID_hash', as_index=False).aggregate(np.mean)

# convert them into numpy arrays
upmat = user_preferences.as_matrix(user_preferences.columns.difference(['USER_ID_hash']))
tcmat = test_coupons.as_matrix(test_coupons.columns.difference(['COUPON_ID_hash']))

# calculate "cosine similarity"

# Method 1
similarity = np.dot(upmat, tcmat.T)

# Method 1 expansion (doesn't work)
#==============================================================================
# square_mag = np.diag(similarity)
# inv_square_mag = 1 / square_mag
# inv_square_mag[np.isinf(inv_square_mag)] = 0
# inv_mag = np.sqrt(inv_square_mag)
# 
# cosine = similarity * inv_mag
# cosine = cosine * inv_mag
# similarity = cosine
#==============================================================================

# Method 2
#==============================================================================
# tcmat_t = tcmat.T
# similarity = np.empty([len(user_preferences), len(test_coupons)])
# for row in range(0, len(upmat)):
#     for col in range(0, len(tcmat_t)):
#         similarity[row][col] = distance.cosine(upmat[row], tcmat[col])
#==============================================================================

# store top 10 scores for each user
results = pd.DataFrame({"USER_ID_hash": ['']*len(similarity), "PURCHASED_COUPONS": ['']*len(similarity)})
for i in range(0, len(similarity)): # iterate by row
    user_hash = user_preferences.at[i, 'USER_ID_hash']
    coupons = ""
    score_indices = np.argsort(similarity[i,])
    count = 0
    for index in reversed(score_indices):
        if count >= 10:
            break
        coupons = coupons + test_coupons.at[index, 'COUPON_ID_hash']
        if count < 9:
            coupons = coupons + " "
        count = count + 1
    results.set_value(i, 'USER_ID_hash', user_hash)
    results.set_value(i, 'PURCHASED_COUPONS', coupons)
    
# merge with users master list and save to csv
user_list = user_list[['USER_ID_hash']]
results = user_list.merge(results, how='outer')
results.to_csv("../data/output/cosine_similarity.csv", na_rep="NA", index=False)

print("done")
