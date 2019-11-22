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
    frameTab = Frame(frame, width = root.winfo_screenwidth())
    frameTab.pack(side="top", fill = "both", expand = True)
    frameTab.grid_columnconfigure(0,weight=1)
    frameTab.grid_columnconfigure(1,weight=1)
    frameTab.grid_columnconfigure(2,weight=1)
    frameTab.grid_columnconfigure(3,weight=1)
    Button(frameTab, text = "Home", relief="solid", width= 10, bd = 1).grid(row = 0, column = 0)
    Button(frameTab, text = "Transaction", relief="solid", width= 13, bd = 1).grid(row = 0, column = 1)
    Button(frameTab, text = "Expense Summary", relief="solid", width= 20, bd = 1).grid(row = 0, column = 2)
    Button(frameTab, text = "Item Budget", relief="solid", width= 15, bd = 1).grid(row = 0, column = 3)
    Label(frame, text = "This Month", width= rootWidth, height = 3, anchor=CENTER, bg='blue',bd=4).pack()
    
    scaleFrame = Frame(frame)
    scaleFrame.pack(fill=BOTH, expand = True)
    scaleFrame.grid_columnconfigure(0, weight = 1)
    scaleFrame.grid_columnconfigure(1, weight = 1)
    for i in range(20):
        Label(scaleFrame, text='Tag1', fg = 'green', pady=20).grid(row = i, column = 0)
        Scale(scaleFrame, orient = HORIZONTAL, length = 200, from_=1, to=100, fg = 'green', troughcolor = 'black').grid(row = i, column = 1)

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

    Button(scaleFrame, text = 'Set item Budget', command = setBudget, fg = 'blue', bg = 'yellow', width = 20, height = 2).grid(row =20, column = 0)
populate(frame)
root.mainloop()

