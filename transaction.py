from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Transaction Page")
root.geometry("600x600")

canvas = Canvas(root, borderwidth=0)
frame = Frame(canvas)
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas_frame = canvas.create_window((0,0), anchor="nw")
canvas.itemconfigure(canvas_frame, window = frame)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def FrameWidth(event):
    canvas_width = event.width
    canvas.itemconfig(canvas_frame, width = canvas_width)

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
canvas.bind('<Configure>', lambda event: FrameWidth(event))

rootWidth = root.winfo_screenwidth()
def populate(frame):
    frameTab = Frame(frame)
    frameTab.pack(side="top", fill = "both", expand = True)
    frameTab.grid_columnconfigure(0,weight=1)
    frameTab.grid_columnconfigure(1,weight=1)
    frameTab.grid_columnconfigure(2,weight=1)
    frameTab.grid_columnconfigure(3,weight=1)
    Button(frameTab, text = "Home", relief="solid", width= 10, bd = 1).grid(row = 0, column = 0)
    Button(frameTab, text = "Transaction", relief="solid", width= 13, bd = 1).grid(row = 0, column = 1)
    Button(frameTab, text = "Expense Summary", relief="solid", width= 20, bd = 1).grid(row = 0, column = 2)
    Button(frameTab, text = "Item Budget", relief="solid", width= 15, bd = 1).grid(row = 0, column = 3)
    Label(frame, text = "Your Transactions", width= rootWidth, height = 3, anchor=CENTER, bg='pink',bd=4).pack()
    searchFrame = Frame(frame, padx = 10, pady=10)
    searchFrame.pack(fill=BOTH, expand = True)
    searchFrame.grid_columnconfigure(0, weight=1)
    searchFrame.grid_columnconfigure(1, weight=1)
    searchFrame.grid_columnconfigure(2, weight=1)
    searchFrame.grid_columnconfigure(3, weight=1)
    Label(searchFrame, text = "From").grid(row = 0, column = 1)
    Entry(searchFrame, width=20).grid(row=0, column=2)
    Label(searchFrame, text = "To").grid(row = 1, column = 1)
    Entry(searchFrame, width=20).grid(row=1, column=2)

    def search():
        for widget in dataFrame.winfo_children():
            widget.destroy()
        for row in range(100):
            Label(dataFrame, text="%s" % row, width=3, borderwidth="1", 
                    relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            Label(dataFrame, text=t).grid(row=row, column=1)

    Button(searchFrame, text="Search", width=10, command = search).grid(row = 2, column = 2)
    dataFrame = Frame(frame, padx = 10, pady=10)
    dataFrame.pack(fill = BOTH, expand = True)
    dataFrame.grid_columnconfigure(0, weight=1)
    dataFrame.grid_columnconfigure(1, weight=2)
    dataFrame.grid_columnconfigure(2, weight=1)
 

    for row in range(100):
        if row%2 == 0:
            Label(dataFrame, text="Tag %s expenses" % (row+1), width = 50, height = 3, borderwidth="1", relief="solid",bg='red').grid(row = row, column = 1)
            # t="this is the second column for row %s" %(row+1)
            # Label(dataFrame, text=t,height = 3,bg='red').grid(row=row, column=1)
        else:
            Label(dataFrame, text="Tag %s" % (row+1), width = 50, height = 3, borderwidth="1", relief="solid",bg='green').grid(row = row, column = 1)
            # t="this is the second column for row %s" %(row+1)
            # Label(dataFrame, text=t,height = 3,bg='green').grid(row=row, column=1)
populate(frame)

root.mainloop()