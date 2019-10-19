from PIL import Image
import os
import tempfile
import subprocess
import sys
import re

def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents


import cv2


while True:
	cam = cv2.VideoCapture(0)
	cv2.namedWindow("test")
	ret, frame = cam.read()
	cv2.imshow("test", frame)
	if not ret:
        break
	img_name = "opencv_frame.png"
	cv2.imwrite(img_name, frame)
    
	address = ocr('opencv_frame.png')	
	print('Address:-\n'+address)

	le = len(address)

	revaddress = address[le::-1]

	revpinsearch = re.search(r'\d\d\d\d\d\d', revaddress)
	revpincode = revpinsearch.group(0)

	le = len(revpincode)
	pincode = revpincode[le::-1]
	print('Pincode:- '+pincode)

	k = cv2.waitKey(1)
	if k%256 == 32:
        break
    

cam.release()

cv2.destroyAllWindows()