from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_train_test = fetch_20newsgroups(subset='test', shuffle=False)

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')

X_train_tfdif = tfidf_vectorizer.fit_transform(twenty_train.data)
X_test_tfdif = tfidf_vectorizer.transform(twenty_train_test.data)

# Model Bulding
multi_nb = MultinomialNB()
multi_nb.fit(X_train_tfdif, twenty_train.target)

prediction = multi_nb.predict(X_test_tfdif)

multinomial_nb_score = round(metrics.accuracy_score(twenty_train_test.target, prediction), 2)
print("MultinomialNB accuracy is: ", multinomial_nb_score)

# Apply SVM
svc = SVC()
svc.fit(X_train_tfdif, twenty_train.target)
svc_score = round(svc.score(X_train_tfdif, twenty_train.target) * 100, 2)
print("SVC accuracy is: ", svc_score / 100)

