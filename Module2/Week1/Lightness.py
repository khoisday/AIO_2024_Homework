import matplotlib.image as mpimg
import numpy as np

# Download image
# ! gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB

img = mpimg.imread('dog.jpeg')
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
print(gray_img_01[0, 0])
