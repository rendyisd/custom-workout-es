import tkinter
import customtkinter

from PIL import Image

class StartView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        img_path = 'assets/main-screen.png'

        self.start_screen_img = customtkinter.CTkImage(
            light_image=Image.open(img_path),
            dark_image=Image.open(img_path),
            size=(1100,580)
        )

        self.start_screen_img_lbl = customtkinter.CTkLabel(self, text='', image=self.start_screen_img)
        self.start_screen_img_lbl.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.start_form_btn = customtkinter.CTkButton(
            self.start_screen_img_lbl,
            text="CUSTOMIZE",
            width=200,
            height=40,
            fg_color='#D32626',
            hover_color='#9C1C1C',
            font=('Bahnschrift', 16, 'bold'),
            
        )
        self.start_form_btn.place(x=155, y=430)