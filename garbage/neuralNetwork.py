import sklearn
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist
data = pd.read_csv("chessDataFinal.csv")

predict = "result"

le = preprocessing.LabelEncoder()
totalMaterial = le.fit_transform(list(data["totalMaterial"]))
colour = le.fit_transform(list(data["colour"]))
scaledMoveNumber = le.fit_transform(list(data["scaledMoveNumber"]))
result = le.fit_transform(list(data["result"]))


X = list(zip(totalMaterial, colour, scaledMoveNumber))  # features
y = list(result)  # label

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.15)






