import csv
import time
from model.User import User

__author__ = 'Krager'


class UserMaster:

    users = []

    @staticmethod
    def load_from_csv():
        user_list_file = open('../data/user_list.csv', encoding="utf8")
        user_list_raw = list(csv.reader(user_list_file))[1:]  # Remove the first header row
        UserMaster.users = [None] * len(user_list_raw)
        for i in range(0, len(UserMaster.users)):
            row = user_list_raw[i]
            #print(str(row).encode('ascii', 'ignore'))

            reg_date = time.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            sex_id = row[1]
            age = int(row[2])
            withdraw_time = None
            if row[3] != "NA":
                withdraw_time = time.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            pref_name = row[4]
            user_id = row[5]

            UserMaster.users[i] = User(reg_date, sex_id, age, withdraw_time, pref_name, user_id)

        print("Read", len(UserMaster.users), "users into list")

        return
