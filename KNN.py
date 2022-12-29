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
plt.ylim(65, 76)
plt.ylabel('Accuracy (%)')
plt.title('KNN Results With Varying K Values')
plt.xlabel('K Value')

plt.show()

print("done running KNN.py")
