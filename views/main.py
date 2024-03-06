from typing import TypedDict
from .root import Root
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView
from .step1view import Step1View
from tkinter import simpledialog
from tkinter import messagebox


class Frames(TypedDict):
    signup: SignUpView
    signin: SignInView
    home: HomeView
    step1view: Step1View


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
        self._add_frame(Step1View, "step1view")
        

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
    
    def message(self, type: str, message: str) -> None:
        if type == "error":
            messagebox.showerror("Error", message)
        elif type == "info":
            messagebox.showinfo("Info", message)
        else:
            messagebox.showwarning("Warning", message)
            
    def get_password(self):
        self.password = simpledialog.askstring("Password", "Enter password:", show='*')
        if self.password:
            print("Entered password:", self.password)
            return self.password
        else:
            print("Password not entered.")
            messagebox.showerror("Error", "Password not entered. Please try again.")
            self.get_password()
