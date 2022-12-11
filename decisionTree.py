import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import seaborn as sns

data = pd.read_csv("chessDataFinal.csv")
# print(data.head())
predict = "result"

le = preprocessing.LabelEncoder()
materialDifference = le.fit_transform(list(data["materialDifference"]))
colour = le.fit_transform(list(data["colour"]))
plyNumber = le.fit_transform(list(data["plyNumber"]))
check = le.fit_transform(list(data["check"]))
whiteQueenExists = le.fit_transform(list(data["whiteQueenExists"]))
blackQueenExists = le.fit_transform(list(data["blackQueenExists"]))
numOfSquaresWhiteAttacks = le.fit_transform(list(data["numOfSquaresWhiteAttacks"]))
numOfSquaresBlackAttacks = le.fit_transform(list(data["numOfSquaresBlackAttacks"]))

result = le.fit_transform(list(data["result"]))

X = list(zip(materialDifference, colour, plyNumber, check, whiteQueenExists, blackQueenExists, numOfSquaresWhiteAttacks, numOfSquaresBlackAttacks))  # features
y = list(result)  # label

# where test_size is the amount of testing data where 1.0 is all data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=20)

#ax = sns.displot(data=data, x="totalMaterial")
#plt.show()
# ax = sns.displot(data = data, x="Age")


# define classification algorithm
dt_clf = tree.DecisionTreeClassifier(max_depth=4, criterion="entropy")
dt_clf = dt_clf.fit(x_train, y_train)

# generating predictions
y_pred = dt_clf.predict(x_test)

from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
print(f1)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

from sklearn.metrics import precision_score

presco = precision_score(y_test, y_pred)
print(presco)

from sklearn.metrics import recall_score

recsco = recall_score(y_test, y_pred)
print(recsco)
