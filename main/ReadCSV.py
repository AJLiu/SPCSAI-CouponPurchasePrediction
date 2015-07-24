import csv
import time
from controller.CouponMaster import CouponMaster
from controller.UserMaster import UserMaster
from model.User import User

__author__ = "Ivon Liu"

# How to print unicode properly
# print(str(row).encode('ascii', 'ignore'))

print("Hello world")

# Read user_list
UserMaster.load_from_csv()
# print("\nPrinting from User object now")
# for row in range(0, len(UserMaster.users)):
    # print(str(UserMaster.users[row]))

# Read coupon_list_train
CouponMaster.load_from_csv()
# print("\n Printing from Coupon object now")
# for row in range(0, len(CouponMaster.coupons)):
    # print(str(CouponMaster.coupons[row]))

