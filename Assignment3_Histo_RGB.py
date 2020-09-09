import numpy as np
import matplotlib.pyplot as plt

nx = 500
ny = 500
File = np.loadtxt('i170b2h0_t0.txt', delimiter=',', dtype=str)
NewFile = (np.core.defchararray.replace(File, old='"', new=' ', count=nx * ny)).astype(np.float)
FlipArray2 = np.flipud(NewFile)

File1 = np.loadtxt('i170b1h0_t0.txt', delimiter=',', dtype=str)
NewFile1 = (np.core.defchararray.replace(File1, old='"', new=' ', count=nx * ny)).astype(np.float)
FlipArray1 = np.flipud(NewFile1)

File2 = np.loadtxt('i170b3h0_t0.txt', delimiter=',', dtype=str)
NewFile2 = (np.core.defchararray.replace(File2, old='"', new=' ', count=nx * ny)).astype(np.float)
FlipArray3 = np.flipud(NewFile2)

File3 = np.loadtxt('i170b4h0_t0.txt', delimiter=',', dtype=str)
NewFile3 = (np.core.defchararray.replace(File3, old='"', new=' ', count=nx * ny)).astype(np.float)
FlipArray4 = np.flipud(NewFile3)

#  max value, the min value, the mean value and the variance value of this 2D data set
#
# print('Maximum Value :', np.max(FlipArray2))
# print('Minimum Value :', np.min(FlipArray2))
# print('Mean Value :', np.mean(FlipArray2))
# print('Variance Value :', np.var(FlipArray2))
#
# # profile line through the line with the maximum value of this 2D data set
#
Axis = np.where(FlipArray2 == np.max(FlipArray2))
Coordinates = list(zip(Axis[0], Axis[1]))
print(Coordinates)
plt.plot(FlipArray2[67], '-g')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.yscale("log")
plt.title('Profile line through line maximum value')
plt.savefig('Profile Line', dpi=300)
plt.show()
#
# # Display a histogram of this 2D data set

# LogValue = np.log(FlipArray2) + 1
# u, v = np.unique(LogValue, return_counts=True)
# plt.plot(u, v, '-')
# plt.title("Freq Distribution")
# plt.ylabel("Frequency")
# plt.yscale("log")
# plt.xlabel("Data Value")
# plt.xscale("log")
# plt.title(" Line graph")
# plt.savefig('Line Graph', dpi=500)
# plt.show()
#
# # Rescale values to range between 0 and 255 using your own transformation
#
# transformation = np.zeros(shape=(500, 500))
#
# for i in range(0, 500):
#     for j in range(0, 500):
#         transformation[i][j] = np.log10(FlipArray2[i][j] + 1)
# temp = (transformation - transformation.min()) / (transformation.max() - transformation.min()) * 255
# plt.imshow(temp, cmap='gray')
# plt.colorbar()
# plt.title("Rescale values to range between 0 and 255 with log transformation ")
# plt.savefig("Log Transformation", dpi=500)
# plt.clim([temp.min(),temp.max()])
# plt.show()

# Histogram equalization for each band

# BAND1 = np.zeros(shape=(500, 500))
# for i in range(0, 500):
#     for j in range(0, 500):
#         BAND1[i][j] = FlipArray1[i][j]
# ImageFlatten = BAND1.flatten()
# cdf_b, bins, arg = plt.hist(ImageFlatten, bins='auto', range=(0, 256), cumulative=True, density=True)
# NewImage = np.interp(ImageFlatten, bins[:-1], cdf_b * 255)
# FinalImage = np.reshape(NewImage, (500, 500))
# # plt.imshow(FinalImage, cmap='gray')
# plt.colorbar()
# plt.title(" Histogram equalization on i170b1h0_t0 ")
# plt.savefig("BAND1", dpi=500)
# plt.clim(0, 255)
# plt.show()
#
# BAND2 = np.zeros(shape=(500, 500))
# for i in range(0, 500):
#     for j in range(0, 500):
#         BAND2[i][j] = FlipArray2[i][j]
# ImageFlatten2 = BAND2.flatten()
# cdf_i, bins, arg = plt.hist(ImageFlatten2, bins='auto', range=(0, 256), cumulative=True, density=True)
# NewImage2 = np.interp(ImageFlatten2, bins[:-1], cdf_i * 255)
# FinalImage2 = np.reshape(NewImage2, (500, 500))
# plt.imshow(FinalImage2, cmap='gray')
# plt.colorbar()
# plt.title(" Histogram equalization on i170b2h0_t0 ")
# plt.savefig("BAND2", dpi=500)
# plt.clim(0, 255)
# plt.show()
#
# BAND3 = np.zeros(shape=(500, 500))
# for i in range(0, 500):
#     for j in range(0, 500):
#         BAND3[i][j] = FlipArray3[i][j]
# ImageFlatten = BAND3.flatten()
# cdf_g, bins, arg = plt.hist(ImageFlatten, bins='auto', range=(0, 256), cumulative=True, density=True)
# NewImage3 = np.interp(ImageFlatten, bins[:-1], cdf_g * 255)
# FinalImage3 = np.reshape(NewImage3, (500, 500))
# # plt.imshow(FinalImage3, cmap='gray')
# plt.colorbar()
# plt.title(" Histogram equalization on i170b3h0_t0")
# plt.savefig("BAND3", dpi=500)
# plt.clim(0, 255)
# plt.show()
#
# BAND4 = np.zeros(shape=(500, 500))
# for i in range(0, 500):
#     for j in range(0, 500):
#         BAND4[i][j] = FlipArray4[i][j]
# ImageFlatten = BAND4.flatten()
# cdf_r, bins, arg = plt.hist(ImageFlatten, bins='auto', range=(0, 256), cumulative=True, density=True)
# NewImage4 = np.interp(ImageFlatten, bins[:-1], cdf_r * 255)
# FinalImage4 = np.reshape(NewImage4, (500, 500))
# plt.imshow(FinalImage4, cmap='gray')
# plt.colorbar()
# plt.title(" Histogram equalization on i170b4h0_t0")
# plt.savefig("BAND4", dpi=500)
# plt.clim(0, 255)
# plt.show()


#  Combine the Histo-equalized data set to an RGB-image

# def meanpixel(rgb):
#     return (rgb - rgb.min()) * 255 / (rgb.max() - rgb.min())
#
#
# rgbimage = np.zeros((500, 500, 3), 'uint16')
#
# redpixel = meanpixel(FinalImage4)
# greenpixel = meanpixel(FinalImage3)
# bluepixel = meanpixel(FinalImage)
#
# for i in range(0, 500):
#     for j in range(0, 500):
#         rgbimage[i, j, 0] = redpixel[i][j]
#         rgbimage[i, j, 1] = greenpixel[i][j]
#         rgbimage[i, j, 2] = bluepixel[i][j]
#
# plt.imshow(rgbimage)
# plt.colorbar()
# plt.title(" Histo-Equalized data set to an RGB-image ")
# plt.savefig("RGB Image", dpi=500)
# plt.clim(0, 255)
# plt.show()
