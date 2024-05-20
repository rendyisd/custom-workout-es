class WorkoutController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.frame = self.view.frames['workout']

        self._bind()

    def _bind(self):
        self.frame.return_btn.configure(command=self.return_to_home)
    
    def return_to_home(self):
        self.view.switch('home')