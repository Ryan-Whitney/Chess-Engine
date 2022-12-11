import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

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
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, shuffle=True)
# Scale data
# ss = StandardScaler().fit(x_train)
# X_train, X_test = ss.transform(x_train), ss.transform(x_test)
# print(x_train)

var = 231
for k in range(1, var, 6):  # (start, stop, step)
    print(str(k))
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    print(accuracy)

# ax = sns.displot(data=data, x="totalMaterial")
# plt.show()

"""
model = KNeighborsClassifier(n_neighbors=21)

model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print(accuracy)
"""
