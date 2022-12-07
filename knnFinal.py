

import csv

gameResultTemp = []

with open('gameResult.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        # print(line)
        gameResultTemp.append(line)
        var1 = ([list(map(int, i)) for i in gameResultTemp])
        gameResultData = sum(var1, [])

print(gameResultData)

totalMaterialTemp = []

with open('totalMaterial.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        # print(line)
        totalMaterialTemp.append(line)
        totalMaterialData = ([list(map(int, i)) for i in totalMaterialTemp])

print(totalMaterialData[1][0])  # [game - odd=white, even=black][move #]  --value is total material



class KNN:
    def __init__(self, k=3):
        self.k = k;

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):


        

        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):







