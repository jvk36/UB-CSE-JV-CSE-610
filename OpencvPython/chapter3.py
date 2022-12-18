# resizing and cropping

import cv2
import numpy as np

img = cv2.imread("Resources/test_image.png")
print(img.shape)

# RESIZING EXAMPLE
imgResize = cv2.resize(img, (400, 400)) # width, height
print(imgResize.shape)

# CROPPING EXAMPLE
imgCropped = img[0:150, 100:250] # height, width

cv2.imshow("Image", img)
cv2.imshow("ImageResized", imgResize)
cv2.imshow("ImageCropped", imgCropped)

cv2.waitKey(0)
