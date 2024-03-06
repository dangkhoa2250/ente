import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

def browse_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def run_application():
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    if password:
        print("Entered password:", password)
    else:
        messagebox.showerror("Error", "Password not entered. Please try again.")
        run_application()

# Tạo cửa sổ chính
app = tk.Tk()
app.title("Simple File Browser App")

# Tạo và cấu hình các thành phần trong cửa sổ
frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_path = tk.Label(frame, text="File Path:")
label_path.grid(row=0, column=0, sticky="e")

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=0, column=1, padx=10)

button_browse = tk.Button(frame, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2)

button_run = tk.Button(frame, text="Run", command=run_application)
button_run.grid(row=1, columnspan=3, pady=10)

# Chạy ứng dụng
app.mainloop()
