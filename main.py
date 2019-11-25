from tkinter import *
from tkcalendar import *
import sqlite3

root =Tk()
root.geometry("600x600")

rootWidth = root.winfo_screenwidth()
conn=sqlite3.connect("ExpenseTracker.db")

def populateTransaction(frame):
    Label(frame, text = "Your Transactions", width= rootWidth, height = 3, anchor=CENTER, bg='blue4',fg='gold',bd=4,font=('Algerian','13','bold')).pack()
    searchFrame = Frame(frame, padx = 10, pady=10)
    searchFrame.pack(fill=BOTH, expand = True)
    searchFrame.grid_columnconfigure(0, weight=1)
    searchFrame.grid_columnconfigure(1, weight=1)
    searchFrame.grid_columnconfigure(2, weight=1)
    searchFrame.grid_columnconfigure(3, weight=1)
    Label(searchFrame, text = "From",font=('Lucida Console','12','bold'),bg='purple',fg='white',width=10).grid(row = 0, column = 1)
    startDate_E = DateEntry(searchFrame, width=20, bd=3,date_pattern='dd/mm/yyyy')
    startDate_E.grid(row=0, column=2, pady=5)
    Label(searchFrame, text = "To",font=('Lucida Console','12','bold'),bg='purple',width=10,fg='white').grid(row = 1, column = 1)
    endDate_E = DateEntry(searchFrame, width=20,bd=3,date_pattern='dd/mm/yyyy')
    endDate_E.grid(row=1, column=2,pady=5)
    
    
    def search():
        for widget in dataFrame.winfo_children():
            widget.destroy()
        a = startDate_E.get()
        b = endDate_E.get()

        cursor = conn.execute("SELECT * FROM Expense where edate >= '%s' and edate <= '%s'"%(a,b))
        #cursor = conn.execute("SELECT * FROM Expense where edate='22/11/2019' or edate='20/11/2019' or edate='21/11/2019' or edate='01/11/2019'")
        i = 0
        for r in cursor:
            if r[3] == 'expense':
                Label(dataFrame, text="%s"%(r[5]), width=20,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=0)
                Label(dataFrame, text = "%s - (%s) :"%(r[1],r[2]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=1)
                Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='red',relief='solid',pady=3).grid(row=i,column=2)
                i+=1
            else:
                Label(dataFrame, text="%s"%(r[5]), width=20,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i,column=0)
                Label(dataFrame, text = "%s - (%s) :"%(r[1],r[2]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i,column=1)
                Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='green',relief='solid',pady=3).grid(row=i,column=2)
                i+=1
        #Label(dataFrame, text = "%s - (%s) :"%(a,b),width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i+1,column=0)
   
    Button(searchFrame, text="Search", width=10, command = search, bg = 'gold', activebackground='green2',font=('Brush Script MT','18')).grid(row = 2, column = 2,pady=10)
    dataFrame = Frame(frame, padx = 10, pady=10)
    dataFrame.pack(fill = BOTH, expand = True)
    dataFrame.grid_columnconfigure(0, weight=1)
    dataFrame.grid_columnconfigure(1, weight=2)
    dataFrame.grid_columnconfigure(2, weight=2)
 
    #database 
    
    cursor=conn.execute("SELECT * FROM Expense WHERE edate='22/11/2019' and type='expense'")
    i = 0
    for r in cursor:
        Label(dataFrame, text="%s"%(r[5]), width=20,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=0)
        Label(dataFrame, text = "%s - (%s) :"%(r[1],r[2]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=1)
        Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='red',relief='solid',pady=3).grid(row=i,column=2)
        i+=1

    
def populateHome(frame):
    for row in range(100):
        Label(frame, text="%s" % row, width=3, borderwidth="1", 
                 relief="solid", bg ='blue').grid(row=row, column=0)
        t="this is the second column for row %s" %row
        Label(frame, text=t).grid(row=row, column=1)

def populateItemTracker(frame):
    Label(frame, text = "This Month", width= rootWidth, height = 3, anchor=CENTER, bg='deep sky blue',bd=4).pack()
    
    scaleFrame = Frame(frame)
    scaleFrame.pack(fill=BOTH, expand = True)
    scaleFrame.grid_columnconfigure(0, weight = 1)
    scaleFrame.grid_columnconfigure(1, weight = 1)
    
    #database
    cursor = conn.execute("SELECT * FROM Expense WHERE lim != 0")
    i=0
    for r in cursor:
        Label(scaleFrame, text='%s'%r[1], pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='MediumOrchid1').grid(row=i,column=0)
        s = Scale(scaleFrame, orient = HORIZONTAL, length = 300, from_=1, to=100, fg = 'brown4', troughcolor = 'salmon1',bg='khaki1')
        s.grid(row=i, column=1)
        a = (r[4]/r[6])*100
        s.set(a)
        #s.set(50/2)
        i+=1
    # 
    # for i in range(50):
    #         Label(scaleFrame, text = "hello",width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i,column=0)
    #         Label(scaleFrame, text = "world", width = 50,height=3, borderwidth = '1',bg='green',relief='solid',pady=3).grid(row=i,column=1)
    #         i+=1       
    def setBudget():
        top = Toplevel()
        top.title('Set item Budget')
        top.grid_columnconfigure(0, weight = 1)
        top.grid_columnconfigure(1, weight = 2)
        top.grid_columnconfigure(2, weight = 2)
        top.grid_columnconfigure(3, weight = 1)
        Label(top, text = 'Enter item', pady = 5, padx = 5).grid(row = 0, column = 1)
        Entry(top, width = 30).grid(row = 0, column = 2)
        Label(top, text = 'Set Budget', pady = 5, padx = 5).grid(row = 1, column = 1)
        Entry(top, width = 30).grid(row = 1, column = 2)
        def change():
            top.destroy()
        Button(top, text = 'SET', command = change, width = 10, height =1, bd = 2, fg = 'blue',pady = 4).grid(row = 2, column = 2)
        top.minsize(400, 150)
        top.mainloop()

    Button(scaleFrame, text = 'Set item Budget', command = setBudget, fg = 'blue', bg = 'yellow', width = 20, height = 2, relief='solid').grid(row =i+1, column = 0)

def populateTagSummary(frame):
    Label(frame, text = "This Month's Expense", width= rootWidth, height = 3, anchor=CENTER, bg='deep sky blue',bd=4, pady=5).pack()
    expenseFrame = Frame(frame, padx = 10, pady=10)
    expenseFrame.pack(fill = BOTH, expand = True)
    expenseFrame.grid_columnconfigure(0, weight=1)
    expenseFrame.grid_columnconfigure(1, weight=1)
    Label(expenseFrame, text = 'Expense',bg='orange red', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid').grid(row=0, column = 0)
    Label(expenseFrame, text = 'Rs 4000',bg='orange red', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid').grid(row=0, column = 1)

    #database
    i=1
    cursor = conn.execute("SELECT * FROM Expense WHERE type='expense'")
    for r in cursor:
        Label(expenseFrame, text = "%s"%r[2],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='firebrick1').grid(row=i,column=0)
        Label(expenseFrame, text = "%s"%r[4],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='firebrick1').grid(row=i,column=1)
        i+=1
    
    
    Label(expenseFrame, text = 'Income', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='green2').grid(row=i, column = 0)
    Label(expenseFrame, text = 'Rs 14000', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='green2').grid(row=i, column = 1)
    i+=1

    cursor = conn.execute("SELECT * FROM Expense WHERE type='income'")

    for r in cursor:
        Label(expenseFrame, text = "%s"%r[2],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='SpringGreen2').grid(row=i,column=0)
        Label(expenseFrame, text = "%s"%r[4],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='SpringGreen2').grid(row=i,column=1)
        i+=1

    # for i in range(50):
    #     Label(expenseFrame, text = "hello",width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i,column=0)
    #     Label(expenseFrame, text = "world", width = 50,height=3, borderwidth = '1',bg='green',relief='solid',pady=3).grid(row=i,column=1)
    #     i+=1

def transactionHelper():
    home.grid_forget()
    itemTracker.grid_forget()
    tagSummary.grid_forget()
    # transaction.grid_forget()
    for Widget in transaction.winfo_children():
        Widget.destroy()        
    transaction.grid(row= 0, column=1,pady=5)
    transaction.tkraise()
    populateTransaction(transaction)

def homeHelper():
    # home.grid_forget()
    itemTracker.grid_forget()
    tagSummary.grid_forget()
    transaction.grid_forget()
    for Widget in home.winfo_children():
        Widget.destroy()
    home.grid(row=0, column=1)
    home.tkraise()
    populateHome(home)

def tagSummaryHelper():
    home.grid_forget()
    itemTracker.grid_forget()
    # tagSummary.grid_forget()
    transaction.grid_forget()
    for Widget in tagSummary.winfo_children():
        Widget.destroy()
    tagSummary.grid(row=0,column=1,pady=5)
    tagSummary.tkraise()
    populateTagSummary(tagSummary)

def itemTrackerHelper():
    home.grid_forget()
    # itemTracker.grid_forget()
    tagSummary.grid_forget()
    transaction.grid_forget()
    for Widget in itemTracker.winfo_children():
        Widget.destroy()
    itemTracker.grid(row= 0, column = 1,pady=5)
    itemTracker.tkraise()
    populateItemTracker(itemTracker)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def FrameWidth(event):
    canvas_width = event.width
    canvas.itemconfig(canvas_frame, width = canvas_width)

canvas = Canvas(root, borderwidth=0)
frame = Frame(canvas)
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas_frame = canvas.create_window((0,0), anchor="nw")
canvas.itemconfigure(canvas_frame, window = frame)
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
canvas.bind('<Configure>', lambda event: FrameWidth(event))


frameTab = Frame(frame)
frameTab.pack(side="top", fill = "both", expand = True)
frameTab.grid_columnconfigure(0,weight=1)
frameTab.grid_columnconfigure(1,weight=1)
frameTab.grid_columnconfigure(2,weight=1)
frameTab.grid_columnconfigure(3,weight=1)
Button(frameTab, text = "Home", relief="solid", width= 50,height=2, bd = 1,bg='yellow',fg='purple', command=homeHelper,font=("Times", "13", "bold italic")).grid(row = 0, column = 0)
Button(frameTab, text = "Transaction", relief="solid", width= 50,height=2, bd = 1,bg='yellow',fg='purple', command=transactionHelper,font=("Times", "13", "bold italic")).grid(row = 0, column = 1)
Button(frameTab, text = "Expense Summary", relief="solid", width= 50,height=2, bd = 1,bg='yellow',fg='purple',command=tagSummaryHelper,font=("Times", "13", "bold italic")).grid(row = 0, column = 2)
Button(frameTab, text = "Item Budget", relief="solid", width= 50,height=2, bd = 1,bg='yellow',fg='purple',command=itemTrackerHelper,font=("Times", "13", "bold italic")).grid(row = 0, column = 3)

f = Frame(frame)
f.pack(fill = BOTH, expand = True)
f.grid_columnconfigure(0,weight=1)
f.grid_columnconfigure(1,weight=8)
f.grid_columnconfigure(2,weight=1)

home = Frame(f)
home.grid(row=0,column=1)
populateHome(home)
transaction = Frame(f)
tagSummary = Frame(f)
itemTracker = Frame(f)
home.tkraise()
root.mainloop()
