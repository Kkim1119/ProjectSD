import time
import math
from math import *
from PIL import Image, ImageDraw

#---------------------------------------------
def scan(robot_x, robot_y, img):
    degree = 0
    pixels = 1
    ten_rad = 10 * (pi/180)
    coord_list = []
    px = img.load()
    print(px [robot_x+1, robot_y+1])

    while not(degree <= -(2*pi-ten_rad)):
        init_x = int((pixels * cos(degree))) + robot_x
        init_y = int((pixels * sin(degree))) + robot_y
        px[init_x,init_y] = (0,0,255)
        init2_x = int(((pixels + 1) * cos(degree))) + robot_x
        init2_y = int(((pixels + 1) * sin(degree))) + robot_y

        next_pixel = px[init2_x,init2_y]
        if(next_pixel[0]==0 and next_pixel[1]==0 and next_pixel[2]==0):
            degree -= ten_rad
            pixels = 1
            coord_list.append([init2_x,init2_y])
        else:
            pixels += 1
            init_x -= robot_x
            init_y -= robot_y
            init2_x -= robot_x
            init2_y -= robot_y

    return coord_list

#------------------------------------------------


w, h = 1000, 1000
room = [(100, 100), (700, 700)]
object = [(150, 150), (300, 400)]
robot = [(490,490),(510,510)]

ROBOT_X = 500
ROBOT_Y = 500

# creating new Image object
img = Image.new("RGB", (w, h), color="white")
px = img.load()

# create line image
img1 = ImageDraw.Draw(img)  #Draws the room border(img1 -> room border)
img1.rectangle(room, outline="#000000", width=7)


img2 = ImageDraw.Draw(img)
img2.rectangle(object, fill="#000000")

img3 = ImageDraw.Draw(img)
img3.rectangle(robot, fill="red")

px[ROBOT_X,ROBOT_Y] = (0,0,255)



print(test_list := scan(ROBOT_X,ROBOT_Y,img))
for i in test_list:
    px[i[0],i[1]]= (255,0,0)

img.show()

#time.sleep(5)
#img.show()

