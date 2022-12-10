from sklearn import svm
import sklearn
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


data = pd.read_csv("chessDataFinal.csv")

predict = "result"

le = preprocessing.LabelEncoder()
totalMaterial = le.fit_transform(list(data["totalMaterial"]))
# colour = le.fit_transform(list(data["colour"]))
# scaledMoveNumber = le.fit_transform(list(data["scaledMoveNumber"]))
result = le.fit_transform(list(data["result"]))

X = list(zip(totalMaterial))  # features
y = list(result)  # label

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

linearModel = linear_model.LinearRegression()
linearModel.fit(x_train, y_train)
accuracy = linearModel.score(x_test, y_test)
#print(accuracy)

#qdaModel = QDA()
#qdaModel.fit(x_train, y_train)
#accuracy = qdaModel.predict(x_test)
#print(accuracy)

#clf = LinearDiscriminantAnalysis()
#clf.fit(x_train, y_train)
#accuracy = clf.predict(x_test)
#print(accuracy)