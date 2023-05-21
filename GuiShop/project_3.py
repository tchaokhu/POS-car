from tkinter import *
from tkinter import ttk
import tkinter as tk
import tempfile
import os
from tkinter import messagebox
import json
from ftplib import FTP
class pos:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant")
        self.root.geometry("1100x600")
        self.root.minsize(1100, 600)
        self.root.maxsize(1100, 600)
        self.root.configure(background='black')
        self.input_value = True

        #============เพิ่มรูป png รูปอาหาร 100x100==========
        self.menu1 = PhotoImage(file="./assets/menu1.png")
        self.menu2 = PhotoImage(file="./assets/menu2.png")
        self.menu3 = PhotoImage(file="./assets/menu3.png")
        self.menu4 = PhotoImage(file="./assets/menu4.png")
        self.menu5 = PhotoImage(file="./assets/menu5.png")
        self.menu6 = PhotoImage(file="./assets/menu1.png")
        self.menu7 = PhotoImage(file="./assets/menu2.png")
        self.menu8 = PhotoImage(file="./assets/menu3.png")
        self.menu9 = PhotoImage(file="./assets/menu4.png")
        self.menu10 = PhotoImage(file="./assets/menu5.png")
        self.exit = PhotoImage(file="./assets/exit.png")
        self.positive = PhotoImage(file="./assets/positive.png")
        self.negative = PhotoImage(file="./assets/negative.png")

        global operator
        operator=""

        data = {
            "Total_Price":"0",
            "Car_licence":"value1"
        }
        Total_Input = StringVar()
        Car_Input = StringVar()
        Itemmenu1 = StringVar()
        Itemmenu2 = StringVar()
        Itemmenu3 = StringVar()
        Itemmenu4 = StringVar()
        Itemmenu5 = StringVar()
        Itemmenu6 = StringVar()
        Itemmenu7 = StringVar()
        Itemmenu8 = StringVar()
        Itemmenu9 = StringVar()
        Itemmenu10 = StringVar()
        Total_Input.set(0)
        Itemmenu1.set(0)
        Itemmenu2.set(0)
        Itemmenu3.set(0)
        Itemmenu4.set(0)
        Itemmenu5.set(0)
        Itemmenu6.set(0)
        Itemmenu7.set(0)
        Itemmenu8.set(0)
        Itemmenu9.set(0)
        Itemmenu10.set(0)


        price = 0
        #=========================SubmitFunction=======================
        def menu1negative():
            NoMenu1 = int(Itemmenu1.get())
            CostofMenu1 = NoMenu1 - 1
            if(CostofMenu1 < 0):
                CostofMenu1 = 0
            else:
                Itemmenu1.set(CostofMenu1)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*60)))
            
        def menu1positive():
            NoMenu1 = int(Itemmenu1.get())
            CostofMenu1 = NoMenu1 + 1
            Itemmenu1.set(CostofMenu1)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*60)))
            
        def menu2negative():
            NoMenu2 = int(Itemmenu2.get())
            CostofMenu2 = NoMenu2 - 1
            if(CostofMenu2 < 0):
                CostofMenu2 = 0
            else:
                Itemmenu2.set(CostofMenu2)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*40)))
            
        def menu2positive():
            NoMenu2 = int(Itemmenu2.get())
            CostofMenu2 = NoMenu2 + 1
            Itemmenu2.set(CostofMenu2)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*40)))
            
        def menu3negative():
            NoMenu3 = int(Itemmenu3.get())
            CostofMenu3 = NoMenu3 - 1
            if(CostofMenu3 < 0):
                CostofMenu3 = 0
            else:
                Itemmenu3.set(CostofMenu3)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*40)))
            
        def menu3positive():
            NoMenu3 = int(Itemmenu3.get())
            CostofMenu3 = NoMenu3 + 1
            Itemmenu3.set(CostofMenu3)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*40)))
            
        def menu4negative():
            NoMenu4 = int(Itemmenu4.get())
            CostofMenu4 = NoMenu4 - 1
            if(CostofMenu4 < 0):
                CostofMenu4 = 0
            else:
                Itemmenu4.set(CostofMenu4)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*460)))
            
        def menu4positive():
            NoMenu4 = int(Itemmenu4.get())
            CostofMenu4 = NoMenu4 + 1
            Itemmenu4.set(CostofMenu4)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*460)))
            
        def menu5negative():
            NoMenu5 = int(Itemmenu5.get())
            CostofMenu5 = NoMenu5 - 1
            if(CostofMenu5 < 0):
                CostofMenu5 = 0
            else:
                Itemmenu5.set(CostofMenu5)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*1000)))
            
        def menu5positive():
            NoMenu5 = int(Itemmenu5.get())
            CostofMenu5 = NoMenu5 + 1
            Itemmenu5.set(CostofMenu5)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*1000)))
            
        def menu6negative():
            NoMenu6 = int(Itemmenu6.get())
            CostofMenu6 = NoMenu6 - 1
            if(CostofMenu6 < 0):
                CostofMenu6 = 0
            else:
                Itemmenu6.set(CostofMenu6)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*60)))
            
        def menu6positive():
            NoMenu6 = int(Itemmenu6.get())
            CostofMenu6 = NoMenu6 + 1
            Itemmenu6.set(CostofMenu6)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*60)))
            
        def menu7negative():
            NoMenu7 = int(Itemmenu7.get())
            CostofMenu7 = NoMenu7 - 1
            if(CostofMenu7 < 0):
                CostofMenu7 = 0
            else:
                Itemmenu7.set(CostofMenu7)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*40)))
            
        def menu7positive():
            NoMenu7 = int(Itemmenu7.get())
            CostofMenu7 = NoMenu7 + 1
            Itemmenu7.set(CostofMenu7)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*40)))
        
        def menu8negative():
            NoMenu8 = int(Itemmenu8.get())
            CostofMenu8 = NoMenu8 - 1
            if(CostofMenu8 < 0):
                CostofMenu8 = 0
            else:
                Itemmenu8.set(CostofMenu8)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*60)))
            
        def menu8positive():
            NoMenu8 = int(Itemmenu8.get())
            CostofMenu8 = NoMenu8 + 1
            Itemmenu8.set(CostofMenu8)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*60)))
            
        def menu9negative():
            NoMenu9 = int(Itemmenu9.get())
            CostofMenu9 = NoMenu9 - 1
            if(CostofMenu9 < 0):
                CostofMenu9 = 0
            else:
                Itemmenu9.set(CostofMenu9)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*40)))
            
        def menu9positive():
            NoMenu9 = int(Itemmenu9.get())
            CostofMenu9 = NoMenu9 + 1
            Itemmenu9.set(CostofMenu9)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*40)))
            
        def menu10negative():
            NoMenu10 = int(Itemmenu10.get())
            CostofMenu10 = NoMenu10 - 1
            if(CostofMenu10 < 0):
                CostofMenu10 = 0
            else:
                Itemmenu10.set(CostofMenu10)
                if(Total_Input == ""):
                    Total_Input.set(0)
                print("Check",Total_Input.get())
                Total_Input.set(str("%.2f" %(float(Total_Input.get())-1*100)))
            
        def menu10positive():
            NoMenu10 = int(Itemmenu10.get())
            CostofMenu10 = NoMenu10 + 1
            Itemmenu10.set(CostofMenu10)
            if(Total_Input == ""):
                Total_Input.set(0)
            print("Check",Total_Input.get())
            Total_Input.set(str("%.2f" %(float(Total_Input.get())+1*100)))
            
        def cash():
            data['Total_Price'] = Total_Input.get()
            data['Car_licence'] = Car_Input.get()
            with open(str(Car_Input.get())+'.json', 'w',encoding='utf-8') as file:
                json.dump(data,file,ensure_ascii=False)
            
            
           
            ftp = FTP('192.168.1.108')
            ftp.login(user='ST03603423', passwd ='03603423')
            ftp.cwd("shopping")
            ftp.storbinary('STOR ' +str(Car_Input.get())+'.json',open(str(Car_Input.get())+'.json', 'rb'))

            ftp.retrlines('LIST')
            reset() 

            
            
        def reset():
            Itemmenu1.set("0")
            Itemmenu2.set("0")
            Itemmenu3.set("0")
            Itemmenu4.set("0")
            Itemmenu5.set("0")
            Itemmenu6.set("0")
            Itemmenu7.set("0")
            Itemmenu8.set("0")
            Itemmenu9.set("0")
            Itemmenu10.set("0")
            Total_Input.set("0.00")
            Car_Input.set("")

        def qExit():
            root.destroy()


        MainFrame = Frame(self.root)
        MainFrame.grid(padx=0,pady=0)

        MenuItemFrame = LabelFrame(MainFrame, bd=2, width=700,height=600,padx=0,pady=0,relief=RIDGE
                                   ,foreground="white",bg='black',font=('arial',12,'bold'),text="เมนู")
        MenuItemFrame.pack(side=LEFT,expand=True, fill=BOTH)

        CalFrame = LabelFrame(MainFrame, bd=2, width=300,height=600,padx=2,pady=2,relief=RIDGE
                                   ,bg='white',font=('arial',12,'bold'),text="จ่ายเงิน")
        CalFrame.pack(side=RIGHT,expand=True, fill=NONE)




        #=========================Cal==================
        self.Total = Label(font=('arial',12,'bold'),text="ราคารวม",bg='white')
        self.Total.place(x=830,y=150)
        self.txtTotal = Entry(font=('arial', 15,'bold'), bd=0,width=16,justify='left',
                                 textvariable=Total_Input,state='readonly')
        self.txtTotal.place(x=830,y=180)

        #=========================car==================
        self.Total = Label(font=('arial',12,'bold'),text="ทะเบียนรถ",bg='white')
        self.Total.place(x=830,y=220)
        self.txtTotal = Entry(font=('arial', 15,'bold'), bd=2,width=16,justify='left',
                                 textvariable=Car_Input)

        self.txtTotal.place(x=830,y=250)

        #=========================button=============
        self.ButtonFrame = Button(pady=0,bg='#FCC92A',font=('arial',15,'bold'),text="ชำระเงิน"
                                  ,width = 20,height=0,bd=0,command=cash)
        self.ButtonFrame.place(x=830,y=320)
        self.ButtonFrame = Button(pady=0,bg='#FE5E5E',font=('arial',15,'bold'),text="ลบข้อมูล"
                                  ,width = 20,height=0,bd=0,command=reset)
        self.ButtonFrame.place(x=830,y=370)
        self.ButtonFrame = Button(pady=0,bg='white',font=('arial',15,'bold'),text="EXIT"
                                  ,width = 20,height=0,bd=0,image=self.exit,command=qExit)
        self.ButtonFrame.place(x=1050,y=550)

        # =========================NameMenu=======================
        Menu1 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="ข้าวกะเพราหมูสับไข่ดาว 60 บาท")
        Menu1.grid(row=1, column=0, padx=0, pady=0)
        Menu2 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="โกโก้ 40 บาท")
        Menu2.grid(row=1, column=1, padx=0, pady=0)
        Menu3 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="ชาเย็น 40 บาท")
        Menu3.grid(row=1, column=2, padx=0, pady=0)
        Menu4 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="เนื้อ A5 460 บาท")
        Menu4.grid(row=1, column=3, padx=0, pady=0)
        Menu5 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="ต้มยำกุ้ง 1000 บาท")
        Menu5.grid(row=1, column=4, padx=0, pady=0)
        
        Menu6 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="ข้าวกะเพราเนื้อสับไข่ดาว 60 บาท")
        Menu6.grid(row=2, column=0, padx=0, pady=0)
        Menu7 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="โกโก้ 40 บาท")
        Menu7.grid(row=2, column=1, padx=0, pady=0)
        Menu8 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="ข้าวกะเพราไก่ไข่ดาว 60 บาท")
        Menu8.grid(row=2, column=2, padx=0, pady=0)
        Menu9 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="โกโก้ 40 บาท")
        Menu9.grid(row=2, column=3, padx=0, pady=0)
        Menu10 = LabelFrame(MenuItemFrame, bd=0, width=160, height=140, padx=0, pady=50, relief=SUNKEN
                           , bg='black', foreground="white", text="ข้าว 100 บาท")
        Menu10.grid(row=2, column=4, padx=0, pady=0)
        
      
        

        #=========================button,with image===============================
        self.btnMenu1 = Label(MenuItemFrame,bd=0,padx=2,image=self.menu1,width=100,height=100)
        self.btnMenu1.grid(row=1,column=0,padx=20,pady=20)
        self.btnMenu2 = Label(MenuItemFrame,bd=0,padx=2,image=self.menu2,width=100,height=100)
        self.btnMenu2.grid(row=1,column=1,padx=20,pady=20)
        self.btnMenu3 = Label(MenuItemFrame,bd=0,padx=2,image=self.menu3,width=100,height=100)
        self.btnMenu3.grid(row=1,column=2,padx=20,pady=20)
        self.btnMenu4 = Label(MenuItemFrame,bd=0,padx=2,image=self.menu4,width=100,height=100)
        self.btnMenu4.grid(row=1,column=3,padx=20,pady=20)
        self.btnMenu5 = Label(MenuItemFrame,bd=0,padx=2,image=self.menu5,width=100,height=100)
        self.btnMenu5.grid(row=1,column=4,padx=20,pady=20)
 
        #===================จำนวนอาหาร====================

        self.txtvaluemenu1 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu1,state='readonly')
        self.txtvaluemenu1.place(x=25,y=130)
        self.Buttonnegativemenu1 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu1negative)
        self.Buttonnegativemenu1.place(x=25, y=132)
        self.Buttonpositivemenu1 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu1positive)
        self.Buttonpositivemenu1.place(x=123, y=132)

        self.txtvaluemenu2 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu2)
        self.txtvaluemenu2.place(x=185,y=130)
        self.Buttonnegativemenu2 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu2negative)
        self.Buttonnegativemenu2.place(x=185, y=132)
        self.Buttonpositivemenu2 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu2positive)
        self.Buttonpositivemenu2.place(x=283, y=132)

        self.txtvaluemenu3 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu3)
        self.txtvaluemenu3.place(x=345,y=130)
        self.Buttonnegativemenu3 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu3negative)
        self.Buttonnegativemenu3.place(x=345, y=132)
        self.Buttonpositivemenu3 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu3positive)
        self.Buttonpositivemenu3.place(x=443, y=132)

        self.txtvaluemenu4 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu4)
        self.txtvaluemenu4.place(x=505,y=130)
        self.Buttonnegativemenu4 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu4negative)
        self.Buttonnegativemenu4.place(x=505, y=132)
        self.Buttonpositivemenu4 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu4positive)
        self.Buttonpositivemenu4.place(x=603, y=132)

        self.txtvaluemenu5 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu5)
        self.txtvaluemenu5.place(x=665,y=130)
        self.Buttonnegativemenu5 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu5negative)
        self.Buttonnegativemenu5.place(x=665, y=132)
        self.Buttonpositivemenu5 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu5positive)
        self.Buttonpositivemenu5.place(x=763, y=132)

        self.txtvaluemenu6 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu6)
        self.txtvaluemenu6.place(x=25,y=280)
        self.Buttonnegativemenu6 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu6negative)
        self.Buttonnegativemenu6.place(x=25, y=282)
        self.Buttonpositivemenu6 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu6positive)
        self.Buttonpositivemenu6.place(x=123, y=282)

        self.txtvaluemenu7 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu7)
        self.txtvaluemenu7.place(x=185,y=280)
        self.Buttonnegativemenu7 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu7negative)
        self.Buttonnegativemenu7.place(x=185, y=282)
        self.Buttonpositivemenu7 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu7positive)
        self.Buttonpositivemenu7.place(x=283, y=282)

        self.txtvaluemenu8 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu8)
        self.txtvaluemenu8.place(x=345,y=280)
        self.Buttonnegativemenu8 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu8negative)
        self.Buttonnegativemenu8.place(x=345, y=282)
        self.Buttonpositivemenu8 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu8positive)
        self.Buttonpositivemenu8.place(x=443, y=282)

        self.txtvaluemenu9 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu9)
        self.txtvaluemenu9.place(x=505,y=280)
        self.Buttonnegativemenu9 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu9negative)
        self.Buttonnegativemenu9.place(x=505, y=282)
        self.Buttonpositivemenu9 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu9positive)
        self.Buttonpositivemenu9.place(x=603, y=282)
        
        self.txtvaluemenu10 = Entry(bd=0,width=18,justify='center',
                                 textvariable=Itemmenu10)
        self.txtvaluemenu10.place(x=665,y=280)
        self.Buttonnegativemenu10 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.negative,command=menu10negative)
        self.Buttonnegativemenu10.place(x=665, y=282)
        self.Buttonpositivemenu10 = Button(pady=0, bg='white', font=('arial', 15, 'bold')
                                  , width=10, height=0, bd=0, image=self.positive,command=menu10positive)
        self.Buttonpositivemenu10.place(x=763, y=282)
        
if __name__ == "__main__":
    root = Tk()
    obj = pos(root)
    root.mainloop()