__author__ = 'Krager'
import datetime
class Coupon:
    """Class used to store data about a coupon"""
    def __init__(self):
        self.capsulteText = "" #JAP
        self.genreName = ""    #JAP
        self.priorityRate = 0
        self.catalogPrice = 0
        self.discoutPrice = 0

        self.startAvailableDate = datetime() #DISPFROM DISP = date the coupons are givin out
        self.endAvailableDate = datetime() #DISPEND
        self.availablePeriod = 0 #DISPPERIOD

        self.startValidityDate = datetime() #VALIDFROM VALID = date the coupon is usable in a store
        self.endValidityDate = datetime() #VALIDEND
        self.validityPeriod = 0 #VALIDEND

        self.usableDaysInWeek = [False, False, False, False, False, False, False] #Each day of the week starting on Monday
        self.usableOnHoliday = False #Whether or not coupon can be used on a holiday
        self.usableBeforeHoliday = False #Whether or not coupon can be used before a holiday

        self.largeAreaName = "" #JAP Large Area the shop is in
        self.kenName = ""       #JAP District name the shop is in??? I'm not really sure
        self.smallAreaName = "" #JAP Small area the shop is in

        self.couponid = ""
        self.couponVisits = [CouponVisit()] # Coupon visists in an array


