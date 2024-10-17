# workout_logger

# A simple workout logging command-line application built with Python and SQLite3, allowing users to log their workouts with details such as exercise, weight, reps, sets, and store them in an SQLite database.

# The workouts are automatically categorized based on the rep range, with the categories being:
#    Strength
#    Hypertrophy
#    Endurance

# Features 
- Log workouts: with exercise name, weight, reps, sets, and date.
- Automatic categorization: of workouts based on reps:
  - Strength: ≤ 5 reps
  - Hypertrophy: 6–12 reps
  - Endurance: ≥ 13 reps
- Store workouts: persistently in an SQLite database.
- View and manage workout logs: for progress tracking.

# How to use
Clone the repository through git by opening your terminal:
BASH:
git clone https://github.com/YOUR_USERNAME/workout_logger.git

BASH:
cd workout-logger

BASH:
pip install -r requirements.txt

BASH:
python main.py
