# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv as csv

# csv_file_object = csv.reader(open('data.csv', 'r'))
# header = csv_file_object.next()
# data= "".encode("utf-8")
count = 0
arr = []
dt = {}
# for row in csv_file_object:
#

with open('data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        count = count + 1
        if (count > 100) and (count < 600):
            utf = unicode(row[0], "utf-8")
            arr.append(utf)
            if count == 110:
                dt["TNGT"] = arr
        elif count <= 100 :
            count = count
        else :
            break



# with codecs.open('test.csv', 'wb') as csvfile:
#     for x_result in arr:
#         csvfile.write(x_result)
#         csvfile.write("\n")

with open('dt500.csv','w') as fout:
    writer=csv.writer(fout)
    for row in zip(*dt.values()):
        row = [s.encode('utf-8') for s in row]
        writer.writerows([row])
        writer.writerows("\n")
