import glob
from sklearn import linear_model
from sklearn import naive_bayes
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier

file_list = glob.glob("../untag_webkb/*/*/*/*")
categories = ['course', 'department', 'faculty', 'other', 'project', 'staff', 'student']
vectorizer = CountVectorizer(input='filename', stop_words='english', encoding='latin1')
y = []

for file_path in file_list:
	y.append(file_path.split('/')[2])

file_train, file_test, y_train, y_test = train_test_split(file_list, y, test_size=0.3)

x_train = vectorizer.fit_transform(file_train)
multiclass_logistic_regression = OneVsRestClassifier(linear_model.LogisticRegression())

multiclass_logistic_regression.fit(x_train, y_train)

# start testing
x_test = vectorizer.transform(file_test)
y_hat = multiclass_logistic_regression.predict(x_test)
print accuracy_score(y_test,y_hat)