
import pandas as pd


train_df= pd.read_csv('train.csv') # Import data form train.csv file to be set
print(train_df.columns.values) # Print columns names
print(train_df['Survived'].value_counts(dropna='False'))


X_train= train_df.drop("Survived", axis=1)  # drop survived from the set
Y_train= train_df["Survived"]


train_df['Sex'] = train_df['Sex'].map({'female': 1, 'male': 0}).astype(int) # Categorizing sex


print(train_df['Survived'].corr(train_df['Sex'])) # Calculation between survived and sex passengers


result = train_df[["Survived","Sex"]].groupby(['Sex'], as_index = False).mean() # Correlation between sex and survived
print(result)