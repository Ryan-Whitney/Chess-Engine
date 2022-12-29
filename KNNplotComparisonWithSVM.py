"""
Manually entered KNN and SVM values for comparison
"""

import matplotlib.pyplot as plt

xlabels = ["KNN", "SVM"]
accuracies = [74.4, 62.6]

plt.bar(xlabels, accuracies)
plt.ylim(58, 78)
plt.ylabel('Accuracy (%)')
plt.xlabel('Model Type')
plt.title('KNN Results')
plt.show()
