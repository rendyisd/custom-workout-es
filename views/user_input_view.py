import tkinter
import customtkinter

class QuestionCard(customtkinter.CTkFrame):
    def __init__(self, master, question, choices, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(border_width=2, corner_radius=10, fg_color="#074173")

        self.question_label = customtkinter.CTkLabel(self, text=question, text_color='white', font=("Helvetica", 16, "bold"))
        self.question_label.pack(pady=(20, 0))

        self._selected_var = customtkinter.StringVar(value='NONE')

        for choice in choices:
            radio_button = customtkinter.CTkRadioButton(
                self,
                text=choice,
                variable=self._selected_var,
                value=choice,
                text_color='white',
                hover_color='#3A6BFF',
                border_color='white',
                fg_color='#3AB0FF'
            )

            radio_button.pack(anchor='w', padx=30, pady=5)
        
    def get_selected(self):
        return self._selected_var.get()

class SubmitPopup(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(border_width=2, corner_radius=10, fg_color='red', border_color='red', background_corner_colors=('#074173', '#074173', '#074173', '#074173'))
        
        self.message_label = customtkinter.CTkLabel(self, text="Please answer all questions before submitting.", text_color='white', font=("Helvetica", 12), fg_color='red')
        self.message_label.pack(padx=10, pady=10)
                
        # Schedule self.dismiss() to be called after 3000 milliseconds (3 seconds)
        self.after(2000, self.dismiss)

    def dismiss(self):
        self.destroy()

class UserInputView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color='white')

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        q_1 = 'Do you have gym access?'
        c_1 = ['Yes', 'No']
        self.qc_1 = QuestionCard(self, question=q_1, choices=c_1)
        self.qc_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        q_2 = 'What is your BMI?'
        c_2 = ['Underweight', 'Proportional', 'Overweight']
        self.qc_2 = QuestionCard(self, question=q_2, choices=c_2)
        self.qc_2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        q_3 = 'How long can you workout in a day?'
        c_3 = ['15-30 minutes', '30-60 minutes', '60+ minutes']
        self.qc_3 = QuestionCard(self, question=q_3, choices=c_3)
        self.qc_3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        q_4 = 'How many times do you workout in a week?'
        c_4 = ['1-2 times', '3 times', '3+ times']
        self.qc_4 = QuestionCard(self, question=q_4, choices=c_4)
        self.qc_4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        
        q_5 = 'What do you want to focus on?'
        c_5 = ['Weight loss', 'Muscle gain', 'Endurance', 'General health']
        self.qc_5 = QuestionCard(self, question=q_5, choices=c_5)
        self.qc_5.grid(row=0, column=2, padx=10, pady=10, rowspan=2, sticky="nsew")

        self.submit_btn = customtkinter.CTkButton(
            self, text="SUBMIT",
            width=200,
            height=40,
            fg_color='#3AB0FF',
            hover_color='#3A6BFF',
            font=('Bahnschrift', 16, 'bold'),
        )
        self.submit_btn.grid(row=2, column=2, columnspan=1, sticky='es', padx=10, pady=(0, 10))

        self.return_btn = customtkinter.CTkButton(
            self, text="RETURN",
            width=200,
            height=40,
            fg_color='#D32626',
            hover_color='#9C1C1C',
            font=('Bahnschrift', 16, 'bold'),
        )
        self.return_btn.grid(row=2, column=0, columnspan=1, sticky='ws', padx=10, pady=(0, 10))