from tkinter import *
import time

def drag_robot(event):
    room.move(robot,event.x,event.y)
    room.update()
    print(event.x,event.y)

window = Tk()



room = Canvas(window, height= 600, width=600)
room.pack()

robot_image = PhotoImage(file="robot.png")
robot_image = robot_image.zoom(5) #Makes the image 5 times bigger
robot_image = robot_image.subsample(32) #shrinks down the image(higher number -> gets smaller
robot = room.create_image(500,500, image=robot_image)



room.create_rectangle(100, 100, 250, 250, fill="Black")


window.mainloop()


