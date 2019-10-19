import cv2
import numpy as np
import itertools

def CropImage():
	img = cv2.imread('hqdefault.jpg')
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	x, y = img_gray.shape
	x_new = int(x/2)
	y_new = int(y/2)

	crop_img = img_gray[x_new:x, y_new:y]

	cv2.imshow("Image", crop_img)
	cv2.waitKey(0)
	cv2.imwrite('01.png',crop_img)

CropImage()