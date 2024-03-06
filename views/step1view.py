from tkinter import *

class Step1View(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Step 1", font=("Helvetica", 16, "bold"))
        self.header.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.frame1 = Frame(self, borderwidth=2, relief=RIDGE)
        self.frame1.grid(row=1, column=0, columnspan=2, padx=5, pady=5,sticky="nsew")
        self.scrollbar = Scrollbar(self.frame1, orient="vertical")
        
        self.text_description = Text(self.frame1, wrap="word", yscrollcommand=self.scrollbar.set, height=10, width=70)
        self.text_description.insert(END, "データの抽出とチェック", "bold")
        self.text_description.insert(END, """
    1. 元のExcelファイルから3つのシートのデータを抽出します（「案件管理【全所属】」、\n「紹介料支払い実績【不営課】」、および「リストマスタ」）。
    2. 各シートから特定の列のデータを取得し、それに基づいてセットを作成します。
    3. データを新しいシートに貼り付けながら、特定の条件を確認しています。\n""")
        
        self.text_description.insert(END, "\n例: 案件管理【全所属】のデータチェック", "bold")
        self.text_description.insert(END, """
        IDが一意であり、数字であることを確認します。
        初回受付の日付が正しい形式になっているかを確認します。
        金融機関、種別、ステータスがそれぞれリストマスタに存在するかを確認します。
        このタスクは、データの整合性を確認しながら元のExcelファイルから必要な情報を取り出し、新しいシートに貼り付けています。
        """)
        self.text_description.tag_configure("bold", font=("Helvetica", 12, "bold"))
        self.text_description.pack(side="left", expand=True, fill="both")

        # Thiết lập kết nối giữa thanh cuộn và vùng văn bản
        self.scrollbar.config(command=self.text_description.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.frame2 = Frame(self)
        self.frame2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.filename = Label(self.frame2, text="File name: ")
        self.filename.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.selectFile = Entry(self.frame2, textvariable="", width=70)
        self.selectFile.grid(row=2, column=1, padx=5, pady=5, sticky="we")
        
        self.button_browse = Button(self.frame2, text="Browse", height=1, width=10)
        self.button_browse.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        
        self.button_run = Button(self.frame2, text="Run", height=1, width=10)
        self.button_run.grid(row=3, column=0, padx=5 ,sticky="w")
        
        self.button_cancel = Button(self.frame2, text="Cancel", height=1, width=10)
        self.button_cancel.grid(row=3, column=2, padx=5 ,sticky="w")
