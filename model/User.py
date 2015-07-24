__author__ = 'Krager'
import datetime


class User:
    """Class used to hold the info found in user; data is gotten from userlist.csv"""
    def __init__(self, reg_date=datetime.datetime.today(), sex_id="",
                 age=0, withdraw_date=datetime.datetime.today(), pref_name="", user_id=""
                 ):

        self.reg_date = reg_date
        self.sex_id = sex_id
        self.age = age
        self.withdraw_date = withdraw_date
        self.pref_name = pref_name
        self.user_id = user_id

    def __str__(self):
        return "[%s, %s, %d, %s, %s, %s]" % (
            str(self.reg_date),
            self.sex_id,
            self.age,
            str(self.withdraw_date),
            str(self.pref_name).encode('ascii', 'ignore'),
            self.user_id
        )
