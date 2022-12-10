from sklearn import svm
import sklearn
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

data = pd.read_csv("chessDataFinal.csv")

predict = "result"

le = preprocessing.LabelEncoder()
totalMaterial = le.fit_transform(list(data["totalMaterial"]))
colour = le.fit_transform(list(data["colour"]))
scaledMoveNumber = le.fit_transform(list(data["scaledMoveNumber"]))
result = le.fit_transform(list(data["result"]))

X = list(zip(totalMaterial))  # features
y = list(result)  # label

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="rbf")
svmModel.fit(x_train, y_train)

y_predict = svmModel.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_predict)
print(accuracy)
