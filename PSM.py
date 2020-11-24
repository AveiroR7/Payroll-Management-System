from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Payroll Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
#Bottoms = Frame(root,width=600, relief = SUNKEN)
#Bottoms.pack(side=BOTTOM)
f1=Frame(root,width=800,height=200,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=300,bd=8,relief="raise")
f2.pack(side=RIGHT)

##f3 =Frame(root,width=500, height=600, bd=8, relief = SUNKEN)
##f3.pack(side=TOP)
#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',30,'bold'),text="Payroll Management System",fg="Black",bd=8,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=8,anchor='w')
lblInfo.grid(row=1,column=0)

def iExit():
     qExit = messagebox.askyesno("Payroll System", "Do You want to exit the system")
     if qExit > 0:
          root.destroy()
          return

def Reset():
     Name.set("")
     Address.set("")
     HoursWorked.set("")
     wageshour.set("")
     Payable.set("")
     Taxable.set("")
     NetPayable.set("")
     overtimehours.set("")
     Employe.set("")
     NINumber.set("")
     GrossPayable.set("")
     txtPaySlip.delete("1.0",END)


def EnterInfo():
     txtPaySlip.insert(END, "\t\tPay Slip\n\n")
     txtPaySlip.insert(END, "Name\t\tP" + Name.get() + "\n\n")
     txtPaySlip.insert(END, "Address\t\t" + Address.get() + "\n\n")
     txtPaySlip.insert(END, "NI Number\t\t" + NINumber.get() + "\n\n")
     txtPaySlip.insert(END, "Hours Worked\t\t" + HoursWorked.get() + "\n\n")
     txtPaySlip.insert(END, "Net Payable\t\t" + NetPayable.get() + "\n\n")
     txtPaySlip.insert(END, "Wages Per Hour\t\t" + wageshour.get() + "\n\n")
     txtPaySlip.insert(END, "Tax Paid\t\t" + Taxable.get() + "\n\n")
     txtPaySlip.insert(END, "Payable\t\t" + Payable.get() + "\n\n")
     
def WeeklyWages():
     HoursWorkedPerWeek = float(HoursWorked.get())
     WagesPerHour = float(wageshour.get())

     paydue =   WagesPerHour * HoursWorkedPerWeek
     PayamentDue = "RS." , str('%.2f'%(paydue))
     Payable.set(PaymentDue)

     tax = paydue *0.2
     Taxable = "RS.",str('%.2f'%(tax))
     Taxable.set(Taxable)

     netpay = paydue - tax
     NetPays = "RS." ,str('%.2f'%(netpay))
     NetPayable.set(NetPays)

     if(HoursWorkedPerWeek > 40):
          OverTimeHours = (HoursWorkedPerWeek - 40) + WagesPerHour * 1.5
          Overtimehrs = "RS." ,str('%.2f'%(overTimeHours))
          OverTimeHours.set(Overtimehrs)

     elif HoursWorkedPerWeek <= 40:
          overTimeHours = (HoursWorkedPerWeek - 40) + WagesPerHour * 1.5
          Overtimehrs = "RS." ,str('%.2f'%(overtimepay))
          OverTimeHours.set(Overtimehrs)
          return
    
#====================================psm Info 1===========================================================
#**********************************Varables*********************
Name = StringVar()
Address = StringVar()
Employe = StringVar()
NINumber = StringVar()
wageshour = StringVar()
HoursWorked = StringVar()
Payable = StringVar()
Taxable = StringVar()
NetPayable = StringVar()
GrossPayable = StringVar()
OverTime = StringVar()
TimeOfOrder =  StringVar()
DateOfOrder = StringVar()

#********************************label**********************
lblName = Label(f1, text="NAME", font=('arial',14,'bold'), bd =10).grid(row=0,column=0)
lblAddress = Label(f1, text="ADDRESS", font=('arial',14,'bold'), bd =10).grid(row=0,column=2)
lblEmploye = Label(f1, text="Employe", font=('arial',14,'bold'), bd =10).grid(row=1,column=0)
lblNINumber = Label(f1, text="ID", font=('arial',14,'bold'), bd=10).grid(row=1,column=2)
lblHoursworked = Label(f1, text="Hours Worked", font=('arial',14,'bold'), bd=10).grid(row=2,column=0)
lblhourlyRate = Label(f1, text="Hourly Rate", font=('arial',14,'bold'), bd=10).grid(row=2,column=2)
lblOverTime = Label(f1, text="Over Time", font=('arial',14,'bold'), bd=10).grid(row=3,column=0)
lblTax= Label(f1, text="TAX", font=('arial',14,'bold'), bd=10).grid(row=3,column=2)
lblGrossPay = Label(f1, text="Gross Pay", font=('arial',14,'bold'), bd=10).grid(row=4,column=0)
lblNetpay = Label(f1, text="Net Pay", font=('arial',14,'bold'), bd=10).grid(row=4,column=2)

#***************************Entry*************************
etxtName = Entry(f1,textvariable=Name, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtName.grid(row=0,column=1)
etxtAddress = Entry(f1,textvariable=Address, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtAddress.grid(row=0,column=3)
etxtEmploye = Entry(f1,textvariable=Employe, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtEmploye.grid(row=1,column=1)
etxtHoursWorked = Entry(f1,textvariable=HoursWorked, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtHoursWorked.grid(row=2,column=1)
etxtWagesPerHour = Entry(f1,textvariable=wageshour, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtWagesPerHour.grid(row=2,column=3)
etxtninoW = Entry(f1,textvariable=NINumber, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtninoW.grid(row=1,column=3)
etxtGrossPay = Entry(f1,textvariable=Payable, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtGrossPay.grid(row=4,column=1)
etxtNetPay = Entry(f1,textvariable=NetPayable, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtNetPay.grid(row=4,column=3)
etxtTax = Entry(f1,textvariable=Taxable, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtTax.grid(row=3,column=1)
etxtovertime = Entry(f1,textvariable=OverTime, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtovertime.grid(row=3,column=3)
#============================================================================================================
#                                 INFO 2
#========================================================================================


lblPaySlip=Label(f2,font=('arial',20,'bold'),text = "Payslip").grid(row=0,column=0)
txtPaySlip=Text(f2, height = 22, width = 34, bd=14,font=('arial',12,'bold'))
txtPaySlip.grid(row=0,column=0)

#==========================================Buttons==========================================================================================
btnSalary = Button(f1,text='Weekly Salary',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1, command = WeeklyWages).grid(row=5,column=0)

btnReset = Button(f1,text='RESET',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1,command=Reset).grid(row=5,column=1)

btnPaySlip = Button(f1,text='Pay Slip',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1,command = EnterInfo).grid(row=5,column=2)

btnExit = Button(f1,text='Eixt System',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1, command = iExit).grid(row=5,column=3)

root.mainloop()


