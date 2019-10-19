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

#Image path to be changed
address = ocr('ImagePath')
print('Address:-\n'+address)

le = len(address)

revaddress = address[le::-1]

revpinsearch = re.search(r'\d\d\d\d\d\d', revaddress)
revpincode = revpinsearch.group(0)

le = len(revpincode)
pincode = revpincode[le::-1]
print('Pincode:- '+pincode)