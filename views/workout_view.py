import tkinter
import customtkinter

class WorkoutView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color='white')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)

        self.day_label = customtkinter.CTkLabel(
            self,
            text='DAY N',
            font=('Bahnschrift', 32, 'bold'),
        )
        self.day_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.return_btn = customtkinter.CTkButton(
            self, text="RETURN",
            width=200,
            height=40,
            fg_color='#D32626',
            hover_color='#9C1C1C',
            font=('Bahnschrift', 16, 'bold'),
        )
        self.return_btn.grid(row=2, column=0, sticky='ws', padx=10, pady=(0, 10))
