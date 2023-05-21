from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("ร้านอาหารตณะวิศวกรรม ศรีราชา")

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# ====================Time===================
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font=('TH Sarabun New', 50, 'bold'), text='ร้านอาหารคณะวิศวกรรม ศรีราชา', fg="blue", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('TH Sarabun New', 20, 'bold'), text=localtime, fg="blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

# ===================Define Variable & function============
text_Input = StringVar()
operator = ""
rand = StringVar()
MenuPrice = [40, 45, 40, 40, 50]
DrinkPrice = [50]
Menu1 = StringVar()
Menu2 = StringVar()
Menu3 = StringVar()
Menu4 = StringVar()
Menu5 = StringVar()
Drink = StringVar()
Total = StringVar()
Service = StringVar()
Totalservice = StringVar()
Tax = StringVar()
Totaltax = StringVar()
Menu1.set(0)

def btnClick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)


def btnEqualInput():
    global operator
    operator = str(eval(operator))
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set(operator)


def TotalCal():
    NoMenu1 = float(Menu1.get())
    NoMenu2 = float(Menu2.get())
    NoMenu3 = float(Menu3.get())
    NoMenu4 = float(Menu4.get())
    NoMenu5 = float(Menu5.get())
    NoDrink = float(Drink.get())

    CostofMenu1 = NoMenu1 * MenuPrice[0]
    CostofMenu2 = NoMenu2 * MenuPrice[1]
    CostofMenu3 = NoMenu3 * MenuPrice[2]
    CostofMenu4 = NoMenu4 * MenuPrice[3]
    CostofMenu5 = NoMenu5 * MenuPrice[4]
    CostofDrink = NoDrink * DrinkPrice[0]

    SubtotalC1 = CostofMenu1 + CostofMenu2 + CostofMenu3 + CostofMenu4 + CostofMenu5 + CostofDrink
    Service_chargeC = SubtotalC1 * 0.1
    SubtotalC2 = SubtotalC1 + Service_chargeC
    PayTax = SubtotalC2 * 0.07
    TotalCostC = SubtotalC2 + PayTax

    Total.set(SubtotalC1)
    Service.set(Service_chargeC)
    Totalservice.set(SubtotalC2)
    Tax.set(PayTax)
    Totaltax.set(TotalCostC)


def Reset():
    Menu1.set("")
    Menu2.set("")
    Menu3.set("")
    Menu4.set("")
    Menu5.set("")
    Drink.set("")
    Total.set("")
    Service.set("")
    Totalservice.set("")
    Tax.set("")
    Totaltax.set("")


def qExit():
    root.destroy()


# ==================Caculator  frame==============
txtDisplay = Entry(f2, font=('TH Sarabun New', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, fg='black',
                   justify='right')
txtDisplay.grid(columnspan=4)

# ==================Row 1=================
btn7 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='7', bg='powder blue',
              command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='8', bg='powder blue',
              command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='9', bg='powder blue',
              command=lambda: btnClick(9)).grid(row=2, column=2)
btnAdd = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='+', bg='powder blue',
                command=lambda: btnClick("+")).grid(row=2, column=3)
# ==================Row 2=================
btn4 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='4', bg='powder blue',
              command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='5', bg='powder blue',
              command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='6', bg='powder blue',
              command=lambda: btnClick(6)).grid(row=3, column=2)
btnMinus = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='-',
                  bg='powder blue',
                  command=lambda: btnClick("-")).grid(row=3, column=3)
# ==================Row 3=================
btn1 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='1', bg='powder blue',
              command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='2', bg='powder blue',
              command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='3', bg='powder blue',
              command=lambda: btnClick(3)).grid(row=4, column=2)
btnMultiply = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='*',
                     bg='powder blue',
                     command=lambda: btnClick("*")).grid(row=4, column=3)
# ==================Row 4=================
btn0 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='0', bg='powder blue',
              command=lambda: btnClick(0)).grid(row=5, column=0)
btnC = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='C', bg='powder blue',
              command=lambda: btnClearDisplay()).grid(row=5, column=1)
btn = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='=', bg='powder blue',
             command=lambda: btnEqualInput()).grid(row=5, column=2)
btnDivide = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('TH Sarabun New', 20, 'bold'), text='/',
                   bg='powder blue',
                   command=lambda: btnClick("/")).grid(row=5, column=3)

# =========================Resturant Info1
lblRef = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='Reference', fg="blue", bd=10, anchor='w')
lblRef.grid(row=0, column=0)
txtRef = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=rand, bd=10, insertwidth=4, fg='black',
               justify='right', bg='powder blue')
txtRef.grid(row=0, column=1)

lblMenu1 = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='ผัดกะเพราราดข้าว *' + str(MenuPrice[0]), fg="blue",
                 bd=10, anchor='w')
lblMenu1.grid(row=1, column=0)
txtMenu1 = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Menu1, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtMenu1.grid(row=1, column=1)

lblMenu2 = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='ราดหน้า *' + str(MenuPrice[1]), fg="blue", bd=10,
                 anchor='w')
lblMenu2.grid(row=2, column=0)
txtMenu2 = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Menu2, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtMenu2.grid(row=2, column=1)

lblMenu3 = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='ข้าวผัด  *' + str(MenuPrice[2]), fg="blue", bd=10,
                 anchor='w')
lblMenu3.grid(row=3, column=0)
txtMenu3 = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Menu3, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtMenu3.grid(row=3, column=1)

lblMenu4 = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='ผัดพริกแกงราดข้าว *' + str(MenuPrice[3]), fg="blue",
                 bd=10, anchor='w')
lblMenu4.grid(row=4, column=0)
txtMenu4 = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Menu4, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtMenu4.grid(row=4, column=1)

lblMenu5 = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='สุกี้ยากี้ทะเล *' + str(MenuPrice[4]), fg="blue", bd=10,
                 anchor='w')
lblMenu5.grid(row=5, column=0)
txtMenu5 = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Menu5, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtMenu5.grid(row=5, column=1)

lblDrink = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='เครื่องดื่ม *' + str(DrinkPrice[0]), fg="blue", bd=10,
                 anchor='w')
lblDrink.grid(row=0, column=2)
txtDrink = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Drink, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtDrink.grid(row=0, column=3)

lblTotal = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='จำนวนเงิน', fg="blue", bd=10, anchor='w')
lblTotal.grid(row=1, column=2)
txtTotal = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Total, bd=10, insertwidth=4, fg='black',
                 justify='right', bg='powder blue')
txtTotal.grid(row=1, column=3)

lblService = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='ค่าบริการ', fg="blue", bd=10, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Service, bd=10, insertwidth=4, fg='black',
                   justify='right', bg='powder blue')
txtService.grid(row=2, column=3)

lblTotalservice = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='จำนวนเงินรวม', fg="blue", bd=10, anchor='w')
lblTotalservice.grid(row=3, column=2)
txtTotalservice = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Totalservice, bd=10, insertwidth=4,
                        fg='black', justify='right', bg='powder blue')
txtTotalservice.grid(row=3, column=3)

lblTax = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='ภาษี', fg="blue", bd=10, anchor='w')
lblTax.grid(row=4, column=2)
txtTax = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Tax, bd=10, insertwidth=4, fg='black',
               justify='right', bg='powder blue')
txtTax.grid(row=4, column=3)

lblTotaltax = Label(f1, font=('TH Sarabun New', 18, 'bold'), text='จำนวนเงินรวมภาษี', fg="blue", bd=10, anchor='w')
lblTotaltax.grid(row=5, column=2)
txtTotaltax = Entry(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=Totaltax, bd=10, insertwidth=4, fg='black',
                    justify='right', bg='powder blue')
txtTotaltax.grid(row=5, column=3)

TotalBotton = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('TH Sarabun New', 20, 'bold'), text='Total',
                     bg='powder blue', command=TotalCal)
TotalBotton.grid(row=6, column=1)

ResetBotton = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('TH Sarabun New', 20, 'bold'), text='Reset',
                     bg='powder blue', command=Reset)
ResetBotton.grid(row=6, column=2)

ExitBotton = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('TH Sarabun New', 20, 'bold'), text='Exit',
                    bg='powder blue', command=qExit)
ExitBotton.grid(row=6, column=3)

root.mainloop()