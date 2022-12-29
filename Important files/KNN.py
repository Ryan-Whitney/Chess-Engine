"""
Generates KNN model for varying values of K and plots them.
"""

import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt

data = pd.read_csv("chessData.csv")
data = (data - data.min()) / (data.max() - data.min())  # min max normalization of data

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

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, shuffle=True)

knn_accuracy = []
k_vals = []
upper_k_bound = 17

for k in range(1, upper_k_bound, 2):
    print(str(k))
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    knn_accuracy.append(accuracy * 100)
    k_vals.append(k)
    print(accuracy)

plt.bar(k_vals, knn_accuracy)
plt.ylim(65, 100)
plt.ylabel('Accuracy (%)')
plt.title('KNN Results With Varying K Values')
plt.xlabel('K Value')

plt.show()

print("done running KNN.py")
