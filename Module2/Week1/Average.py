import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('dog.jpeg')
gray_img_01 = np.mean(img, axis=2)  # Your code here
print(gray_img_01[0, 0])
