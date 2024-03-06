from tkinter import *
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime
class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Business Maching")
        self.createWidgets()

    def select_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.selectFile.delete(1, tk.END)
            self.selectFile.insert(0, filename)
            
    def getFilePath(self):
        return self.selectFile.get()
    
    def getPassword(self):
        return self.password.get()
      
    def createWidgets(self):
        self.labelStep1 = Label(self.root, text="Step 1&2")
        self.labelStep1.grid(row=0, column=0, padx=5, pady=5)

        self.selectFile = Entry(self.root, textvariable="", width=30)
        self.selectFile.grid(row=0, column=1, padx=5, pady=5)
        
        self.labelPassword = Label(self.root, text="Password")
        self.labelPassword.grid(row=1, column=0, padx=5, pady=5)
        
        self.password = Entry(self.root, show="*", width=30)
        self.password.grid(row=1, column=1, padx=5, pady=5)
        
        
        period_frame = tk.Frame(self.root)
        self.outputPeriod = Label(period_frame, text="年月選択")
        self.outputPeriod.grid(row=2, column=0, padx=5, pady=5)
        
        Lb_year = tk.Label(period_frame, text="年", fg="#333333", justify="center", font=('MS Gothic', '12'))
        Lb_year.grid(row=2, column=2, padx=1, pady=5, sticky="w")
        Lb_month = tk.Label(period_frame, text="月", fg="#333333", justify="center", font=('MS Gothic', '12'))
        Lb_month.grid(row=2, column=4, padx=1, pady=5, sticky="w")
        
        _value = []
        for i in range(0, 5):
            _value.append(int(datetime.now().year) - i)
        year_list=ttk.Combobox(period_frame, values=_value, state="readonly", justify="center", width=5 ,font=('MS Gothic', '12'))
        year_list.current(1 if int(datetime.now().month) == 1 else 0)
        year_list.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        _value = []
        for i in range(1, 13):
            _value.append(i)
        month_list=ttk.Combobox(period_frame, values=_value, state="readonly", justify="center", width=3 ,font=('MS Gothic', '12'))
        month_list.current(11 if int(datetime.now().month) == 1 else int(datetime.now().month) - 2)
        month_list.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        period_frame.grid(row=2, column=1)
        
        self.buttonBrowse = Button(self.root, text="Browse...", command=self.select_file)
        self.buttonBrowse.grid(row=0, column=2)
        
        self.buttonRunStep1 = Button(self.root, text="Run")
        self.buttonRunStep1.grid(row=2, column=2, padx=5, pady=5, sticky="w")
    
    def message(self, type, message):
        if type == "error":
            messagebox.showerror(type, message)
        if type == "info":
            messagebox.showinfo(type, message)