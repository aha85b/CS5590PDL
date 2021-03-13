
# Import Libraries
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
# Importing StandardScaler Normalization
from sklearn.preprocessing import StandardScaler
# Importing dataset
dataset = pd.read_csv("breastcancer.csv")
# dropping id attribute
dataset = dataset.drop(columns = 'id')
# Change diagnosis values with B and M to 1 and 0
dataset['diagnosis'] = dataset['diagnosis'].map({'B': 1, 'M': 0}).astype(int)
dataset = dataset.values
print(dataset)

# Apply StandardScaler for normalization
sc = StandardScaler()
sc_dataset = sc.fit_transform(dataset[:, 0:31])


X_train, X_test, Y_train, Y_test = train_test_split(sc_dataset, dataset[:,0],
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