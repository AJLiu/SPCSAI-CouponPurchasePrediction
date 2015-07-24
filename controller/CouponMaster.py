import csv
import time
from model.Coupon import Coupon

__author__ = 'Krager'


class CouponMaster:

    coupons = []

    @staticmethod
    def load_from_csv():
        coupon_list_file = open('../data/coupon_list_train.csv', encoding="utf8")
        coupon_list_raw = list(csv.reader(coupon_list_file))[1:]  # Remove the first header row
        CouponMaster.coupons = [None] * len(coupon_list_raw)

        for i in range(0, len(CouponMaster.coupons)):
            row = coupon_list_raw[i]
            # print(str(row).encode('ascii', 'ignore'))

            capsule_text = row[0]
            genre_name = row[1]
            priority_rate = int(row[2])
            catalog_price = int(row[3])
            discount_price = int(row[4])
            start_available_date = time.strptime(row[5], "%Y-%m-%d %H:%M:%S")
            end_available_date = time.strptime(row[6], "%Y-%m-%d %H:%M:%S")
            available_period = int(row[7])
            start_validity_date = None
            if row[8] != "NA":
                start_validity_date = time.strptime(row[8], "%Y-%m-%d")
            end_validity_date = None
            if row[9] != "NA":
                end_validity_date = time.strptime(row[9], "%Y-%m-%d")
            validity_period = 0
            if row[10] != "NA":
                validity_period = int(row[10])
            usable_days_in_week = [
                row[11] == "NA" or int(row[11]) == 1,
                row[12] == "NA" or int(row[12]) == 1,
                row[13] == "NA" or int(row[13]) == 1,
                row[14] == "NA" or int(row[14]) == 1,
                row[15] == "NA" or int(row[15]) == 1,
                row[16] == "NA" or int(row[16]) == 1,
                row[17] == "NA" or int(row[17]) == 1
            ]
            usable_on_holiday = row[18] == "NA" or int(row[18]) == 1
            usable_before_holiday = row[19] == "NA" or int(row[19]) == 1
            large_area_name = row[20]
            ken_name = row[21]
            small_area_name = row[22]
            coupon_id = row[23]
            coupon_areas = None

            CouponMaster.coupons[i] = Coupon(
                capsule_text, genre_name, priority_rate, catalog_price, discount_price,
                start_available_date, end_available_date, available_period,
                start_validity_date, end_validity_date, validity_period,
                usable_days_in_week, usable_on_holiday, usable_before_holiday,
                large_area_name, ken_name, small_area_name, coupon_id, coupon_areas
            )

        print("Read", len(CouponMaster.coupons), "coupons into list")

        return

    # @staticmethod
    # def addCouponListToCouponWithID(id):
        # for current in couponList:

