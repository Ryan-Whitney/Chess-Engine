"""
Generates SVM model for chosen kernel type. Plots accuracy.
"""

from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv("chessData.csv")

le = preprocessing.LabelEncoder()
result = le.fit_transform(list(data["result"]))

materialDifference = le.fit_transform(list(data["materialDifference"]))
totalWhiteMaterial = le.fit_transform(list(data["totalWhiteMaterial"]))
totalBlackMaterial = le.fit_transform(list(data["totalBlackMaterial"]))
colour = le.fit_transform(list(data["colour"]))
plyNumber = le.fit_transform(list(data["plyNumber"]))
whiteInCheck = le.fit_transform(list(data["whiteInCheck"]))
blackInCheck = le.fit_transform(list(data["blackInCheck"]))
whiteQueenExists = le.fit_transform(list(data["white_queen_exists"]))
blackQueenExists = le.fit_transform(list(data["black_queen_exists"]))
numSquaresWhiteAttacks = le.fit_transform(list(data["numSquaresWhiteAttacks"]))
numSquaresBlackAttacks = le.fit_transform(list(data["numSquaresBlackAttacks"]))

X = list(zip(materialDifference, totalWhiteMaterial, totalBlackMaterial, colour, plyNumber, whiteInCheck, blackInCheck,
             whiteQueenExists, blackQueenExists,
             numSquaresWhiteAttacks, numSquaresBlackAttacks))  # features
y = list(result)  # label

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="rbf")
#svmModel = svm.SVC(kernel="linear")
#svmModel = svm.SVC(kernel="sigmoid")
#svmModel = svm.SVC(kernel="poly")

svmModel.fit(x_train, y_train)
y_predict = svmModel.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_predict)
print(accuracy)

xlabel = ["RBF"]

plt.bar(xlabel, accuracy*100)
plt.ylim(50, 70)
plt.ylabel('Accuracy (%)')
plt.xlabel('Kernel Type')
plt.title('SVM Result')
plt.show()

print("done running SVM.py")
