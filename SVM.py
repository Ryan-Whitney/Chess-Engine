"""
Generates SVM model for chosen kernel type. Plots accuracy.
"""

from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv("chessData.csv")

le = preprocessing.LabelEncoder()
result = le.fit_transform(list(data["result"]))

material_difference = le.fit_transform(list(data["material_difference"]))
total_white_material = le.fit_transform(list(data["total_white_material"]))
total_black_material = le.fit_transform(list(data["total_black_material"]))
colour = le.fit_transform(list(data["colour"]))
ply_number = le.fit_transform(list(data["ply_number"]))
white_in_check = le.fit_transform(list(data["white_in_check"]))
black_in_check = le.fit_transform(list(data["black_in_check"]))
white_queen_exists = le.fit_transform(list(data["white_queen_exists"]))
black_queen_exists = le.fit_transform(list(data["black_queen_exists"]))
num_squares_white_attacks = le.fit_transform(list(data["num_squares_white_attacks"]))
num_squares_black_attacks = le.fit_transform(list(data["num_squares_black_attacks"]))

X = list(zip(material_difference, total_white_material, total_black_material, colour, ply_number, white_in_check,
             black_in_check, white_queen_exists, black_queen_exists,
             num_squares_white_attacks, num_squares_black_attacks))  # features
y = list(result)  # label

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

svmModel = svm.SVC(kernel="rbf")
#svmModel = svm.SVC(kernel="linear")
#svmModel = svm.SVC(kernel="sigmoid")
#svmModel = svm.SVC(kernel="poly")

svmModel.fit(x_train, y_train)
y_predict = svmModel.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_predict)
print(accuracy)

xlabel = ["RBF"]

plt.bar(xlabel, accuracy*100)
plt.ylim(50, 70)
plt.ylabel('Accuracy (%)')
plt.xlabel('Kernel Type')
plt.title('SVM Result')
plt.show()

print("done running SVM.py")
