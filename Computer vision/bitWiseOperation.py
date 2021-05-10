import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('img2.png')

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img2, img1)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
cv2.imshow('img3', bitAnd)
cv2.imshow('img4', bitOr)
cv2.imshow('img5', bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()
