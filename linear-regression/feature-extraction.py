import glob
from sklearn import linear_model
from sklearn.feature_extraction.text import CountVectorizer

file_list = glob.glob("../course-cotrain-data/small/untag_*/*")

vectorizer = CountVectorizer(input='filename', stop_words='english')
X_train = vectorizer.fit_transform(file_list)
Y_train = []
for file_path in file_list:
	Y_train.append(not ('non_course' in file_path))
doc = vectorizer.transform([file_list[11]])
logreg = linear_model.LogisticRegression(dual=True)
logreg.fit(X_train, Y_train)
print logreg.predict(doc)
