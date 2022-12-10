import matplotlib.pyplot as plt
import numpy as np

dataArray = np.genfromtxt('chessDataFinal.csv', delimiter=',', names=True)

plt.figure()
for col_name in dataArray.dtype.names:
    plt.plot(dataArray[col_name], label=col_name)
plt.legend()
plt.show()
