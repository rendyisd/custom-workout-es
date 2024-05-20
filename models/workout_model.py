import json
from .base import ObservableModel

class Workout(ObservableModel):
    def __init__(self, workout_plan_id):
        super().__init__()

        self.workout_plan_id = workout_plan_id

        self.exercises = self._get_exercise_name() # returns a dictionary filled with resolved exercise name from the ids
    
    def _get_exercise_name(self):
        with open('controllers/inference_system/knowledge_base/solutions.json') as f:
            d = json.load(f)

            exercises = {}

            for k, v in d[self.workout_plan_id].items():
                day = "D" + str(int(k) + 1)

                exercises[day] = []

                for ex_id in v:
                    q = """
                        SELECT exercise
                        FROM ext_exercise
                        WHERE id = ?
                    """

                    self.cursor.execute(q, (ex_id,))
                    exercises[day].append(self.cursor.fetchone()[0])
            
        
        return exercises