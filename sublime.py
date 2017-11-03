# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pickle
import numpy
X = numpy.array([['1', '2', '3']])
print 'Before pickle'
print '-'*30
print X
print '-'*30
def write(data, outfile):
        f = open(outfile, "w+b")
        pickle.dump(data, f)
        f.close()
def read(filename):
        f = open(filename)
        data = pickle.load(f)
        f.close()
        return data
if __name__ == "__main__":
        some_data = X
        write(some_data, "temp.file")
        read_data = read("temp.file")
        print 'After pickle'
        print '-'*30
        print read_data
        print '-'*30
