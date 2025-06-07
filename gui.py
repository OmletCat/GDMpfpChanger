import customtkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import StringVar
from PIL import Image
from os import getlogin
from pyperclip import copy
from top_level import ToplevelWindow


class App(tk.CTk):
    def __init__(self):
        super().__init__()


        self.my_title = "GDM pfp Changer"
        self.title(self.my_title)
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)
        self._set_appearance_mode("system")

        self.header()
        self.buttons()
        self.labels()


    def header(self):
        self.label = tk.CTkLabel(self, text=self.my_title, fg_color="transparent", font = ("Arial", 40))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan = 2)


    def buttons(self):
        self.image_button = tk.CTkButton(self, text="Select Image", command=self.image_selector_callback)
        self.image_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

        self.show_image_button = tk.CTkButton(self, text="Show Image", command=self.preview_image)
        self.show_image_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.apply_button = tk.CTkButton(self, text="Get Command", command=self.apply_changes)
        self.apply_button.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    def labels(self):
        self.username = StringVar()
        self.username.set(getlogin())

        self.entry = tk.CTkEntry(self, textvariable=self.username)
        self.entry.grid(row=3, column = 1, padx=20, pady=20, sticky="ew")

        self.username_label = tk.CTkLabel(self, text = "Username:\n(needed for file names)")
        self.username_label.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = "ew")

        self.file_path = StringVar()
        self.entry = tk.CTkEntry(self, textvariable=self.file_path)
        self.entry.grid(row=1, column = 1, padx=20, pady=20, sticky="ew")


    def image_selector_callback(self):
        self.file_path.set(askopenfilename())

    def preview_image(self):
        try:
            image = Image.open(self.file_path.get())
            image.show()
        except:
            top = ToplevelWindow()
            text = "Error: No image selected!"
            top.text(text)

    def apply_changes(self):
        src = self.file_path.get()
        des = "/var/lib/AccountsService/icons/" + self.username.get()
        command = f"cp {src} {des}"

        top = ToplevelWindow()
        text = "Command:\nCopied to clipboard!\n\nRun command with sudo to change pfp!"
        top.text(text)
        top.box(command)
        copy(command)
