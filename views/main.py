from .root import Root

from .start_view import StartView
from .user_input_view import UserInputView
from .home_view import HomeView
from .workout_view import WorkoutView

class View:
    def __init__(self):
        self.root = Root()
        
        self.frames = {}

        self.current_frame = None

        self._add_frame(StartView, 'start')
        self._add_frame(UserInputView, 'user-input')
        self._add_frame(HomeView, 'home')
        self._add_frame(WorkoutView, 'workout')

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        
        self.current_frame = frame
        self.current_frame.grid(row=0, column=0, sticky="nsew")
    
    def start_mainloop(self):
        self.root.mainloop()