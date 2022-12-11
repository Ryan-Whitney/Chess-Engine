from sklearn import svm
import sklearn
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

data = pd.read_csv("chessDataFinal.csv")

predict = "result"

le = preprocessing.LabelEncoder()
result = le.fit_transform(list(data["result"]))

materialDifference = le.fit_transform(list(data["materialDifference"]))
colour = le.fit_transform(list(data["colour"]))
plyNumber = le.fit_transform(list(data["plyNumber"]))
whiteInCheck = le.fit_transform(list(data["whiteInCheck"]))
blackInCheck = le.fit_transform(list(data["blackInCheck"]))
whiteQueenExists = le.fit_transform(list(data["whiteQueenExists"]))
blackQueenExists = le.fit_transform(list(data["blackQueenExists"]))
numOfSquaresWhiteAttacks = le.fit_transform(list(data["numOfSquaresWhiteAttacks"]))
numOfSquaresBlackAttacks = le.fit_transform(list(data["numOfSquaresBlackAttacks"]))


X = list(zip(materialDifference, colour, plyNumber, whiteInCheck, blackInCheck, whiteQueenExists, blackQueenExists, numOfSquaresWhiteAttacks, numOfSquaresBlackAttacks))  # features
y = list(result)  # label

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="rbf")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
print(accuracy)
