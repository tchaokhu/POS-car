from tkinter import *
from tkinter import ttk
import tkinter as tk
import tempfile
import os
from tkinter import messagebox
import json
import codecs
import io
import sys
from smtplib import*
from getpass import getpass
import sys
from ftplib import FTP
from ftplib import FTP
import json
from datetime import datetime, timedelta




class car:
    def __init__(self,root):
        self.root  = root
        self.root.title("CAR")
        self.root.geometry("1100x600")
        self.root.minsize(1100, 600)
        self.root.maxsize(1100, 600)
        self.root.configure(background='white')
        self.input_value = True


        global operator
        operator=""
        global discount
        discount=0
        global cash
        cash=0


        Car_Input = StringVar()
        Time_In = StringVar()
        Car_InOut = StringVar()
        Time_Out = StringVar()
        Time_Total = StringVar()
        Price = StringVar()
        #Car1 = ['กก1234',19.02,20.33,01.31,100]
        Car_inout = StringVar()
        Carinout = 0
        Car_Checkin = StringVar()
        Total_Cash = StringVar()
        Total_Discount = StringVar()
        
        carforcash = {
            "Car_licence" : "Value1",
            "Time_in" : "Value2",
            "Time_out" : "Value3",
            "Time_all" : "Value4",
            "Cash" : "0",
            "Discount":"0"
        }
        datatest = [
            {
                "Car_licence": "test555",
                "Time_in": "13.00",
                "Time_out": "16.30",
                "Time_all": "3.30",
                "Cash": "0",
                "Discount":"0"
            },
            {
                "Car_licence": "test666",
                "Time_in": "13.00",
                "Time_out": "16.30",
                "Time_all": "3.30",
                "Cash": "0",
                "Discount":"0"
            }
        ]
        datashop = {"Total_Price": "0.00", "Car_licence": "Value1"}
        result = {"จำนวนรถเข้าออก": "0", "ยอดเงินทั้งหมด": "0.00", "ยอดเงินที่ต้องเรียกเก็บจากห้าง": "0.00"}
        with open('carsave.json', 'w', encoding='utf-8') as f:
            json.dump(datatest, f, ensure_ascii=False)
            f.close()
        try:
            ftp = FTP('192.168.1.108')
            ftp.login(user = 'ST03603423',passwd='03603423')
        except:
            print("FTP Connect lost")
        def Cashcar():
            check = False
            carforcash["Car_licence"] = Car_Checkin.get()
            carforcash["Time_in"] = Time_In.get()
            datashop['Car_licence'] = Car_Checkin.get()
            print(carforcash)
            print(datashop)
            ftp.cwd('/')
            ftp.cwd('Shopping')
            carforcash_str = json.dumps(carforcash,ensure_ascii=False)
            with open('carsave.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            for datas in data:
                if datas['Car_licence'] == Car_Checkin.get():
                    datas['Car_licence'] = Car_Checkin.get()
                    datas['Time_in'] = Time_In.get()
                    check = True
            if check == False:
                data.append(carforcash)

            with open('carsave.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
                f.close()
            
            #shopping
            with open(Car_Checkin.get()+'.json', 'w', encoding='utf-8') as f:
                json.dump(datashop, f, ensure_ascii=False)
                f.close()
            ftp.storbinary('STOR '+Car_Checkin.get()+'.json', open(Car_Checkin.get()+'.json','rb'))
            ftp.cwd('/')
            
            #Car
            ftp.cwd('Car')
            ftp.storbinary('STOR '+'carsave.json', open('carsave.json','rb'))
            ftp.cwd('/')
            Car_Checkin.set("")
            Time_In.set("")
                 
        def Showcar():   
            global discount
            global cash
            Filename = Car_Input.get()+'.json'
            print(Filename)
            Shopping = 0
            try:
                ftp.cwd('/')
                ftp.cwd('Shopping')
                ftp.retrbinary('RETR '+Filename, open(Filename,'wb').write, 1024)
                ftp.cwd('/')
            except:
                print("File shopping is not found in FTP")
                
            try:
                with open(Filename, encoding='utf-8') as f:
                    json_data = f.read()
                    data = json.loads(json_data)
                    f.close()
            except:
                print("Error open file shopping")
                
            Shopping += float(data["Total_Price"])

            with open('carsave.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                f.close()
                

            #Calculate Discount
            Discount =0
            Cash =0
            for item in data:
                if Car_Input.get() == item['Car_licence']:
                    print(item['Car_licence'])
                    Time_In_str = item['Time_in']
                    Time_Out_str = Time_Out.get()
                    try:
                        Time_In_obj = datetime.strptime(Time_In_str,"%H.%M")
                        Time_Out_obj = datetime.strptime(Time_Out_str,"%H.%M")
                    except ValueError:
                        print("Error")
                        return 1
                    Time_Total = Time_Out_obj - Time_In_obj
                    minutes = Time_Total.total_seconds() // 60
                    hours = Time_Total.seconds // 3600
                    carforcash['Time_out'] = Time_Out_str
                    carforcash['Time_all'] = str(Time_Total)
                    self.txtTimeTotal.config(state="normal")
                    self.txtTimeTotal.delete(0, tk.END)
                    self.txtTimeTotal.insert(0, str(Time_Total))
                    self.txtTimeTotal.config(state="readonly")
                    
                    if Shopping > 1000:
                        if(minutes % 60 >= 30):
                              hours += 1
                        Price.set(0)
                        Cash = 0
                        Discount = str(int(hours)*30)
                    elif Shopping >= 100 and Shopping < 1000:
                        if(minutes % 60 >= 30):
                              hours += 1
                        Cash = int(hours)*30-30
                        Discount = 30
                        Price.set((int(hours)*30)-30)
                    elif Shopping >= 0 and Shopping < 100:
                        
                        if(minutes % 60 >= 30):
                            hours += 1
                        Discount = 0
                        Cash = str(int(hours)*30)
                        Price.set((int(hours)*30))   
                    carforcash['Discount'] = Discount
                    discount += int(Discount)
                    carforcash['Cash'] = Cash
                    cash += int(Cash)
                    item.update(carforcash)
   
                    
            with open('carsave.json', 'w',encoding='utf-8') as f:
                json.dump(data, f)
                print(data)
                f.close()    
            ftp.cwd('/')
            ftp.cwd('Car')
            ftp.storbinary('STOR '+'carsave.json', open('carsave.json','rb'))
            

        def Carout():
            global discount
            global cash
            ftp.cwd('/')
            ftp.cwd('Car')
            ftp.retrbinary('RETR '+'carsave.json', open('carsave.json','wb').write, 1024)
            unique_cars = set()
            total_cash = 0
            discount_cash = 0
            with open('carsave.json', encoding='utf-8') as file:
                json_data = file.read()
                f.close()
            data = json.loads(json_data)
            for car in data:
                total_cash += int(car['Cash'])
                #print(car['Discount'])
                discount_cash += int(car['Discount'])
                
                unique_cars.add(car['Car_licence'])
                
            num_unique_cars = len(unique_cars)
            #Carinout += num_unique_cars
            Car_inout.set(num_unique_cars-2)
            Total_Cash.set(cash)
            Total_Discount.set(discount)
            Car_Input.set("")
            Time_Out.set("")
            Price.set("")
            self.txtTimeTotal.config(state="normal")
            self.txtTimeTotal.delete(0, tk.END)
            self.txtTimeTotal.insert(0, "")
            self.txtTimeTotal.config(state="readonly")
            
            
        def Finish():
            num_unique_cars = 0
            smtp = open("SMTPDomain.txt")
            smtp_domain,smtp_port = smtp.read().split(";")
            smtp.close()

            try:
                #server = smtplib.SMTP('smtp.gmail.com', 587)
                server = SMTP(smtp_domain, smtp_port)
                # server.starttls()
            except :
                print("Error: unable to connect SMTP server")
                


            sender = open("SMTP_Account.txt")
            sender_email,sender_password,receiver_email = sender.read().split(";")
            sender.close()


            try:
                server.login(sender_email, sender_password)
            except:
                 print ("Error: invalid email address or password")        
                 
                    #เปลี่ยนเปนแจงขอความแลวออกจากโปรแกรม
            else:
                print("SMTP Connected")


            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = "ข้อมูลการปิดยอดประจำวัน"

            import json 
            with open('carsave.json', encoding='utf-8') as file:
                json_data = file.read()

            data = json.loads(json_data)
            unique_cars = set()
            total_cash = 0
            discount_cash = 0
            for car in data:
                total_cash += int(car['Cash'])
                discount_cash += int(car['Discount'])
                unique_cars.add(car['Car_licence'])

            num_unique_cars = len(unique_cars)


            body = "จำนวนรถเข้า-ออกทั้งหมด : "+str(len(unique_cars)-2)+"\n"
            body+= "ยอดเงินทั้งหมด : " + str(total_cash)+"\n"
            body+= "ยอดเงินที่ต้องเรียกเก็บจากห้าง : " + str(discount_cash)

            msg.attach(MIMEText(body,'plain'))
            try:
                server.sendmail(sender_email,receiver_email,msg.as_string())
            except:
                print("send data fail")
            else:
                Car_inout.set("")
                Total_Cash.set("")
                Total_Discount.set("")
                with open('carsave.json', 'w', encoding='utf-8') as f:
                    json.dump(datatest, f, ensure_ascii=False)
                    f.close()
                ftp.cwd('/')
                ftp.cwd('Car')
                ftp.storbinary('STOR '+'carsave.json', open('carsave.json','rb'))
                ftp.cwd('/')
                #ftp.close()
                server.quit()
                print("Success")
            




        CalFrame = LabelFrame(bd=2, width=500,height=490,padx=7,pady=2,relief=RIDGE
                                   ,bg='#393E46',font=('arial',12,'bold'),text="")
        CalFrame.place(x=650,y=130)
        CarIn = LabelFrame(bd=2, width=1100,height=140,padx=7,pady=2,relief=RIDGE
                                   ,bg='#000',font=('arial',12,'bold'),text="")
        CarIn.place(x=0,y=0)

        self.Car_Input = Label(font=('arial',20,'bold'),text="เลขทะเบียน",bg='gray')
        self.Car_Input.place(x=60,y=160)
        self.txtCar_Input = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Car_Input)
        self.txtCar_Input.place(x=205,y=160)


        self.TimeOut = Label(font=('arial',20,'bold'),text="เวลาออก",bg='white')
        self.TimeOut.place(x=60,y=230)
        self.txtTimeOut = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Time_Out)
        self.txtTimeOut.place(x=205,y=230)

        self.TimeTotal = Label(font=('arial',20,'bold'),text="เวลาจอดทั้งหมด",bg='white')
        self.TimeTotal.place(x=60,y=300)
        self.txtTimeTotal = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Time_Total,state='readonly')
        self.txtTimeTotal.place(x=265,y=300)

        self.Price = Label(font=('arial',20,'bold'),text="ค่าบริการ",bg='white')
        self.Price.place(x=60,y=370)
        self.txtPrice = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Price,state='readonly')
        self.txtPrice.place(x=205,y=370)

        self.ButtonFrame = Button(pady=0,bg='#FFD369',font=('arial',15,'bold'),text="ยืนยัน"
                                  ,width = 10,height=0,bd=0,command=Showcar)
        self.ButtonFrame.place(x=500,y=155)

        self.ButtonFrame = Button(pady=0,bg='#FFD329',font=('arial',15,'bold'),text="รถออก"
                                  ,width = 30,height=0,bd=0,command=Carout)
        self.ButtonFrame.place(x=170,y=525)





        self.Car_Input = Label(font=('arial', 20, 'bold'), text="เลขทะเบียน", foreground="white", bg='#000')
        self.Car_Input.place(x=260, y=20)
        self.txtCar_Input = Entry(font=('arial', 15, 'bold'), bd=2, width=20, justify='left',
                                  textvariable=Car_Checkin)
        self.txtCar_Input.place(x=405, y=20)

        self.TimeIn = Label(font=('arial',20,'bold'),text="เวลาเข้า", foreground="white",bg='#000')
        self.TimeIn.place(x=260,y=70)
        self.txtTimeIn = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Time_In)
        self.txtTimeIn.place(x=405,y=70)

        self.ButtonFrame = Button(pady=0, bg='#FFD369', font=('arial', 15, 'bold'), text="รถเข้า"
                                  , width=10, height=0, bd=0, command=Cashcar)
        self.ButtonFrame.place(x=670, y=45)




        self.Car_inout = Label(font=('arial',15,'bold'),text="จำนวนรถเข้าออก",foreground="white",bg='#393E46')
        self.Car_inout.place(x=670,y=230)
        self.txtCar_inout = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Car_inout,state='readonly')
        self.txtCar_inout.place(x=850,y=230)

        self.Total_Cash = Label(font=('arial',15,'bold'),text="ยอดเงินทั้งหมด",foreground="white",bg='#393E46')
        self.Total_Cash.place(x=670,y=300)
        self.txtTotal_Cash = Entry(font=('arial', 15,'bold'), bd=2,width=20,justify='left',
                                 textvariable=Total_Cash,state='readonly')
        self.txtTotal_Cash.place(x=850,y=300)
           
        self.Total_Discount = Label(font=('arial',15,'bold'),text="ยอดเงินเรียกเก็บจากห้าง",foreground="white",bg='#393E46')
        self.Total_Discount.place(x=670,y=370)
        self.txtTotal_Discount = Entry(font=('arial', 15,'bold'), bd=2,width=17,justify='left',
                                 textvariable=Total_Discount,state='readonly')
        self.txtTotal_Discount.place(x=883,y=370)

        self.ButtonFrame = Button(pady=0,bg='#EEEEEE',font=('arial',15,'bold'),text="ปิดยอด"
                                  ,width = 30,height=0,bd=0,command=Finish)
        self.ButtonFrame.place(x=700,y=525)

if __name__ == '__main__':
    root = Tk()
    application = car(root)
    root.mainloop()