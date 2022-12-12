from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv("chessDataFinal.csv")

predict = "result"

result = (list(data["result"]))

materialDifference = (list(data["materialDifference"]))
totalWhiteMaterial = (list(data["totalWhiteMaterial"]))
totalBlackMaterial = (list(data["totalBlackMaterial"]))
colour = (list(data["colour"]))
plyNumber = (list(data["plyNumber"]))
whiteInCheck = (list(data["whiteInCheck"]))
blackInCheck = (list(data["blackInCheck"]))
whiteQueenExists = (list(data["whiteQueenExists"]))
blackQueenExists = (list(data["blackQueenExists"]))
numSquaresWhiteAttacks = (list(data["numSquaresWhiteAttacks"]))
numSquaresBlackAttacks = (list(data["numSquaresBlackAttacks"]))

X = list(zip(materialDifference, totalWhiteMaterial, totalBlackMaterial, colour, plyNumber, whiteInCheck, blackInCheck,
             whiteQueenExists, blackQueenExists,
             numSquaresWhiteAttacks, numSquaresBlackAttacks))  # features
y = list(result)  # label

svmAccuracies = []

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="rbf")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
svmAccuracies.append(accuracy)
print(accuracy)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="linear")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
svmAccuracies.append(accuracy)
print(accuracy)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="poly")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
svmAccuracies.append(accuracy)
print(accuracy)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="sigmoid")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
svmAccuracies.append(accuracy)
print(accuracy)
"""
xlabels = ["RBF", "Linear", "Polynomial", "Sigmoid"]
svmAccuracies = []

plt.bar(xlabels, svmAccuracies)
plt.ylim(50, 65)
plt.ylabel('Accuracy (%)')
plt.xlabel('Kernel Type')
#plt.title('SVM Results')
plt.show()

"""
print("done running SVM.py")
