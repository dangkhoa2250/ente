from models.main import Model
from models.auth import User
from views.main import View
import tkinter.filedialog as filedialog
from tkinter import *

class Step1Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["step1view"]
        self.unlocker = self.model.unlocker
        self.filename = None
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.button_browse.config(command=self.select_file)
        self.frame.button_run.config(command=self.run_step1)
        self.frame.button_cancel.config(command=self.destroy_app)

    def destroy_app(self) -> None:
        self.view.root.destroy()
        
    def select_file(self) -> None:
        self.frame.selectFile.delete(0, END)
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.frame.selectFile.delete(1, END)
            self.frame.selectFile.insert(0, self.filename)

    def run_step1(self) -> None:
        if self.filename:
            if self.has_password(self.filename):
                result, unlocked_file = self.unlock(self.filename, self.view.get_password())
                if result == False:
                    self.view.message("error", "Wrong Password")
                else:
                    self.view.message("info", "Unlock Sucessfully")
            else:
                self.view.message("error", "File is invalid")
        else:
            self.view.message("error", "Please select a file")

    def has_password(self, file_path: str) -> bool:
        try:
            wb = openpyxl.load_workbook(file_path)
            return False
        except:
            return True
        
    def unlock(self, file_path: str, password: str) -> tuple:
        return self.unlocker.unlock_file(file_path, password)
