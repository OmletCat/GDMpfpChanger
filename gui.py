import customtkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from os import getcwd

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.buttons()

    def buttons(self):
        self.image_button = tk.CTkButton(self, text="Select Image", command=self.image_selector_callback)
        self.image_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.show_image_button = tk.CTkButton(self, text="Show Image", command=self.preview_image)
        self.show_image_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    def image_selector_callback(self):
        self.image_path = askopenfilename()

    def preview_image(self):
        try:
            image = Image.open(self.image_path)
            image.show()
        except:
            print("Error: No Image Selected")
