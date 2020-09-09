import matplotlib.pyplot as plt
import numpy as np

nx = 512
ny = 512
Data = np.fromfile('slice150.raw', dtype='uint16')
array = np.reshape(Data, [nx, ny])

plt.imshow(array, cmap="gray")
plt.title(" Original Image")
plt.savefig('Original Image', dpi=500)
plt.show()

# a) profile line through line 256

plt.plot(array[256], '-g')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title('Profile line through line 256')
plt.savefig('Profile Line', dpi=300)
plt.show()

# b) mean and variance value of Dataset

print('Mean Value :', array.mean())
print('Variance Value :', array.var())

# c) Histogram of the Dataset(Line Graph)

counts, bins = np.histogram(array, bins=100)
y = 0.5 * (bins[1:] + bins[:-1])
frequency = counts / 20
plt.plot(y, frequency)
plt.xlabel("Occurrence")
plt.ylabel("Frequency")
plt.title(" Line graph")
plt.savefig('Line Graph', dpi=500)
plt.show()

# d) Linear Transformation

temp = np.round((array - array.min()) / (array.max() - array.min()) * 255)
plt.imshow(temp, cmap='gray')
plt.title("Linear transformation")
plt.savefig("Linear Transformation", dpi=500)
plt.show()

# e) Non - Linear Transformation

nonlinear = np.zeros(shape=(512, 512))

for i in range(0, 512):
    for j in range(0, 512):
        nonlinear[i][j] = np.log10(array[i][j] + 1)
temp = np.round((nonlinear - nonlinear.min()) / (nonlinear.max() - nonlinear.min()) * 255)
plt.imshow(temp, cmap='gray')
plt.title("Non-Linear transformation")
plt.savefig("Non-Linear Transformation", dpi=500)
plt.show()

# f) Box Car filter

convolution = np.zeros(shape=(512, 512))


def mean(a, b):
    kernel = np.zeros(shape=(11, 11))
    sumOfKernel = 0
    for v in range(a, a + 11):
        for u in range(b, b + 11):
            kernel[v - a][u - b] = array[v][u]
            sumOfKernel += array[v][u]
    meanValue = sumOfKernel / (11 * 11)
    return meanValue


for x in range(0, 502):
    for y in range(0, 502):
        convolution[x + 5][y + 5] = mean(x, y)
plt.imshow(convolution, cmap="gray")
plt.title("Box Car Filter")
plt.savefig("Box Car Filter", dpi=500)
plt.show()

# g) Median Filter

Median = np.zeros(shape=(512, 512))


def sortKernel(kernel):
    kernel = np.median(kernel)
    return kernel


def medianFilter(a, b):
    kernel = np.zeros(shape=(11, 11))
    for u in range(a, a + 11):
        for v in range(b, b + 11):
            kernel[u - a][v - b] = array[u][v]

    kernel = sortKernel(kernel)
    return kernel


for x in range(0, 502):
    for y in range(0, 502):
        Median[x + 5][y + 5] = medianFilter(x, y)
plt.imshow(Median, cmap="gray")
plt.title("Median Filter")
plt.savefig("Median Filter", dpi=500)
plt.show()
