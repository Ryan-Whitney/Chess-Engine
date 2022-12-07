# Ryan Whitney
# Offical python-chess docs code was used
# https://python-chess.readthedocs.io/en/latest/pgn.html

import csv
import chess.pgn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import sklearn
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# from sklearn import datasets
# iris = datasets.load_iris()
# x,y = iris.data, iris.target

temp = []
with open('gameResult.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        #print(line)
        temp.append(line)
        var1 = ([list(map(int, i)) for i in temp])  # var1 is a 2d list of ints
        var2 = sum(var1, [])



#  var is the game result, 1 or 0
print(var2)

totalMaterialList = []
with open('totalMaterial.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        #print(line)
        totalMaterialList.append(line)
        var3 = ([list(map(int, i)) for i in totalMaterialList])  # var3 is a 2d list of the totalMaterial for each game

#var3 =  ( [list( map(int,i) ) for i in totalMaterialList] )
#var4 = sum(var3, [])
#print(var4)
print(var3)
white = var3[0]
black = var3[1]


# var1 - game results -- 1d array (val for each game)
# var3 - total material for each move of each game -- 2d array (array of vals for each game)

xLabels = var2
yFeatures = var3

#x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(xLabels, yFeatures, test_size = 0.1)









