class StartController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.frame = self.view.frames['start']
        self._bind()

    def _bind(self):
        self.frame.start_form_btn.configure(command=self.user_input_form_view)
    
    def user_input_form_view(self):
        self.view.switch('user-input')