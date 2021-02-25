from tkinter import *
import sys
from tkinter import PhotoImage
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import subprocess
import keyboard


root = Tk()
root.title('Crack Detection Interface')
root.iconphoto(True, PhotoImage(file="/home/eee/CrackUI/yolo_crack.png"))#used to make image to become app icon
textlabel = Label(root, text = "Welcome to our Crack Detection User Interface. Please refrain from running both features at the same time. Happy detecting!", fg='purple')
textlabel.config(font=("Helvetica", 16))
textlabel.place(x= 130,y = 300)

####Changing size of application
root.geometry('1400x1000')

####Creating main icon
main = Image.open('/home/eee/CrackUI/yolo_crack.png')
main2=main.resize((1000,200),Image.ANTIALIAS)
main_photo=ImageTk.PhotoImage(main2)

main_icon = Label(image=main_photo)
main_icon.place(x=200 ,y=50 )

####Creating the start button, assign it a variable then putting variable into Button() function

#start = PhotoImage(file = "/home/eee/UItest/start.png") [NOT USED NOW AS NEED TO RESIZE IMAGE]

start = Image.open('/home/eee/CrackUI/start.png')
start2=start.resize((250,250),Image.ANTIALIAS) 
main_start=ImageTk.PhotoImage(start2)        


def startClick():
    myLabel = Label(root, 
    os.chdir("/home/eee/darknet-yolo"),
    os.system("./darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3-crack_updated.weights -thresh  0.123 & ") )
    myLabel.pack()


button_start = Button(root, image=main_start,activebackground='green',borderwidth = 0, command=startClick)
button_start.place(x = 150,y = 400)

####Creating the stop button assign it a variable then putting variable into Button() function

quit = Image.open('/home/eee/CrackUI/stop.png')
quit2=quit.resize((250,250),Image.ANTIALIAS) 
main_quit=ImageTk.PhotoImage(quit2)    

def quitmaster():
    os.system("killall python3 image_viewer.py") 
    os.system("killall ./darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3-crack_updated.weights -thresh 0.123 ")
    root.destroy
 
button_quit = Button(root,image= main_quit,activebackground='red', borderwidth = 0, command=quitmaster )#used to exit the app
button_quit.pack(side = BOTTOM) #pack needed to place it into the application

#####Creating the image viewer button


viewer = Image.open('/home/eee/CrackUI/viewer.png')
viewer2=viewer.resize((250,250),Image.ANTIALIAS)
main_viewer=ImageTk.PhotoImage(viewer2)        

def viewClick():

    myLabelview = Label(root, os.chdir("/home/eee/imageviewer"), os.system("python3 image_viewer.py &") )
    myLabelview.pack()
    button_quit.pack(side = BOTTOM)

button_view = Button(root, image = main_viewer,activebackground='cyan', borderwidth = 0, command = viewClick)
button_view.place(x=1000 ,y=400 )

root.mainloop()
