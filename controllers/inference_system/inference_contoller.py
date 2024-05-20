from models.workout_model import Workout

class InferenceController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def infer_workout_plan(self):
        suggested_focus = self.model.facts.infer_suggested_focus()
        intensity = self.model.facts.infer_intensity()
        gym_access = self.model.facts.gym

        workout_plan = "NONE"

        if (intensity == "Light") and (suggested_focus == "Cardio"):
            workout_plan = "W1"
        
        elif (gym_access == "Yes") and (intensity == "Light") and (suggested_focus == "Bodybuilding"):
            workout_plan = "W4"
        
        elif (intensity == "Light") and (suggested_focus == "Powerlifting"):
            workout_plan = "W7"

        elif (intensity == "Light") and (suggested_focus == "HIIT"):
            workout_plan = "W10"
        
        elif (gym_access == "Yes") and (intensity == "Moderate") and (suggested_focus == "Cardio"):
            workout_plan = "W2"

        elif (gym_access == "Yes") and (intensity == "Moderate") and (suggested_focus == "Bodybuilding"):
            workout_plan = "W5"
        
        elif (intensity == "Moderate") and (suggested_focus == "Powerlifting"):
            workout_plan = "W8"
        
        elif (intensity == "Moderate") and (suggested_focus == "HIIT"):
            workout_plan = "W11"
        
        elif (intensity == "Heavy") and (suggested_focus == "Cardio"):
            workout_plan = "W3"
        
        elif (gym_access == "Yes") and (intensity == "Heavy") and (suggested_focus == "Bodybuilding"):
            workout_plan = "W6"
        
        elif (intensity == "Heavy") and (suggested_focus == "Powerlifting"):
            workout_plan = "W9"
        
        elif (gym_access == "Yes") and (intensity == "Heavy") and (suggested_focus == "HIIT"):
            workout_plan = "W12"
        
        elif (gym_access == "No") and (intensity == "Light") and (suggested_focus == "Bodybuilding"):
            workout_plan = "W13"
        
        elif (gym_access == "No") and (intensity == "Moderate") and (suggested_focus == "Cardio"):
            workout_plan = "W14"
        
        elif (gym_access == "No") and (intensity == "Moderate") and (suggested_focus == "Bodybuilding"):
            workout_plan = "W15"
        
        elif (gym_access == "No") and (intensity == "Heavy") and (suggested_focus == "Bodybuilding"):
            workout_plan = "W16"
        
        elif (gym_access == "No") and (intensity == "Heavy") and (suggested_focus == "HIIT"):
            workout_plan = "W17"
        
        return Workout(workout_plan_id=workout_plan)