import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Acquire the data and create our environment
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10 ,6)

# training data set
train = pd.read_csv('datatest.csv')
print('\n', 'The described data: ', '\n', train.revenue.describe(), '\n')

#handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()

print('Columns Value: ')

print(sum(data.isnull().sum() != 0))

print('\n')

# Perform a correlation
corr = data.corr()
print('Top Five: ', '\n', corr['revenue'].sort_values(ascending=False)[:5], '\n')

#Build a linear model
y = np.log(train['revenue'])
X = data.drop(['revenue', 'Id'], axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

print('--------------------------------------')
#Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)

from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

print('\n', '--------------------------------------')
