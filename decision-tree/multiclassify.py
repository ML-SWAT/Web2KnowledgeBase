import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import tree
from decisionTree import *
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier

if __name__=="__main__":
    file_list = glob.glob("../untag_webkb/*/*/*/*")
    categories = ['course', 'department', 'faculty', 'other', 'project', 'staff', 'student']
    vectorizer = CountVectorizer(input='filename', stop_words='english', encoding='latin1')
    y = []

    for file_path in file_list:
        y.append(file_path.split('/')[3])

    file_train, file_test, y_train, y_test_true = train_test_split(file_list, y, test_size=0.3)
    x_train = vectorizer.fit_transform(file_train)
    x_train = x_train.toarray()
    # x_train = []
    # for file in file_list:
    #     print "ddd"
    #     print file
    #     x_train = vectorizer.fit_transform(file);
        # x_train = [x_train, vectorizer.fit_transform(file).toarray()]
    # x_train = x_train.toarray()
    x_test_predict = vectorizer.transform(file_test)
    x_test_predict = x_test_predict.toarray();
    print "----------------multiple classification decision tree----------------"
    decisionmake(x_train, y_train, x_test_predict, y_test_true)
