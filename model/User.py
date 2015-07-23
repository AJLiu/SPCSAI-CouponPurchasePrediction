__author__ = 'Krager'
import datetime


class User:
    """Class used to hold the info found in user; data is gotten from userlist.csv"""
    def __init__(self, regDate = datetime(), sexid = '', age = 0, withdrawDate = datetime(), prefName = "", userid = ""):
        self.regDate = regDate
        self.sexid = sexid
        self.age = age
        self.withdrawDate = withdrawDate
        self.prefName = prefName
        self.userid = userid
