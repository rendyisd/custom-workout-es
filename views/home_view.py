import tkinter
import customtkinter

class NormalCard(customtkinter.CTkFrame):
    def __init__(self, master, title, description, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.configure(border_width=2, corner_radius=10, fg_color="#074173")

        self.title_label = customtkinter.CTkLabel(self, text=title, text_color='white', font=('Arial', 14, 'bold'))
        self.title_label.pack(pady=(5, 0))

        self.title_desc = customtkinter.CTkLabel(self, text=description, text_color='white', font=('Arial', 12))
        self.title_desc.pack(pady=(0, 5))

class HomeView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color='white')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.card_fact_1 = NormalCard(self, 'Gym', '')
        self.card_fact_1.grid(row=0, column=0, padx=10, pady=10, sticky="new")

        self.card_fact_2 = NormalCard(self, 'BMI', '')
        self.card_fact_2.grid(row=0, column=1, padx=10, pady=10, sticky="new")

        self.card_fact_3 = NormalCard(self, 'Daily', '')
        self.card_fact_3.grid(row=0, column=2, padx=10, pady=10, sticky="new")

        self.card_fact_4 = NormalCard(self, 'Weekly', '')
        self.card_fact_4.grid(row=0, column=3, padx=10, pady=10, sticky="new")

        self.card_fact_5 = NormalCard(self, 'Goal', '')
        self.card_fact_5.grid(row=0, column=4, padx=10, pady=10, sticky="new")

        self.day_frame = customtkinter.CTkScrollableFrame(self)
        self.day_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=(0, 10), sticky="nsew")

        self.restart_btn = customtkinter.CTkButton(
            self, text="RESTART",
            width=200,
            height=40,
            fg_color='#D32626',
            hover_color='#9C1C1C',
            font=('Bahnschrift', 16, 'bold'),
        )
        self.restart_btn.grid(row=2, column=0, columnspan=5, sticky='ws', padx=10, pady=(0, 10))
    
