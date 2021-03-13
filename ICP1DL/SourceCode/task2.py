# Import Libraries
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Import dataset
dataset = pd.read_csv("breastcancer.csv")
# Drop id columns
dataset = dataset.drop(columns = 'id')
# Change diagnosis attributes values from M and B to 0 and 1
dataset['diagnosis'] = dataset['diagnosis'].map({'B': 1, 'M': 0}).astype(int)
# Set Values
dataset = dataset.values
print(dataset)

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:31], dataset[:,31],
                                                    test_size=0.25, random_state=87)
# Create Sequential Model
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=31, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))