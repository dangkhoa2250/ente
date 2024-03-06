from tkinter import *
import tkinter as tk
import View
import openpyxl
import Model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.buttonRunStep1["command"] = self.runStep1
        
    def runStep1(self):
        file_path = view.getFilePath()
        if self.has_password(file_path):
            result, unlocked_file = self.unlock(file_path, view.getPassword())
            if result == False:
                view.message("error", "Wrong Password")
            else:
                view.message("info", "Unlock Sucessfully")
        else:
            view.message("error", "File is invalid")
        
        
    def has_password(self, file_path):
        try:
            wb = openpyxl.load_workbook(file_path)
            return False
        except:
            return True
    
    def unlock(self, file_path, password):
        return self.model.unlock_file(self, file_path, password)
        
if _name_ == "_main_":
    root = tk.Tk()
    view = View.View(root)
    model = Model.Model
    controller = Controller(model, view)
    root.mainloop()