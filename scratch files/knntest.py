# from https://github.com/patrickloeber/MLfromscratch/blob/master/mlfromscratch/knn.py

from collections import Counter
import csv
import numpy as np


gameResultTemp = []

with open('../garbage/gameResult.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        # print(line)
        gameResultTemp.append(line)
        var1 = ([list(map(int, i)) for i in gameResultTemp])
        gameResultData = sum(var1, [])

print(gameResultData)

totalMaterialTemp = []

with open('../garbage/totalMaterial.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        # print(line)
        totalMaterialTemp.append(line)
        totalMaterialData = ([list(map(int, i)) for i in totalMaterialTemp])

print(totalMaterialData[1][0])  # [game - odd=white, even=black][move #]  --value is total material


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_idx = np.argsort(distances)[: self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]


if __name__ == "__main__":
    # Imports
    from matplotlib.colors import ListedColormap
    from sklearn import datasets
    from sklearn.model_selection import train_test_split

    cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    k = 3
    clf = KNN(k=k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("KNN classification accuracy", accuracy(y_test, predictions))