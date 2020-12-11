import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import os
import csv
import datetime
import time

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

############################################################Students Interface###############################################################
class Page1(Page):
   def assure_path_exists(self,path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
   def check_haarcascadefile(self):
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        self.destroy()
   def TrackImages(self):
    pass
   def TakeImages(self):
    self.check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    self.assure_path_exists("StudentDetails/")
    self.assure_path_exists("TrainingImage/")
    serial = 0
    print(1)
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
  


  ##doing above
   def psw(self):
    pass
   def tick(self,clock):
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    # clock.after(200,self.tick)
   def clear(self,txt,message1):
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


   def clear2(self,txt2,message1):
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

   
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # cont=tk.Frame(self)
        self.show1()
   def show1(self):
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
        window=self
        window.configure(background="black")
        frame1 = tk.Frame(window, bg="#00aeff")
        frame1.place(relx=0.12, rely=0.17, relwidth=0.39, relheight=0.80)
        frame2 = tk.Frame(window, bg="#00aeff")
        frame2.place(relx=0.52, rely=0.17, relwidth=0.38, relheight=0.80)
        message3 = tk.Label(window, text="Face Recognition Based Attendance System(Students)" ,fg="white",bg="black" ,width=50 ,height=1,font=('times', 29, ' bold '))
        message3.place(relx=0.09, rely=0.01)
        frame3 = tk.Frame(window, bg="#c4c6ce")
        frame3.place(relx=0.52, rely=0.09, relwidth=0.13, relheight=0.07)

        frame4 = tk.Frame(window, bg="#c4c6ce")
        frame4.place(relx=0.26, rely=0.09, relwidth=0.25, relheight=0.07)

        datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   ", fg="orange",bg="black" ,width=55,height=1,font=('times', 20, ' bold '))
        datef.pack(fill='both',expand=1)

        clock = tk.Label(frame3,fg="orange",bg="black" ,width=55 ,height=1,font=('times', 20, ' bold '))
        clock.pack(fill='both',expand=1)
        self.tick(clock)
        head2 = tk.Label(frame2, text=" For New Registrations                       ", fg="black",bg="#3ece48", width=50 ,font=('times', 17, ' bold ') )
        head2.grid(row=0,column=0)

        head1 = tk.Label(frame1, text=" For Already Registered                       ", fg="black",bg="#3ece48", width=50 ,font=('times', 17, ' bold ') )
        head1.place(x=0,y=0)

        lbl = tk.Label(frame2, text="Enter ID",width=30  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
        lbl.place(x=-100, y=55)

        txt = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=50, y=88)

        lbl2 = tk.Label(frame2, text="Enter Name",width=30,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
        lbl2.place(x=-83, y=140)

        txt2 = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold ')  )
        txt2.place(x=50, y=173)

        message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
        message1.place(x=7, y=230)

        message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        message.place(x=7, y=450)

        lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
        lbl3.place(x=100, y=115)
        res=0
        message.configure(text='Total Registrations till now  : '+str(res))



        ##TreeView Attendance Table
        tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
        tv.column('#0',width=82)
        tv.column('name',width=130)
        tv.column('date',width=133)
        tv.column('time',width=133)
        tv.grid(row=2,column=0,padx=(20,0),pady=(150,0),columnspan=4)
        tv.heading('#0',text ='ID')
        tv.heading('name',text ='NAME')
        tv.heading('date',text ='DATE')
        tv.heading('time',text ='TIME')

        #Scroll bar
        scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
        scroll.grid(row=2,column=4,padx=(0,20),pady=(150,0),sticky='ns')
        tv.configure(yscrollcommand=scroll.set)
        #buttons
        clearButton = tk.Button(frame2, text="Clear", command=self.clear(txt,message1)  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
        clearButton.place(x=335, y=86)
        clearButton2 = tk.Button(frame2, text="Clear", command=self.clear2(txt2,message1)  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
        clearButton2.place(x=335, y=172)    
        takeImg = tk.Button(frame2, text="Take Images", command=self.TakeImages()  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        takeImg.place(x=50, y=300)
        trainImg = tk.Button(frame2, text="Save Profile", command=self.psw() ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        trainImg.place(x=50, y=380)
        trackImg = tk.Button(frame1, text="Take Attendance", command=self.TrackImages()  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        trackImg.place(x=30,y=50)
        quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        quitWindow.place(x=50, y=450)


############################################################Teachers Interface###############################################################
class Page2(Page):
   def TrackImages(self):
    pass
   def TakeImages(self):
    pass
   def psw(self):
    pass
   def stuattend(self):
    pass
   def tick(self,clock):
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    # clock.after(200,self.tick)

   def clear(self,txt,message1):
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


   def clear2(self,txt2,message1):
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

   
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
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
        window=self
        window.configure(background="black")
        frame1 = tk.Frame(window, bg="#00aeff")
        frame1.place(relx=0.12, rely=0.17, relwidth=0.39, relheight=0.80)
        frame2 = tk.Frame(window, bg="#00aeff")
        frame2.place(relx=0.52, rely=0.17, relwidth=0.38, relheight=0.80)
        message3 = tk.Label(window, text="Face Recognition Based Attendance System(Teachers)" ,fg="white",bg="black" ,width=50 ,height=1,font=('times', 29, ' bold '))
        message3.place(relx=0.09, rely=0.01)
        frame3 = tk.Frame(window, bg="#c4c6ce")
        frame3.place(relx=0.52, rely=0.09, relwidth=0.13, relheight=0.07)

        frame4 = tk.Frame(window, bg="#c4c6ce")
        frame4.place(relx=0.26, rely=0.09, relwidth=0.25, relheight=0.07)

        datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   ", fg="orange",bg="black" ,width=55,height=1,font=('times', 20, ' bold '))
        datef.pack(fill='both',expand=1)

        clock = tk.Label(frame3,fg="orange",bg="black" ,width=55 ,height=1,font=('times', 20, ' bold '))
        clock.pack(fill='both',expand=1)
        self.tick(clock)
        head2 = tk.Label(frame2, text=" For New Registrations                       ", fg="black",bg="#3ece48", width=50 ,font=('times', 17, ' bold ') )
        head2.grid(row=0,column=0)

        head1 = tk.Label(frame1, text=" For Already Registered                       ", fg="black",bg="#3ece48", width=50 ,font=('times', 17, ' bold ') )
        head1.place(x=0,y=0)

        lbl = tk.Label(frame2, text="Enter ID",width=30  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
        lbl.place(x=-100, y=55)

        txt = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=50, y=88)

        lbl2 = tk.Label(frame2, text="Enter Name",width=30,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
        lbl2.place(x=-83, y=140)

        txt2 = tk.Entry(frame2,width=30 ,fg="black",font=('times', 15, ' bold ')  )
        txt2.place(x=50, y=173)

        message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
        message1.place(x=7, y=230)

        message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        message.place(x=7, y=450)

        lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
        lbl3.place(x=100, y=115)
        res=0
        message.configure(text='Total Registrations till now  : '+str(res))



        ##TreeView Attendance Table
        tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
        tv.column('#0',width=82)
        tv.column('name',width=130)
        tv.column('date',width=133)
        tv.column('time',width=133)
        tv.grid(row=2,column=0,padx=(20,0),pady=(150,0),columnspan=4)
        tv.heading('#0',text ='ID')
        tv.heading('name',text ='NAME')
        tv.heading('date',text ='DATE')
        tv.heading('time',text ='TIME')

        #Scroll bar
        scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
        scroll.grid(row=2,column=4,padx=(0,20),pady=(150,0),sticky='ns')
        tv.configure(yscrollcommand=scroll.set)
        #buttons
        clearButton = tk.Button(frame2, text="Clear", command=self.clear(txt,message1)  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
        clearButton.place(x=335, y=86)
        clearButton2 = tk.Button(frame2, text="Clear", command=self.clear2(txt2,message1)  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
        clearButton2.place(x=335, y=172)    
        takeImg = tk.Button(frame2, text="Take Images"  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        takeImg.place(x=50, y=300)
        trainImg = tk.Button(frame2, text="Save Profile", command=self.psw() ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        trainImg.place(x=50, y=380)
        trackImg = tk.Button(frame1, text="Take Attendance", command=self.TrackImages()  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        trackImg.place(x=30,y=50)
        stattend = tk.Button(frame1, text="View Students Attendance", command=self.stuattend()  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        stattend.place(x=50, y=450)
        quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        quitWindow.place(x=50, y=550)


##Admins####
class Page3(Page):
   def TrackImages(self):
    pass
   def TakeImages(self):
    pass
   def psw(self):
    pass
   def tick(self,clock):
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    # clock.after(200,self.tick)

   def clear(self,txt,message1):
    txt.delete(0, 'end')
    res = ""
    message1.configure(text=res)


   def clear2(self,txt2,message1):
    txt2.delete(0, 'end')
    res = ""
    message1.configure(text=res)

   
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
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
        window=self
        window.configure(background="black")
        frame2 = tk.Frame(window, bg="#00aeff")
        frame2.place(relx=0.28, rely=0.17, relwidth=0.38, relheight=0.80)
        message3 = tk.Label(window, text="Face Recognition Based Attendance System(Admins)" ,fg="white",bg="black" ,width=50 ,height=1,font=('times', 29, ' bold '))
        message3.place(relx=0.09, rely=0.01)
        frame3 = tk.Frame(window, bg="#c4c6ce")
        frame3.place(relx=0.52, rely=0.09, relwidth=0.13, relheight=0.07)

        frame4 = tk.Frame(window, bg="#c4c6ce")
        frame4.place(relx=0.26, rely=0.09, relwidth=0.25, relheight=0.07)

        datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   ", fg="orange",bg="black" ,width=55,height=1,font=('times', 20, ' bold '))
        datef.pack(fill='both',expand=1)

        clock = tk.Label(frame3,fg="orange",bg="black" ,width=55 ,height=1,font=('times', 20, ' bold '))
        clock.pack(fill='both',expand=1)
        self.tick(clock)
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

        message1 = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
        message1.place(x=7, y=230)

        message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        message.place(x=7, y=450)
        res=0
        message.configure(text='Total Registrations till now  : '+str(res))
        clearButton = tk.Button(frame2, text="Clear", command=self.clear(txt,message1)  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
        clearButton.place(x=335, y=86)
        clearButton2 = tk.Button(frame2, text="Clear", command=self.clear2(txt2,message1)  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
        clearButton2.place(x=335, y=172)
        newtenrol=tk.Button(frame2, text="New Teachers Enrolments"  ,fg="black"  ,bg="#ea2a2a"  ,width=34 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        newtenrol.place(x=50, y=250)
        newstenrol=tk.Button(frame2, text="New Students Enrolments"  ,fg="black"  ,bg="#ea2a2a"  ,width=34 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        newstenrol.place(x=50, y=320)
        trainImg = tk.Button(frame2, text="Save Profile", command=self.psw() ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        trainImg.place(x=50, y=380)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Students",bg="yellow" ,command=p1.lift)
        b2 = tk.Button(buttonframe, text="Teachers",bg="yellow" ,command=p2.lift)
        b3 = tk.Button(buttonframe, text="Admin",bg="yellow", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p3.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Attendance System")
    main = MainView(root)
    main.pack(side="top", fill="both",expand=True)
    root.wm_geometry("400x400")
    root.mainloop()