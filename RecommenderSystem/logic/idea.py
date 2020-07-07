# -*- coding: utf-8 -*-
# loading libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import OneHotEncoder #dummy
#from sklearn.preprocessing import LabelEncoder #discretización


# loading data
data = pd.read_csv('RecommenderSystem/data/advertising.csv')

# splitting data
X = data.iloc[:, [0, 1, 2, 3, -4]].values
y = data.iloc[:, -1].values

# Preprocessing
scaler = StandardScaler()
scaler.fit(X[:, 0:-1])

X[:, 0:-1] = scaler.transform(X[:, 0:-1])

# Splitting the data
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=0)

# Defining the architecture
lr = LogisticRegression()
lr.fit(xtrain, ytrain)

# Evaluating the model
ypred = lr.predict(xtest)

score = lr.score(xtest, ytest)
print(score)

# testing our model
model = data.iloc[:, [0, 1, 2, 3, -4]]

new_user = np.array([[60.0, 21, 100000, 150, 1]])
new_user[:, :-1] = scaler.transform(new_user[:, :-1])
lr.predict(new_user)
