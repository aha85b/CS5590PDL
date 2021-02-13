
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Importing data set
train_df = pd.read_csv('glass.csv')
X = train_df.drop("Type", axis=1)
Y = train_df["Type"]

# Training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# using navie bays
gnb = GaussianNB()

# Showing the result of test data
Y_prediction = gnb.fit(X_train, y_train).predict(X_test)
acc_gnb = round(gnb.score(X_test, y_test) * 100)

# Calculating the accuracy
print("Accuracy is:", acc_gnb)
print(classification_report(y_test, Y_prediction))