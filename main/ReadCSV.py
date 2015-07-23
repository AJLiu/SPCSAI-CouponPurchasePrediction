__author__ = 'MES'


#class ReadCSV:

import csv
import User

print("Hello world")

user_list_file = open('../data/user_list.csv', encoding="utf8")
#user_list_file = open('test.csv', encoding="utf8")
user_list_raw = list(csv.reader(user_list_file))

user_list = [0 * len(user_list_raw)]

count = 0
for row in user_list_raw:
    if count == 10:
        break
    # do things
    user_list[count] = User()
    count += 1


# How to print unicode properly
#print(str(row).encode('ascii', 'ignore'))
