import tkinter
import customtkinter

customtkinter.set_appearance_mode("light")

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        start_width = 1100
        start_height = 580

        self.title("Custom Workout Plan - Expert System")
        self.geometry(f"{start_width}x{start_height}")

        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)