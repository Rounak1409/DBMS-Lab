import tkinter as tk
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

clock=""
txt=""
txt2=""
txt3=""
txt4=""
txt5=""
st=""
message1=""
message=""
tv=""


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)


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
    mess._show(title='Contact us', message="Please contact us on : 'shubhamkumar8180323@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        st.destroy()

###################################################################################


#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        pass
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

def clear3():
    txt3.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME','','ADDRESS']
    assure_path_exists("AdminDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("AdminDetails\AdminDetails.csv")
    if exists:
        with open("AdminDetails\AdminDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("AdminDetails\AdminDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()

    


    Id = (txt.get())
    name = (txt2.get())
    address = (txt3.get())
    if (((name.isalpha()) or (' ' in name)) and ((address.isalpha()) or (' ' in address))):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name,'',address]
        with open('AdminDetails\AdminDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)
        if (address.isalpha() == False):
            res = "Enter Correct address"
            message.configure(text=res)

########################################################################################



def admin():
    global clock
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
    st = tk.Tk()
    st.geometry("1280x820")
    st.resizable(True,True)
    st.title("Attendance System")
    st.configure(background='#262523')

    frame2 = tk.Frame(st, bg="#00aeff")
    frame2.place(relx=0.28, rely=0.17, relwidth=0.38, relheight=0.80)
    message3 = tk.Label(st, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=50 ,height=1,font=('times', 29, ' bold '))
    message3.place(relx=0.09, rely=0.01)
    frame3 = tk.Frame(st, bg="#c4c6ce")
    frame3.place(relx=0.52, rely=0.09, relwidth=0.13, relheight=0.07)

    frame4 = tk.Frame(st, bg="#c4c6ce")
    frame4.place(relx=0.26, rely=0.09, relwidth=0.25, relheight=0.07)

    datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   ", fg="orange",bg="#262523" ,width=55,height=1,font=('times', 20, ' bold '))
    datef.pack(fill='both',expand=1)

    clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 20, ' bold '))
    clock.pack(fill='both',expand=1)
    tick()
    head2 = tk.Label(frame2, text=" For New Registrations                       ", fg="black",bg="#3ece48", width=50 ,font=('times', 17, ' bold ') )
    head2.grid(row=0,column=0)

    

    lbl = tk.Label(frame2, text="Enter ID",width=30  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
    lbl.place(x=-100, y=55)

    txt = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold '))
    txt.place(x=50, y=88)

    lbl2 = tk.Label(frame2, text="Enter Name",width=30,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
    lbl2.place(x=-83, y=140)
    txt2 = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold ')  )
    txt2.place(x=50, y=173)

    lbl3 = tk.Label(frame2, text="Enter Address",width=30,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
    lbl3.place(x=-83, y=230)
    txt3 = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold ')  )
    txt3.place(x=50, y=270)

    

    message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
    message1.place(x=7, y=410)

    message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
    message.place(x=7, y=540)

    
    res=0
    exists = os.path.isfile("AdminDetails\AdminDetails.csv")
    if exists:
        with open("AdminDetails\AdminDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0
    message.configure(text='Total Registrations till now  : '+str(res))
    


        #buttons
    clearButton = tk.Button(frame2, text="Clear", command=clear  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton.place(x=335, y=86)
    clearButton2 = tk.Button(frame2, text="Clear", command=clear2  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton2.place(x=335, y=172)    
    clearButton3 = tk.Button(frame2, text="Clear", command=clear3  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton3.place(x=335, y=269) 
    
    takeImg = tk.Button(frame2, text="Take Images", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    takeImg.place(x=50, y=440)
    trainImg = tk.Button(frame2, text="Save Profile", command=psw ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    trainImg.place(x=50, y=490)
    quitWindow = tk.Button(frame2, text="Back to Guide", command=st.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    quitWindow.place(x=50, y=600)