from .base import ObservableModel

class Facts(ObservableModel):
    def __init__(self, gym=None, bmi=None, daily=None, weekly=None, goals=None):
        super().__init__()

        self.gym = gym
        self.bmi = bmi
        self.daily = daily
        self.weekly = weekly
        self.goals = goals

    @classmethod
    def from_dict(cls, data):
        return cls(
            gym=data.get('gym'),
            bmi=data.get('bmi'),
            daily=data.get('daily'),
            weekly=data.get('weekly'),
            goals=data.get('goals'),
        )
    
    def infer_suggested_focus(self):
        q1 = """
            SELECT id
            FROM set2_goals
            WHERE goals = ?
        """
        self.cursor.execute(q1, (self.goals,))
        goal_id = self.cursor.fetchone()[0]

        q2 = """
            SELECT id
            FROM set2_bmi
            WHERE bmi_category = ?
        """
        self.cursor.execute(q2, (self.bmi,))
        bmi_id = self.cursor.fetchone()[0]

        q3 = """
            SELECT focus
            FROM set1_focus
            WHERE goal_id = ? and bmi_id = ?
        """

        self.cursor.execute(q3, (goal_id, bmi_id))
        infered_suggested_focus = self.cursor.fetchone()[0]

        return infered_suggested_focus


    def infer_intensity(self):
        q1 = """
            SELECT id
            FROM set3_daily
            WHERE daily_time = ?
        """
        self.cursor.execute(q1, (self.daily,))
        daily_id = self.cursor.fetchone()[0]

        q2 = """
            SELECT id
            FROM set3_weekly
            WHERE weekly_freq = ?
        """
        self.cursor.execute(q2, (self.weekly,))
        weekly_id = self.cursor.fetchone()[0]

        q3 = """
            SELECT intensity
            FROM set1_intensity
            WHERE daily_id = ? and weekly_id = ?
        """

        self.cursor.execute(q3, (daily_id, weekly_id))
        infered_intensity = self.cursor.fetchone()[0]

        return infered_intensity