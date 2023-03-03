#Libraries
from tkinter import *
from tkcalendar import *

#Application Creation
root = Tk()
root.geometry("300x300+340+80")
root.title("Calendar")
root.resizable(False,False)
root.configure(bg="light blue")

#Application Setup
cal = Calendar(root, setmode = "day",date_pattern='dd/mm/yyyy')
cal.pack(padx=15,pady=45)
root.mainloop()