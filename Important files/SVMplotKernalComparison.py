"""
Manually entered SVM values for comparison of different kernels
"""

import matplotlib.pyplot as plt

xlabels = ["RBF", "Linear", "Polynomial", "Sigmoid"]
svmAccuracies = [63.1, 61.7, 62.3, 50.6]

plt.bar(xlabels, svmAccuracies)
plt.ylim(50, 65)
plt.ylabel('Accuracy (%)')
plt.xlabel('Kernel Type')
plt.title('SVM Results')
plt.show()
