# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
with open('csv.csv','r') as csvinput:
    with open('tcsv.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            writer.writerow(row+['Berry'])