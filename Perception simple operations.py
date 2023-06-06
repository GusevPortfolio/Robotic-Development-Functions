import matplotlib.image as mplimg
import matplotlib.pyplot as plt
import numpy as np

#Filename and see the initial photo
filename = "img01.jpg"
image=mplimg.imread(filename)
plt.imshow(image)
plt.show()

#See type, shape, min and max of pixel brightness
print(image.dtype, image.shape, np.min(image), np.max(image))

#Color channels separation
red_channel = np.copy(image)
green_channel = np.copy (image)
blue_channel = np.copy(image)
red_channel[:, :, [1, 2]] = 0 #change to zero green and blue
green_channel[:, :, [0, 2]] = 0 #change to zero red and blue
blue_channel[:, :, [0, 1]] = 0  #change to zero red and green

fig = plt.figure(figsize=(12, 3))
plt.subplot(131)
plt.imshow(red_channel)
plt.subplot(132)
plt.imshow(green_channel)
plt.subplot(133)
plt.imshow(blue_channel)
plt.show()