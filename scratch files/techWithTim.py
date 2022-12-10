import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("../chessDataFinal.csv")
print(data.head())  # To check if our data is loaded correctly

predict = "result"

le = preprocessing.LabelEncoder()
totalMaterial = le.fit_transform(list(data["totalMaterial"]))
colour = le.fit_transform(list(data["colour"]))
scaledMoveNumber = le.fit_transform(list(data["scaledMoveNumber"]))
result = le.fit_transform(list(data["result"]))


X = list(zip(totalMaterial, colour, scaledMoveNumber))  # features
y = list(result)  # label

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1, random_state=7)

model = KNeighborsClassifier(n_neighbors=11)

model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print("KNN accuracy: " + accuracy)

