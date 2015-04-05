import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import BernoulliNB
from sklearn import cross_validation
file_list = glob.glob("../untag_webkb/*/*/*/*")
categories = ['course', 'department', 'faculty', 'other', 'project', 'staff', 'student']
vectorizer = CountVectorizer(input='filename', stop_words='english', encoding='latin1')
y = []

for file_path in file_list:
	y.append(file_path.split('/')[3])

file_train, file_test, y_train, y_test = train_test_split(file_list, y, test_size=0.3)

x_train = vectorizer.fit_transform(file_train)
clf = BernoulliNB()
#clf.fit(x_train,y_train)
#multiclass_logistic_regression.fit(x_train, y_train)

# start testing


scores = cross_validation.cross_val_score(clf, x_train, y_train, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
# x_test = vectorizer.transform(file_test)
# y_hat = clf.predict(x_test)
# print accuracy_score(y_test,y_hat)