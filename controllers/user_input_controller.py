from models.facts_model import Facts
from views.user_input_view import SubmitPopup

class UserInputController:
    def __init__(self, model, view, controller):
        self.model = model
        self.view = view
        self.controller = controller

        self.frame = self.view.frames['user-input']
        self._bind()

    def _bind(self):
        self.frame.return_btn.configure(command=self.return_to_start)
        self.frame.submit_btn.configure(command=self.submit_answer)
    
    def return_to_start(self):
        self.view.switch('start')
    
    def submit_answer(self):
        data = {
            'gym': self.frame.qc_1.get_selected(),
            'bmi': self.frame.qc_2.get_selected(),
            'daily': self.frame.qc_3.get_selected(),
            'weekly': self.frame.qc_4.get_selected(),
            'goals': self.frame.qc_5.get_selected()
        }

        for _, ans in data.items():
            if ans == 'NONE':
                popup = SubmitPopup(self.frame)
                popup.place(relx=0.5, rely=0.5, anchor="center")
                return

        self.model.facts = Facts.from_dict(data)
        workout_plan = self.controller.inference_controller.infer_workout_plan()

        self.controller.home_controller.change_card()
        self.controller.home_controller.add_workout_buttons(workout_plan.exercises)

        self.view.switch('home')