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

# course_file_list = glob.glob("untag_/cotraining_data/*/*/course/*")
# non_course_file_list = glob.glob("untag_/cotraining_data/*/*/non-course/*")
all_list = glob.glob("untag_/cotraining_data/*/inlinks/*/*")
vectorizer = CountVectorizer(input='filename', stop_words='english', encoding='latin1')


#print course_file_list
m=vectorizer.fit_transform(all_list)
m=m.toarray()
print type(m)

numpy.savetxt("matrix2.csv", m, delimiter=",")
#print m.shape
# for file_path in file_list:
# 	y.append(file_path.split('/')[3])
#
# file_train, file_test, y_train, y_test = train_test_split(file_list, y, test_size=0.3)
#
# x_train = vectorizer.fit_transform(file_train)
# x_train = x_train.toarray()