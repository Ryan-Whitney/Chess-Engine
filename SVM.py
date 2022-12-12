from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics

data = pd.read_csv("chessDataFinal.csv")

predict = "result"
le = preprocessing.LabelEncoder()
result = le.fit_transform(list(data["result"]))

materialDifference = le.fit_transform(list(data["materialDifference"]))
totalWhiteMaterial = le.fit_transform(list(data["totalWhiteMaterial"]))
totalBlackMaterial = le.fit_transform(list(data["totalBlackMaterial"]))
colour = le.fit_transform(list(data["colour"]))
plyNumber = le.fit_transform(list(data["plyNumber"]))
whiteInCheck = le.fit_transform(list(data["whiteInCheck"]))
blackInCheck = le.fit_transform(list(data["blackInCheck"]))
whiteQueenExists = le.fit_transform(list(data["whiteQueenExists"]))
blackQueenExists = le.fit_transform(list(data["blackQueenExists"]))
numSquaresWhiteAttacks = le.fit_transform(list(data["numSquaresWhiteAttacks"]))
numSquaresBlackAttacks = le.fit_transform(list(data["numSquaresBlackAttacks"]))

X = list(zip(materialDifference, totalWhiteMaterial, totalBlackMaterial, colour, plyNumber, whiteInCheck, blackInCheck,
             whiteQueenExists, blackQueenExists,
             numSquaresWhiteAttacks, numSquaresBlackAttacks))  # features
y = list(result)  # label



x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="poly")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
print(accuracy)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="poly")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy1 = metrics.accuracy_score(y_test, y_predict)
print(accuracy1)


