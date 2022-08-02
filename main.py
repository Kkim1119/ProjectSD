import time
import math
import random
from math import *
from PIL import Image, ImageDraw

#---------------------------------------------
def scan(robot_x, robot_y, img):
    degree = 0
    pixels = 1
    ten_rad = 10 * (pi/180)
    coord_list = []
    scan_px = img.load()
    #print(scan_px [robot_x+1, robot_y+1])

    while not(degree <= -(2*pi-ten_rad)):
        init_x = int((pixels * cos(degree))) + robot_x
        init_y = int((pixels * sin(degree))) + robot_y
        scan_px[init_x,init_y] = (0,0,255)
        init2_x = int(((pixels + 1) * cos(degree))) + robot_x
        init2_y = int(((pixels + 1) * sin(degree))) + robot_y

        next_pixel = scan_px[init2_x,init2_y]
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
def draw_points(list, img):
    dp_px = img.load()
    for i in range(len(test_list)-1):
        dp_px[test_list[i][0], test_list[i][1]] = (255, 0, 0)
        connect = ImageDraw.Draw(img)
        dots = [(test_list[i][0], test_list[i][1]), (test_list[i+1][0], test_list[i+1][1])]
        connect.line(dots, fill="red")
        if(i == len(test_list)-2):
            final_dots = [(test_list[0][0], test_list[0][1]), (test_list[len(test_list)-1][0], test_list[len(test_list)-1][1])]
            connect.line(final_dots, fill="red")

#------------------------------------------------
w, h = 1000, 1000
room = [(100, 100), (700, 700)]
object = [(150, 150), (300, 400)]
ROOM_BORDER_WIDTH = 7
ROBOT_WIDTH = 5

# creating new Image object
main_img = Image.new("RGB", (w, h), color="white")
px = main_img.load()

points_img = Image.new("RGB", (w, h), color="white")
# create line image
img1 = ImageDraw.Draw(main_img)  #Draws the room border(img1 -> room border)
img1.rectangle(room, outline="#000000", width=ROOM_BORDER_WIDTH)

img2 = ImageDraw.Draw(main_img)
img2.rectangle(object, fill="#000000")

NUMBER_OF_SCANS = 10

for i in range(NUMBER_OF_SCANS):
    rand_x = random.randint(100 + ROOM_BORDER_WIDTH + ROBOT_WIDTH, 700 - ROOM_BORDER_WIDTH-ROBOT_WIDTH) #allows the robot square to be inside room even if random spawns it right next to a border
    rand_y = random.randint(100 + ROOM_BORDER_WIDTH + ROBOT_WIDTH,700 - ROOM_BORDER_WIDTH-ROBOT_WIDTH) #allows the robot square to be inside room even if random spawns it right next to a border

    while(px[rand_x,rand_y][0] == 0 and px[rand_x,rand_y][1] == 0 and px[rand_x,rand_y][2] == 0):
        rand_x = random.randint(100 + ROOM_BORDER_WIDTH + ROBOT_WIDTH,
                            700 - ROOM_BORDER_WIDTH - ROBOT_WIDTH)
        rand_y = random.randint(100 + ROOM_BORDER_WIDTH + ROBOT_WIDTH,
                            700 - ROOM_BORDER_WIDTH - ROBOT_WIDTH)

    px[rand_x,rand_y] = (0,0,255)
    robot = [(rand_x-10,rand_y-10),(rand_x+10,rand_y+10)]

    img3 = ImageDraw.Draw(main_img)
    img3.rectangle(robot, fill="red")

    test_list = scan(rand_x,rand_y,main_img)
    draw_points(test_list, points_img)


main_img.show()
time.sleep(5)
points_img.show()


