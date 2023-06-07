import matplotlib.image as mplimg
import matplotlib.pyplot as  plt
import numpy as np

#image read
filename = "img00.jpg"
image = mplimg.imread(filename)

#goal: eliminate all noice and return black/white image of the road surface
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    color_select = np.zeros_like(img[:, :, 0])
    above_thesh = (img[:, :, 0] > rgb_thresh[0]) \
        & (img[:, :, 1] > rgb_thresh[1]) \
        & (img[:, :, 2] > rgb_thresh[2])
    color_select[above_thesh] = 1
    return color_select

#gaites for the threshold
red_threshold = 160
green_threshold = 160
blue_threshold = 160


rgb_threshold = (red_threshold, green_threshold, blue_threshold)

# pixels below the thresholds
colorsel = color_thresh(image, rgb_thresh=rgb_threshold)

# Display the original image and black/white               
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)
ax2.imshow(colorsel, cmap='gray')
ax2.set_title('Your Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()
