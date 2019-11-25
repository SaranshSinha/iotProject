import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sqlite3
from datetime import date
import datetime
from tkinter import *
from tkinter import ttk

global Ecat,Icat,wday
Ecat=["Entertainment","Utility","Education","Others"]
Icat=["Salary","Bonus","Gift Income","Pension"]
count=[0,0,0,0]
global uname
uname="rounak"
def daily_summary():
	daily_sum=Frame(dashboard,width=100,height=100)
	Label(daily_sum,text="Here is your daily summary!",anchor=W,justify=LEFT).pack()
	#data retrival
	dt=[]
	for i in range(7):
		d=str(tdate-i)+today1[2:]
		dt.append(d)
	dt.reverse()
	print()
	print(dt)
	val=[]
	for i in range(7):
		cursor = conn.execute("SELECT sum(amount) FROM Expense where type = \"expense\" and edate='%s'"%(dt[i]))
		row=cursor.fetchone()
		print(row)
		if(row[0]==None):
			val.append(0)
		else:
			val.append(int(row[0]))
	#graph
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	ind = numpy.arange(7)  # the x locations for the groups
	width = .5
	for i in range(7):
		dt[i]=dt[i][:5]
	rects1 = ax.bar(ind,val, width,tick_label = dt,color = ['red', 'green','blue','black'])
	ax.set_xlabel('Date') 
	ax.set_ylabel('Expense') 
	ax.set_title('Daily Expense')
	canvas = FigureCanvasTkAgg(f, master=daily_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	#
	daily_sum.grid(row=0,column=0)

def budget_summary():
	bud_sum=Frame(dashboard)
	Label(bud_sum,text="Here is your budget summary!").pack()
	#<data retrival>
	cursor=conn.execute("SELECT amount,tag from Expense where type=\"expense\" and eDate Between '%s' and '%s'"%(startdate,today1))
	rows=cursor.fetchall()
	for row in rows:
		print(row)
		for i in range(len(Ecat)):
			if(row[1].lower()==Ecat[i].lower()):
				count[i]+=row[0]
				break
	print()
	print(count)
	value=[]
	tag=[]
	for i in range(len(Ecat)):
		if(count[i]!=0):
			value.append(count[i])
			tag.append(Ecat[i])
	#
	print()
	print(value)
	print()
	print(tag)
	#<graph>
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	rects1 = ax.pie(value,labels=tag)
	ax.set_title('Daily Expense')
	canvas = FigureCanvasTkAgg(f, master=bud_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	#
	bud_sum.grid(row=1,column=0)

def earning_summary():
	ear_sum=Frame(dashboard)
	Label(ear_sum,text="Here is your earning summary!").pack()
	#
	inc=[0,0,0,0]
	exp=[0,0,0,0]
	for i in range(4):
		cursor=conn.execute("SELECT type,amount from Expense where eDate Between '%s' and '%s'"%(mon[i],endmon[i]))
		rows=cursor.fetchall()
		for row in rows:
			if(row[0].lower()=="expense"):
				exp[i]+=row[1]
			elif(row[0].lower()=="income"):
				inc[i]+=row[1]
	#
	l=[]
	for x in mon:
		l.append(x[3:5]+"/"+x[-2:])
	#graph
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	ind = numpy.arange(4)  # the x locations for the groups
	width = .25
	rects1 = ax.bar(ind,exp, width,tick_label = l,color = ['red'])
	rects1 = ax.bar(ind+width,inc, width,tick_label =l,color = ['green'])
	ax.set_xlabel('Months') 
	ax.set_ylabel('Amount') 
	ax.set_title('Net Earning')
	canvas = FigureCanvasTkAgg(f, master=ear_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	#
	ear_sum.grid(row=2,column=0)

def add_to_database():
	try:
		conn.execute("INSERT into Expense(user,item,tag,type,amount,edate) VALUES ('%s','%s','%s','%s','%s','%s');"%(uname,name,tg,typ,amt,today1))
		Label(tran_win,text="Transaction Added", fg="green", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)
	except:
		Label(tran_win,text="Transaction Failed!! Try Again", fg="red", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)
	#add some timer to remove this or close TLW


def transaction():
	global tran_win
	tran_win = Toplevel(dashboard)
	tran_win.title("Add a transaction")
	tran_win.geometry("400x200")
	Label(tran_win,text="Add your transaction : ").grid(row=0,column=0,sticky = W, pady = 2)
	v = StringVar()
	v.set(1)
	def event():
		if v.get()=="1":
			nl.config(text="Name of Expense : ")
			radio1.config(text="Entertainment")
			radio2.config(text="Utilities")
			radio3.config(text="Education")
			radio4.config(text="Others")
			radioVar.set(0)
			typ='expense'
		else:
			nl.config(text="Name of Income : ")
			radio1.config(text="Salary")
			radio2.config(text="Bonus")
			radio3.config(text="Gift Income")
			radio4.config(text="Pension")
			radioVar.set(0)
			typ='income'
	def update():
		if(value==1):
			tg=radio1.cget("text")
		if(value==2):
			tg=radio2.cget("text")
		if(value==3):
			tg=radio3.cget("text")
		if(value==4):
			tg=radio4.cget("text")
	Radiobutton(tran_win,text="Expense",variable=v,value =1,command=event).grid(row=2,column=0,sticky = W, pady = 2)
	Radiobutton(tran_win,text="Income",variable=v,value =2,command=event).grid(row=2,column=3,sticky = W, pady = 2)
	global typ
	nl=Label(tran_win,text="Name of Expense : ")
	nl.grid(row=3,column=0,sticky = W, pady = 2)
	global name
	name=Entry(tran_win).grid(row=3,column=3,sticky = W, pady = 2)
	Label(tran_win,text="Amount : ").grid(row=4,column=0,sticky = W, pady = 2)
	global amt
	amt=Entry(tran_win).grid(row=4,column=3,sticky = W, pady = 2)
	#take date time from system
	global tg
	Label(tran_win,text="Tags : ").grid(row=5,column=0,sticky = W, pady = 2)
	radioVar = BooleanVar()
	radioVar.set(0)
	radio1 = Radiobutton(tran_win,text = "Entertainment", variable=radioVar,command=update,value=1)
	radio1.grid(row = 5, column = 3, sticky = W,padx=2,pady=2)
	radio2 = Radiobutton(tran_win,text = "Utilities", variable=radioVar,command=update,value=2)
	radio2.grid(row = 5, column = 5, sticky = W,padx=2,pady=2)
	radio3 = Radiobutton(tran_win,text = "Education", variable=radioVar,command=update,value=3)
	radio3.grid(row = 6, column = 3, sticky = W,padx=2,pady=2)
	radio4 = Radiobutton(tran_win,text = "Others", variable = radioVar,command=update,value=4)
	radio4.grid(row = 6, column = 5, sticky = W,padx=2,pady=2)
	add=ttk.Button(tran_win, text="Add", width=10)
	add.grid(row=7,column=3,sticky = W, pady = 2)

def add_transaction():
	add_tran=Frame(dashboard)
	add=Button(add_tran, text="Add a transaction", width=20, command = transaction,activebackground='green',activeforeground='black',anchor=N).pack()
	add_tran.grid(row=4,column=0)


global dashboard
dashboard = Tk()
dashboard.title("Dashboard")
#
today=str(date.today()).replace("-","/")	#today's date in string format	output : 'yyyy/mm/dd'
tdate=int(today[-2:])	#today's date like 08
today1=today.split("/")
today1.reverse()
today1="/".join(today1)		#format : 'dd/mm/yyyy'
#day=datetime.datetime.strptime(date, '%d %m %Y').weekday()	#day of week
startdate='01'+today1[2:]	#start date of current month
m=int(today1[3:5])	#month no
mon=[]
endmon=[]
mon.append(startdate)
'''if(m<=10):
	for i in range(3):
		if(m-i-1<1):
			mon.append('01/'+str((m-i-1)%12 if (m-i-1)%12!=0 else 12)+"/"+str(int(today1[-4:])-1))
		else:
			mon.append('01/0'+str(m-i-1)+today1[-5:])
'''
temp=m
for i in range(3):
	if(temp<=10):
		if(m-i-1<1):
			mon.append('01/'+str((m-i-1)%12 if (m-i-1)%12!=0 else 12)+"/"+str(int(today1[-4:])-1))
		else:
			mon.append('01/0'+str(m-i-1)+today1[-5:])
		temp-=1
	else:
		mon.append('01/'+str(m-i-1)+today1[-5:])
		temp-=1
#
for x in mon:
	endmon.append('31'+x[2:])
mon.reverse()
endmon.reverse()
endmon.pop()
endmon.append(today1)
print(mon)
print()
print(endmon)    
#
conn=sqlite3.connect("ExpenseTracker2.db")
#daily_summary()
#budget_summary()
earning_summary()
add_transaction()
dashboard.mainloop()