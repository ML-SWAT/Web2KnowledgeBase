
measurements = [['Dubai', 33.],['London',  12.],['San Fransisco',  18.]]

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()

vec.fit_transform(measurements).toarray()
# array([[  1.,   0.,   0.,  33.],
#        [  0.,   1.,   0.,  12.],
#        [  0.,   0.,   1.,  18.]])