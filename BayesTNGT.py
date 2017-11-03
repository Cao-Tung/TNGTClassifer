# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv as csv
from sklearn.naive_bayes import MultinomialNB
import numpy as np 
from pyvi.pyvi import ViTokenizer, ViPosTagger
import sys
import pickle

def read(filename):
        f = open(filename)
        data = pickle.load(f)
        f.close()
        return data

def makeMatrix(arr,dct):
    lst = []
    for x in dct:
        if x in arr:
            lst.append(1)
        else:
            lst.append(0)
    return lst
diction = read("diction.file")
lb = read("labels.file")

trd = read("trains.file")
count = 0
lpre = []
ldata = []
with open('data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        count = count + 1
        pre = unicode(row[0], "utf-8")
        ldata.append(row)
        lpre.append(pre)
# du doan
count = 0
for i in range(len(ldata)):

	lpre[i] = lpre[i].replace("," , "").replace("." , "")
	lpre[i] = ViTokenizer.tokenize(lpre[i])
	lpre[i] = lpre[i].lower()
	arrpre = lpre[i].split()
	apre = makeMatrix(arrpre, diction)
	dpre = np.array([apre])

## call MultinomialNB
	clf = MultinomialNB()
# training 
	clf.fit(trd, lb)

# test
	# print(repr(pre).decode("unicode-escape"))
	print('Predicting class of dpre:', str(clf.predict(dpre)[0]), clf.predict_proba(dpre))
	if str(clf.predict(dpre)[0]) == '1':
		count = count + 1

print(count)
	# ldata[i] = ldata[i] + [unicode(str(clf.predict(dpre)[0]), "utf-8")]
# with open('result.csv', 'w') as csvoutput:
#     writer = csv.writer(csvoutput)
#     for j in range(len(ldata)):
#         writer.writerow(ldata[j])
# print(repr(lpre[0]).decode("unicode-escape"))