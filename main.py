############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import students as stu
import teachers as tech
import admin as ad

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################
def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)


###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'rounakjainajmera@gmail.com' or 'pulakpathak.cs18@rvce.edu.in'")

master=""
old=""
new=""
nnew=""
def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

###################################################################################
def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%D-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
        '02':'February',
        '03':'March',
        '04':'April',
        '05':'May',
        '06':'June',
        '07':'July',
        '08':'August',
        '09':'September',
        '10':'October',
        '11':'November',
        '12':'December'
        }



#ui
window = tk.Tk()
window.geometry("1280x820")
window.resizable(True,True)
window.title("Attendance System")
window.configure(background='#262523')

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=50 ,height=1,font=('times', 29, ' bold '))
message3.place(relx=0.07, rely=0.01)
message4 = tk.Label(window, text="Press the button of your choice" ,fg="white",bg="#262523" ,width=50 ,height=1,font=('times', 29, ' bold '))
message4.place(x=100, rely=0.19)
frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.13, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.26, rely=0.09, relwidth=0.25, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   ", fg="orange",bg="#262523" ,width=55,height=1,font=('times', 20, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 20, ' bold '))
clock.pack(fill='both',expand=1)
tick()

clearButton = tk.Button(window, text="Admin", command=ad.admin  ,fg="black"  ,bg="#ea2a2a"  ,width=40 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=500, y=200)
clearButton2 = tk.Button(window, text="Students", command=stu.students  ,fg="black"  ,bg="#ea2a2a"  ,width=40 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=500, y=300)    
clearButton3 = tk.Button(window, text="Teachers", command=tech.teachers  ,fg="black"  ,bg="#ea2a2a"  ,width=40 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton3.place(x=500, y=400) 
clearButton4 = tk.Button(window, text="Change Password", command=change_pass  ,fg="black"  ,bg="#ea2a2a"  ,width=40 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton4.place(x=500, y=500)
clearButton5 = tk.Button(window, text="Contact Us", command=contact  ,fg="black"  ,bg="#ea2a2a"  ,width=40 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton5.place(x=500, y=600)    
clearButton6 = tk.Button(window, text="Exit", command=window.destroy  ,fg="black"  ,bg="#ea2a2a"  ,width=40 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton6.place(x=500, y=700) 




window.mainloop()
