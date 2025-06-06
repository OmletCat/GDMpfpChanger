import customtkinter as tk
from tkinter.filedialog import askopenfilename
import PIL

class utils(tk.CTK):
    def __init__(self):
        super().__init__()

    def image_selector_callback(self):
        image_path = askopenfilename()

    def preview_image(self):
        image =
