import tkinter
import customtkinter

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.frame = self.view.frames['home']

        self._bind()

    def _bind(self):
        self.frame.restart_btn.configure(command=self.return_to_start)
    
    def return_to_start(self):
        frame_to_clear = self.frame.day_frame
        for widget in frame_to_clear.winfo_children():
            frame_to_clear._parent_canvas.yview_moveto(0)
            widget.destroy()

        self.view.switch('start')

    def change_card(self):
        gym = self.model.facts.gym
        bmi = self.model.facts.bmi
        daily = self.model.facts.daily
        weekly = self.model.facts.weekly
        goals = self.model.facts.goals

        self.frame.card_fact_1.title_desc.configure(text=gym)
        self.frame.card_fact_2.title_desc.configure(text=bmi)
        self.frame.card_fact_3.title_desc.configure(text=daily)
        self.frame.card_fact_4.title_desc.configure(text=weekly)
        self.frame.card_fact_5.title_desc.configure(text=goals)
    
    def add_exercise_labels(self, day_n, exercises):
        workout_view = self.view.frames['workout']

        # change day label
        workout_view.day_label.configure(text=f'DAY {day_n}')

        # clears scrollable frame
        frame_to_clear = workout_view.scrollable_frame
        for widget in frame_to_clear.winfo_children():
            frame_to_clear._parent_canvas.yview_moveto(0)
            widget.destroy()

        for exercise in exercises:
            button_as_label = customtkinter.CTkButton(
                workout_view.scrollable_frame,
                text=exercise,
                height=100,
                fg_color='white',
                hover_color = '#F8F2ED',
                font=('Bahnschrift', 20, 'bold'),
                text_color='black'
            )

            button_as_label.pack(fill=customtkinter.BOTH, expand=True, anchor='center', padx=10, pady=10)

        self.view.switch('workout')

    
    def add_workout_buttons(self, workout_plan):
        for i, key in enumerate(workout_plan):
            btn = customtkinter.CTkButton(
                self.frame.day_frame,
                text='DAY '+str(i+1),
                height=100,
                fg_color='#D32626',
                hover_color='#9C1C1C',
                font=('Bahnschrift', 20, 'bold'),
                command=lambda day_n=i+1, exercises_name=workout_plan[key]: self.add_exercise_labels(day_n, exercises_name)
            )

            # command=lambda v=value: show_frame(v)

            btn.pack(fill=customtkinter.BOTH, expand=True, anchor='center', padx=10, pady=10)
