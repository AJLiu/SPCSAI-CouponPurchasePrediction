__author__ = 'Krager'
import datetime


class User:
    """Class used to hold the info found in user; data is gotten from userlist.csv"""
    def __init__(self, regDate=datetime.datetime.today(), sexid='', age=0, withdrawDate=datetime.datetime.today(), prefName="", userid=""):
        self.regDate = regDate
        self.sexid = sexid
        self.age = age
        self.withdrawDate = withdrawDate
        self.prefName = prefName
        self.userid = userid

    def __str__(self):
        return "[%s, %s, %s, %s, %s, %s]" % (str(self.regDate), self.sexid, self.age, str(self.withdrawDate), str(self.prefName).encode('ascii', 'ignore'), self.userid)
