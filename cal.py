from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
 

def get_date():
    today = datetime.today()    
    current_date = None
    # Create Object
    root = Tk()
    
    # Set geometry
    root.geometry("250x250")
    
    # Add Calendar
    cal = Calendar(root, selectmode = 'day',
                year = today.year, month = today.month,
                day = today.day)
    
    cal.pack(pady = 20)
    
    def grad_date():  
        nonlocal current_date
        date_str = cal.get_date()
        current_date = datetime.strptime(date_str, '%d/%m/%y')
        root.destroy()    
    
    # Add Button and Label
    Button(root, text = "Get Date",
        command = grad_date).pack(pady = 20)
    
    date = Label(root, text = "")
    date.pack(pady = 20)
    
    # Execute Tkinter
    root.mainloop()
    date_obj = datetime.strptime(str(current_date), '%Y-%m-%d %H:%M:%S')
    date_only = date_obj.date()
    return date_only