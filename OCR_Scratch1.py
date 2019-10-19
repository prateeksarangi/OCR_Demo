from PIL import Image
import numpy as np

im = Image.open("postcard-copy.jpg")

w,h = im.size
w = int(w)
h = int(h)

#2D-Array for area
area = []
for x in range(w):
    area.append([])
    for y in range(h):
        area[x].append(2) #number 0 is white, number 1 is black

#2D-Array for letter
letter = []
for x in range(50):
    letter.append([])
    for y in range(50):
        letter[x].append(0)

#2D-Array for label
label = []
for x in range(50):
    label.append([])
    for y in range(50):
        label[x].append(0)

#image to number conversion
pix = im.load()
threshold = 200
for x in range(w):
    for y in range(h):
        aaa = pix[x, y]
        bbb = aaa[0] + aaa[1] + aaa[2] #total value
        if bbb<=threshold:
            area[x][y] = 1
        if bbb>threshold:
            area[x][y] = 0
np.set_printoptions(threshold='nan', linewidth=10)

#matrix transponation
ccc = np.array(area) 
area = ccc.T #better solution?

#find all black pixel and set temporary label numbers
i=1
for x in range(40): # width (later)
    for y in range(40): # heigth (later)
        if area[x][y]==1:
            letter[x][y]=1
            label[x][y]=i
            i += 1

#connected components labeling
for x in range(40): # width (later)
    for y in range(40): # heigth (later)
        if area[x][y]==1:
            label[x][y]=i
            #if pixel has neighbour:
            if area[x][y+1]==1:
                #pixel and neighbour get the lowest label             
                pass # tomorrows work
            if area[x+1][y]==1:
                #pixel and neighbour get the lowest label             
                pass # tomorrows work            
            #should i also compare pixel and left neighbour?


im.save("output.jpg")
print('done')