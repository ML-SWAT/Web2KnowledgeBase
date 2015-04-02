from glob import glob
from sklearn import tree
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals.six import StringIO
import pydot

# function:
#  get the decision tree by training data
# input:
#  X_train: of size [n_samples, n_features] holding the training samples
#  Y_train: of size [n_samples], holding the class labels for the training samples
# output:
def train(X_train, Y_train):

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, Y_train)

    #show the constructed dtree
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data)
    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("decision tree.pdf")
    return clf


# function:
#  read the data from html file and translate it into readable X and Y
def getData(path):
    file_list = glob(path)

    vectorizer = CountVectorizer(input='filename', stop_words='english',encoding='latin1')
    X = vectorizer.fit_transform(file_list)
    Y = []
    for file_path in file_list:
        Y.append(not ('non_course' in file_path))
    return X, Y

# function:
#  predict the label of testing data by implementing the constructed decision tree
# input:
#  clf: the constructed decision tree
#  X_test: of size [n_samples, n_features] holding the testing samples
# output:
def test(clf, X_test):
    Y_test_predict = clf.predict(X_test)
    return Y_test_predict

def getPrecision(Y_test_predict, Y_test_true):
    sum_total = Y_test_true.__len__();
    sum_wrong = 0;
    for label in Y_test_predict:
        if label != Y_test_predict:
            sum_wrong = sum_wrong + 1

    print "error rate: " + str(sum_wrong * 1.0 / sum_total)

if __name__=="__main__":
    X_train, Y_train = getData("../naive_bayes/*course_train/*")
    clf = train(X_train, Y_train)
    X_test, Y_test_true = getData("../naive_bayes/*course_test/*")
    Y_test_predict = test(clf, X_test)
    getPrecision(Y_test_predict, Y_test_true)