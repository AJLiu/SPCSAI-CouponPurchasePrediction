# -*- coding: utf-8 -*-
import random
import pandas as pd
import numpy as np

coupon_list = pd.read_csv('../csv/Krager_Set/Mutilated Orginal Sheets/coupon_list_train.csv', encoding="utf8")
krager_list = pd.DataFrame(columns=coupon_list.columns)
#coupon_list = pd.DataFrame(columns=coupon_list.columns)

usedNum = random.sample(range(0, len(coupon_list)), 310)
for i in range(0, 310):
    rowNum = usedNum[i] 
    krager_list.loc[i] = coupon_list.loc[rowNum]
    #coupon_list = coupon_list.drop(rowNum)
    
usedNum.sort()
for i in range(0, len(krager_list)):
    coupon_list = coupon_list[coupon_list.COUPON_ID_hash != krager_list.at[i, 'COUPON_ID_hash']]
    
coupon_detail = pd.read_csv('../csv/Krager_Set/Mutilated Orginal Sheets/coupon_detail_train.csv', encoding="utf8")
krager_detail = pd.DataFrame(columns=coupon_detail.columns)
for i in range(0, 310):
    row = coupon_detail[coupon_detail.COUPON_ID_hash == krager_list.at[i , 'COUPON_ID_hash' ]]
    krager_detail = krager_detail.append(row)
    coupon_detail = coupon_detail[coupon_detail.COUPON_ID_hash != krager_list.at[i, 'COUPON_ID_hash']]
    
krager_list.to_csv("../csv/Krager_Set/Mutilated Orginal Sheets/coupon_list_krager.csv", na_rep="NA", index=False)
krager_detail.to_csv("../csv/Krager_Set/Mutilated Orginal Sheets/coupon_detail_krager.csv", na_rep="NA", index=False)
coupon_list.to_csv("../csv/Krager_Set/Mutilated Orginal Sheets/coupon_list_modified_training.csv", na_rep="NA", index=False)
coupon_detail.to_csv("../csv/Krager_Set/Mutilated Orginal Sheets/coupon_detail_modified_training.csv", na_rep="NA", index=False)