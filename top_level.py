import customtkinter as tk
from tkinter import StringVar

class ToplevelWindow(tk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1)

        self.buttons()

    def text(self, my_text):
        self.label = tk.CTkLabel(self, text=my_text)
        self.label.grid(row = 0, padx=20, pady=20, columnspan = 2)

    def box(self, my_contents):
        text = StringVar()
        text.set(my_contents)
        self.box = tk.CTkEntry(self, textvariable = text)
        self.box.grid(row = 1, padx=20, pady=20, sticky = "ew", columnspan = 2)

    def buttons(self):
        self.button = tk.CTkButton(self, text = "Close Program", command = self.button_callback)
        self.button.grid(row = 2, padx=20, pady=20, sticky = "ew", columnspan = 2)

    def button_callback(self):
        self.quit()
