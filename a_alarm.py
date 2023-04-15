from tkinter import *
 
from tkinter import messagebox

import time, sys

from pygame import mixer

from PIL import Image, ImageTk



def alarm():

	alarm_time=user_input.get()

	if alarm_time=="":

		messagebox.askretrycancel("Error Message","Please Enter Value")

	else:

		while True:

			time.sleep(1)

			if (alarm_time==time.strftime("%H:%M")):

				playmusic()

def playmusic():

	mixer.init()

	mixer.music.load('aa.mp3')

	mixer.music.play()

	while mixer.music.get_busy():

		time.sleep(30)

		mixer.music.stop()

		sys.exit()


root=Tk()

root.title("ALARM CLOCK")

root.geometry("600x370")

canvas=Canvas(root,width=600,height=380)

image=ImageTk.PhotoImage(Image.open("al.jpg"))

canvas.create_image(0,0,anchor=NW,image=image)

canvas.pack()

header=Frame(root)



box1=Frame(root)

box1.place(x=260,y=150)

box2=Frame(root)

box2.place(x=272,y=200)




user_input=Entry(box1,font=('Arial Bold',25),width=5)

user_input.grid(row=0,column=2)



start_button=Button(box2,text="Start",font=('Arial Narrow',16,'bold'),width=5,command=alarm)

start_button.grid(row=2,column=2)



root.mainloop()




