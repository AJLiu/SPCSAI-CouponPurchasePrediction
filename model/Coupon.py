from datetime import datetime

__author__ = 'Krager'


class Coupon:
    """Class used to store data about a coupon"""

    def __init__(self, capsule_text="", genre_name="", priority_rate=0, catalog_price=0, discount_price=0,
                 start_available_date=datetime.today(), end_available_date=datetime.today(), available_period=0,
                 start_validity_date=datetime.today(), end_validity_date=datetime.today(), validity_period=0,
                 usable_days_in_week=[False] * 7, usable_on_holiday=False, usable_before_holiday=False,
                 large_area_name="", ken_name="", small_area_name="", coupon_id="", coupon_areas=None
                 ):
        self.capsule_text = capsule_text  # JAP
        self.genre_name = genre_name  # JAP
        self.priority_rate = priority_rate
        self.catalog_price = catalog_price
        self.discount_price = discount_price

        self.start_available_date = start_available_date  # DISPFROM DISP = date the coupons are given out
        self.end_available_date = end_available_date  # DISPEND
        self.available_period = available_period  # DISPPERIOD

        self.start_validity_date = start_validity_date  # VALIDFROM VALID = date the coupon is usable in a store
        self.end_validity_date = end_validity_date  # VALIDEND
        self.validity_period = validity_period  # VALIDEND

        self.usable_days_in_week = usable_days_in_week  # Each day of the week starting on Monday
        self.usable_on_holiday = usable_on_holiday  # Whether or not coupon can be used on a holiday
        self.usable_before_holiday = usable_before_holiday  # Whether or not coupon can be used before a holiday

        self.large_area_name = large_area_name  # JAP Large Area the shop is in
        self.ken_name = ken_name  # JAP District name the shop is in??? I'm not really sure
        self.small_area_name = small_area_name  # JAP Small area the shop is in

        self.coupon_id = coupon_id
        self.coupon_areas = coupon_areas  # Coupon visits in an array
        return

    def __str__(self):
        return "[%s, %s, %s, %s, %s, " \
               "%s, %s, %s, " \
               "%s, %s, %s, " \
               "%s, %s, %s, " \
               "%s, %s, %s, %s, %s]" % (
                   str(self.capsule_text).encode('ascii', 'ignore'),
                   str(self.genre_name).encode('ascii', 'ignore'),
                   self.priority_rate, self.catalog_price, self.discount_price,
                   str(self.start_available_date), str(self.end_available_date), str(self.available_period),
                   str(self.start_validity_date), str(self.end_validity_date), self.validity_period,
                   str(self.usable_days_in_week), self.usable_on_holiday, self.usable_before_holiday,
                   str(self.large_area_name).encode('ascii', 'ignore'),
                   str(self.ken_name).encode('ascii', 'ignore'),
                   str(self.small_area_name).encode('ascii', 'ignore'),
                   self.coupon_id, str(self.coupon_areas)
               )
