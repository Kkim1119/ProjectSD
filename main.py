from tkinter import *
import time
import math
from math import *

def scan(canvas): #creates the scan lines that show the robot doing a 360 degree scan
    degree = 0
    counter = 0 #method of checking that 36 lines are made
    ten_rad = 10 * (pi/180) #Changes 10 degrees into radians
    #Radians is the default for cosine. So any value given to cos and sin is received as a radian

    #Sets the coordinates of the end of the line in relation to the robot's coordinates
    while not(degree <= -(2*pi-ten_rad)):
        new_line_x = (ROBOT_X * cos(degree)) + ROBOT_X
        new_line_y = (ROBOT_Y * sin(degree)) + ROBOT_Y

        canvas.create_line(ROBOT_X, ROBOT_Y, new_line_x, new_line_y)
        canvas.update()

        time.sleep(0.1)
        degree -= ten_rad

        counter += 1
        
#--------------------------------------------------
def find_coord(event):  #Used to check how the coordinates work inside the canvas
    print(event.x,event.y)

#--------------------------------------------------
window = Tk()

ROBOT_X = 500
ROBOT_Y = 500

room = Canvas(window, height= 600, width=600)
room.pack()

room.bind("<Button-1>",find_coord)

robot_image = PhotoImage(file="robot.png")
robot_image = robot_image.zoom(5) #Makes the image 5 times bigger
robot_image = robot_image.subsample(32) #shrinks down the image(higher number -> gets smaller

robot = room.create_image(ROBOT_X,ROBOT_Y, image=robot_image)
room.create_rectangle(100, 100, 250, 250, fill="Black")

scan(room)

window.mainloop()


