import cv2
import numpy as np
import itertools

def CropImage():
	img = cv2.imread('address.jpg')
	#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	x = img.shape[0]
	y = img.shape[1]
	x_new = int(x/2)
	y_new = int(y/2)

	#crop_img = img_gray[x_new:x, y_new:y]

	resize_img = cv2.resize(img  , (y_new , x_new))

	cv2.imshow("Image", resize_img)
	cv2.waitKey(0)
	cv2.imwrite('01.png',resize_img)

CropImage()