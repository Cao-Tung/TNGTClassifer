# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from sklearn.naive_bayes import MultinomialNB
import numpy as np 
from pyvi.pyvi import ViTokenizer, ViPosTagger
import sys

# train raw data
dt1 = u"Hà Nội Phở Cháo Lòng Hà Nội Cháo Trai"
dt2 = u"Hà Nội Bún Chả Phở Ô Mai Lẩu Ếch"
dt3 = u"Phở Bánh Giò Ô Mai"
dt4 = u"Sài Gòn Hủ Tiếu Bánh Bò Phở Bún Nem"
dt5 = u"Hà Nội Hà Nội Bún Chả Hủ Tiếu Nem Gián Cơm Gà Phở"

#VNTokenizer
dt1 = ViTokenizer.tokenize(dt1)
dt2 = ViTokenizer.tokenize(dt2)
dt3 = ViTokenizer.tokenize(dt3)
dt4 = ViTokenizer.tokenize(dt4)
dt5 = ViTokenizer.tokenize(dt5)

print(isinstance(dt1, (str, unicode)))

# Dictionary
arr1 = dt1.split()
arr2 = dt2.split()
arr3 = dt3.split()
arr4 = dt4.split()
arr5 = dt5.split()
arr = arr1 + arr2 + arr3 + arr4

dt = list(set(arr))

# Function make Matrix in dict
def makeMatrix(arr,dct):
    lst = []
    for x in dct:
        if x in arr:
            lst.append(1)
        else:
            lst.append(0)
    return lst

d1,d2,d3,d4,d5 = [],[],[],[],[];

print(repr(arr5).decode("unicode-escape"))
print(repr(dt).decode("unicode-escape"))

#make Matrix 1,2,..
d1 = makeMatrix(arr1,dt)
d2 = makeMatrix(arr2,dt)
d3 = makeMatrix(arr3,dt)
d4 = makeMatrix(arr4,dt)
d5 = makeMatrix(arr5,dt)

train_data = np.array([d1, d2, d3, d4])
label = np.array(['B', 'B', 'B', 'N'])

#data predict
d5 = np.array([d5])

## call MultinomialNB
clf = MultinomialNB()
# training 
clf.fit(train_data, label)

# test
print('Predicting class of d5:', str(clf.predict(d5)[0]), clf.predict_proba(d5))

# print(dt)
# print(repr(dt).decode("unicode-escape"))
# msg = repr([x.encode(sys.stdout.encoding) for x in dt]).decode('string-escape')
# print(msg)
