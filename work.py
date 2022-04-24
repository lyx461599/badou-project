from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt

#灰度图
img = plt.imread("lenna.png")

plt.subplot(221)
plt.imshow(img)

img_gary = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gary,cmap='gray')
#二值化
img_binary = np.where(img_gary >=0.5, 1 ,0)
plt.subplot(223)
plt.imshow( img_binary,cmap='gray')

plt.show()