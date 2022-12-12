# To plot KNN and SVM results, results manually entered

from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

xlabels = ["KNN", "SVM"]
accuracies = [74.4, 62.6]

plt.bar(xlabels, accuracies)
plt.ylim(58, 78)
plt.ylabel('Accuracy (%)')
plt.xlabel('Model Type')
plt.show()