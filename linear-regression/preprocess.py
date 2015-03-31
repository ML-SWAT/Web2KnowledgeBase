#!/usr/bin/python
from __future__ import print_function
import string
import glob
import array
from string import maketrans
from sklearn import linear_model
from sklearn.feature_extraction.text import CountVectorizer
import numpy
dictionary = []

file_list = glob.glob("../course-cotrain-data/fulltext/untag_*/*")
Y = array.array('l')
X = numpy.zeros((len(file_list), 23153))
count = 0;
for file_path in file_list:
	if 'non-course' in file_path:
		Y.append(0)
	else:
		Y.append(1)

	web_file = open(file_path, 'r')
	source = web_file.read()
	source = source.lower()
	source = source.translate(string.maketrans("",""), string.punctuation)
	word_list = source.split()
	index = -1
	for word in word_list:
	    if word not in dictionary:
	        dictionary.append(word)
	        index = len(dictionary) - 1
	    else:
	    	index = dictionary.index(word)
	    X[count][index] += 1
	count += 1;

# fy = open('y.dat','w')
# print(Y, file=fy)
# fy.close()
# fx = open('x.dat','w')
# print(X, file=fx)
# fx.close()
# fd = open('dic.dat','w')
# print(dictionary, file=fd)
# fd.close()