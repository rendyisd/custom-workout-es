from .start_controller import StartController
from .user_input_controller import UserInputController
from .home_controller import HomeController
from .inference_system.inference_contoller import InferenceController
from.workout_controller import WorkoutController

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.start_controller = StartController(model, view)
        self.user_input_controller = UserInputController(model, view, self)
        self.home_controller = HomeController(model, view)
        self.inference_controller = InferenceController(model, view)
        self.workout_controller = WorkoutController(model, view)

    def start(self):
        self.view.switch('start')

        self.view.start_mainloop()