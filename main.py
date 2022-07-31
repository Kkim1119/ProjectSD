from tkinter import *
import time

def scan(image,canvas): #creates the scan lines that show the robot doing a 360 degree scan
    degree = 0
    canvas.create_line(ROBOT_X,ROBOT_Y,ROBOT_X,0)

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

scan(robot,room)

window.mainloop()


