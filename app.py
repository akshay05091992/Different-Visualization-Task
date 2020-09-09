import matplotlib.pyplot as plt
import numpy as np

X = np.zeros([6724])
Y = np.zeros([6724])
DX = np.zeros([6724])
DY = np.zeros([6724])

Array = np.sqrt((DX ** 2) + (DY ** 2))

with open("field2.irreg.txt", 'r') as f:
    Data = f.readlines()
Data = Data[6:]

for i in range(0, 6724):
    temp = Data[i].split(" ")
    X[i] = float(temp[0])
    Y[i] = float(temp[1])
    DX[i] = float(temp[3])
    DY[i] = float(temp[4])
    Array = np.sqrt((DX ** 2) + (DY ** 2))
q = plt.quiver(X, Y, DX, DY, Array,
               # units='xy',
               angles='xy',
               scale=15,
               # scale_units='xy',
               width=0.001,
               headwidth=6.5,
               headlength=8,
               headaxislength=8,
               # minshaft=2,
               # minlength=2,
               cmap=plt.cm.jet)

cbar = plt.colorbar(q)
cbar.set_ticks([0.0, 0.5, 1.0])
cbar.set_ticklabels(["Low", "Medium", "High"])
plt.axis('equal')
plt.title("Vector Field Visualization")
plt.xlabel("X Equivalent of Vectors")
plt.ylabel("Y Equivalent of Vectors")
plt.grid(which='both')
plt.savefig('Plot', dpi=300)
plt.show()
