import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

data = pd.read_csv("chessDataFinal.csv")
# data = SelectKBest(chi2, k=2).fit_transform(data)
# print(data.head())
#data = (data - data.mean()) / data.std()  # normalize the data between 0 and 1
#data=(data-data.min())/(data.max()-data.min())  # min max normalization of data

# print(data.head())

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

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, shuffle=True)

temp = []
maxK = 21
i = 0
# print(data.head())

# print(data.shape)

for k in range(1, maxK, 2):  # (start, stop, step)
    print(str(k))
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    temp.append(accuracy)
    i = i + 1
    print(accuracy)

print(sum(temp) / i)  # average accuracy of KNN over all values of K
# ax = sns.displot(data=data, x="materialDifference")
# plt.show()


"""
model = KNeighborsClassifier(n_neighbors=21)

model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print(accuracy)
"""

print("done running KNN")
