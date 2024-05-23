-- Create table set2_bmi
CREATE TABLE IF NOT EXISTS set2_bmi (
    id INTEGER PRIMARY KEY,
    bmi_category VARCHAR NOT NULL
);

-- Insert data into set2_bmi
INSERT INTO set2_bmi (id, bmi_category) VALUES (1, 'Underweight');
INSERT INTO set2_bmi (id, bmi_category) VALUES (2, 'Proportional');
INSERT INTO set2_bmi (id, bmi_category) VALUES (3, 'Overweight');

-- Create table set2_goals
CREATE TABLE IF NOT EXISTS set2_goals (
    id INTEGER PRIMARY KEY,
    goals VARCHAR NOT NULL
);

-- Insert data into set2_goals
INSERT INTO set2_goals (id, goals) VALUES (1, 'Weight loss');
INSERT INTO set2_goals (id, goals) VALUES (2, 'Muscle gain');
INSERT INTO set2_goals (id, goals) VALUES (3, 'Endurance');
INSERT INTO set2_goals (id, goals) VALUES (4, 'General health');

-- Create table set3_daily
CREATE TABLE IF NOT EXISTS set3_daily (
    id INTEGER PRIMARY KEY,
    daily_time VARCHAR NOT NULL
);

-- Insert data into set3_daily
INSERT INTO set3_daily (id, daily_time) VALUES (1, '15-30 minutes');
INSERT INTO set3_daily (id, daily_time) VALUES (2, '30-60 minutes');
INSERT INTO set3_daily (id, daily_time) VALUES (3, '60+ minutes');

-- Create table set3_weekly
CREATE TABLE IF NOT EXISTS set3_weekly (
    id INTEGER PRIMARY KEY,
    weekly_freq VARCHAR NOT NULL
);

-- Insert data into set3_weekly
INSERT INTO set3_weekly (id, weekly_freq) VALUES (1, '1-2 times');
INSERT INTO set3_weekly (id, weekly_freq) VALUES (2, '3 times');
INSERT INTO set3_weekly (id, weekly_freq) VALUES (3, '3+ times');

-- Create table set1_gym
CREATE TABLE IF NOT EXISTS set1_gym (
    id INTEGER PRIMARY KEY,
    has_access VARCHAR NOT NULL
);

-- Insert data into set1_gym
INSERT INTO set1_gym (id, has_access) VALUES (1, 'Yes');
INSERT INTO set1_gym (id, has_access) VALUES (2, 'No');

-- Create table set1_intensity
CREATE TABLE IF NOT EXISTS set1_intensity (
    id INTEGER PRIMARY KEY,
    daily_id INTEGER NOT NULL,
    weekly_id INTEGER NOT NULL,
    intensity VARCHAR NOT NULL,
    FOREIGN KEY (daily_id) REFERENCES set3_daily (id),
    FOREIGN KEY (weekly_id) REFERENCES set3_weekly (id)
);

-- Insert data into set1_intensity
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (1, 1, 1, 'Light');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (2, 1, 2, 'Light');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (3, 1, 3, 'Light');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (4, 2, 1, 'Moderate');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (5, 2, 2, 'Moderate');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (6, 2, 3, 'Heavy');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (7, 3, 1, 'Moderate');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (8, 3, 2, 'Heavy');
INSERT INTO set1_intensity (id, daily_id, weekly_id, intensity) VALUES (9, 3, 3, 'Heavy');

-- Create table set1_focus
CREATE TABLE IF NOT EXISTS set1_focus (
    id INTEGER PRIMARY KEY,
    goal_id INTEGER NOT NULL,
    bmi_id INTEGER NOT NULL,
    focus VARCHAR NOT NULL,
    FOREIGN KEY (goal_id) REFERENCES set2_goals (id),
    FOREIGN KEY (bmi_id) REFERENCES set2_bmi (id)
);

-- Insert data into set1_focus
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (1, 1, 1, 'Cardio');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (2, 1, 2, 'Cardio');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (3, 1, 3, 'Cardio');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (4, 2, 1, 'Bodybuilding');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (5, 2, 2, 'Bodybuilding');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (6, 2, 3, 'Powerlifting');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (7, 3, 1, 'HIIT');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (8, 3, 2, 'HIIT');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (9, 3, 3, 'HIIT');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (10, 4, 1, 'Bodybuilding');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (11, 4, 2, 'HIIT');
INSERT INTO set1_focus (id, goal_id, bmi_id, focus) VALUES (12, 4, 3, 'Cardio');

-- Create table ext_exercise
CREATE TABLE IF NOT EXISTS ext_exercise (
    id INTEGER PRIMARY KEY,
    exercise VARCHAR NOT NULL
);

-- Insert data into ext_exercise
INSERT INTO ext_exercise (id, exercise) VALUES (1, 'Barbell Back Squat');
INSERT INTO ext_exercise (id, exercise) VALUES (2, 'Squat');
INSERT INTO ext_exercise (id, exercise) VALUES (3, 'Leg Press');
INSERT INTO ext_exercise (id, exercise) VALUES (4, 'Leg Curl');
INSERT INTO ext_exercise (id, exercise) VALUES (5, 'Reverse Leg Curl');
INSERT INTO ext_exercise (id, exercise) VALUES (6, 'Hip Thrust');
INSERT INTO ext_exercise (id, exercise) VALUES (7, 'Bulgarian Split');
INSERT INTO ext_exercise (id, exercise) VALUES (8, 'Calves Raises');
INSERT INTO ext_exercise (id, exercise) VALUES (9, 'Deadlift');
INSERT INTO ext_exercise (id, exercise) VALUES (10, 'Pull Up');
INSERT INTO ext_exercise (id, exercise) VALUES (11, 'Barbell Rowing');
INSERT INTO ext_exercise (id, exercise) VALUES (12, 'Lat Pulldown');
INSERT INTO ext_exercise (id, exercise) VALUES (13, 'Seated Cable Row');
INSERT INTO ext_exercise (id, exercise) VALUES (14, 'Flat Dumbbell/Bench Press');
INSERT INTO ext_exercise (id, exercise) VALUES (15, 'Incline Dumbbell/Bench Press');
INSERT INTO ext_exercise (id, exercise) VALUES (16, 'Pec Fly');
INSERT INTO ext_exercise (id, exercise) VALUES (17, 'Overhead Press');
INSERT INTO ext_exercise (id, exercise) VALUES (18, 'Lateral Raises');
INSERT INTO ext_exercise (id, exercise) VALUES (19, 'Reverse Pec Fly');
INSERT INTO ext_exercise (id, exercise) VALUES (20, 'Overhead Extension');
INSERT INTO ext_exercise (id, exercise) VALUES (21, 'Triceps Kick Back');
INSERT INTO ext_exercise (id, exercise) VALUES (22, 'Bicep Curl');
INSERT INTO ext_exercise (id, exercise) VALUES (23, 'Sit Up');
INSERT INTO ext_exercise (id, exercise) VALUES (24, 'Bicycle Crunches');
INSERT INTO ext_exercise (id, exercise) VALUES (25, 'Russian Twist');
INSERT INTO ext_exercise (id, exercise) VALUES (26, 'Jogging');
INSERT INTO ext_exercise (id, exercise) VALUES (27, 'Jumping Jacks');
INSERT INTO ext_exercise (id, exercise) VALUES (28, 'Mountain Climbers');
INSERT INTO ext_exercise (id, exercise) VALUES (29, 'Push Up Burpees');
INSERT INTO ext_exercise (id, exercise) VALUES (30, 'Jump Rope');
INSERT INTO ext_exercise (id, exercise) VALUES (31, 'Cycling');
INSERT INTO ext_exercise (id, exercise) VALUES (32, 'Push Up');

-- Query to check the data
SELECT * FROM set2_bmi;
SELECT * FROM set2_goals;
SELECT * FROM set3_daily;
SELECT * FROM set3_weekly;
SELECT * FROM set1_gym;
SELECT * FROM set1_intensity;
SELECT * FROM set1_focus;
SELECT * FROM ext_exercise;