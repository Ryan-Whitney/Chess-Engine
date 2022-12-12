# To plot KNN and SVM results, results manually entered

from sklearn import svm
import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

xlabels = ["KNN", "SVM"]
svmAccuracies = [74.4, 62.5]

plt.bar(xlabels, svmAccuracies)
plt.ylim(58, 77)
plt.ylabel('Accuracy (%)')
plt.xlabel('Model')
#plt.title('SVM Results')
plt.show()