import customtkinter as tk

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = tk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox_1 = tk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox_2 = tk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

    def button_callback(self):
        print("button pressed")
