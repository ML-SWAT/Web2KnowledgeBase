import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cross_validation
import numpy
from untag_script import *

# folder = "webkb"
# course_files = glob.glob("../cotraining_data/course-cotrain-data/fulltext/course/*")
# transcribe(course_files,'untag_binary/course/')
# non_course_files = glob.glob("../cotraining_data/course-cotrain-data/fulltext/non-course/*")
# transcribe(non_course_files,'untag_binary/non_course/')

#course_file_list = glob.glob("untag_/cotraining_data/*/*/course/*")
#non_course_file_list = glob.glob("untag_/cotraining_data/*/*/non-course/*")
all_list = glob.glob("untag_/cotraining_data/*/fulltext/*/*")
all_list2 = glob.glob("untag_/cotraining_data/*/inlinks/*/*")
vectorizer = CountVectorizer(input='filename', stop_words='english', encoding='latin1')

all = all_list+all_list2;
#print course_file_list
m=vectorizer.fit_transform(all)
#m2 = vectorizer.fit(all_list2)
m=m.toarray()
#m2 = m2.toarray()
print type(m)
print m.shape

m1=m[0:1051,:]
m2=m[1051:2102,:]
print m1.shape
print m2.shape
#print all_list.__len__()
#print all_list2.__len__()
numpy.savetxt("matrix1.csv", m1, delimiter=",")
numpy.savetxt("matrix2.csv", m2, delimiter=",")
#print m.shape
# for file_path in file_list:
# 	y.append(file_path.split('/')[3])
#
# file_train, file_test, y_train, y_test = train_test_split(file_list, y, test_size=0.3)
#
# x_train = vectorizer.fit_transform(file_train)
# x_train = x_train.toarray()