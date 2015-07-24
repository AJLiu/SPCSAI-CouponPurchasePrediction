import csv
import time
from model.User import User

__author__ = "Ivon Liu"

print("Hello world")

user_list_file = open('../data/user_list.csv', encoding="utf8")
user_list_raw = list(csv.reader(user_list_file))[1:]    # Remove the first header row

user_list = [None] * len(user_list_raw)

count = 0
for row in user_list_raw:
    #if count == 10:
        #break
    # do things
    print(str(row).encode('ascii', 'ignore'))
    reg_date = time.strptime(row[0], "%Y-%m-%d %H:%M:%S")

    withdraw_time = None
    if row[3] != "NA":
        withdraw_time = time.strptime(row[3], "%Y-%m-%d %H:%M:%S")

    user_list[count] = User(reg_date, row[1], row[2], withdraw_time, row[4], row[5])
    count += 1

print("\nPrinting from User object now")
for row in range(0, len(user_list)):
    print(str(user_list[row]))



# How to print unicode properly
#print(str(row).encode('ascii', 'ignore'))
