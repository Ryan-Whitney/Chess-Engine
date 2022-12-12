# To plot KNN and SVM results, results manually entered

from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

xlabels = ["RBF", "Linear", "Polynomial", "Sigmoid"]
svmAccuracies = [62.5, 61.9, 63.2, 52.8]

plt.bar(xlabels, svmAccuracies)
plt.ylim(50, 65)
plt.ylabel('Accuracy (%)')
plt.xlabel('Kernel Type')
#plt.title('SVM Results')
plt.show()