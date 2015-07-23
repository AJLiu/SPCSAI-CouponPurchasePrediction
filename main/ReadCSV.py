__author__ = 'MES'


#class ReadCSV:

import csv

print("Hello world")

with open('../data/user_list.csv', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0;
    for row in spamreader:
        count += 1
        if count == 10:
            break
        print(str(row).encode('ascii', 'ignore'))

