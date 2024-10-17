from datetime import date
import sqlite3

#Creating a database and table to store data
def create_table(db_name):
    '''
        This function creates a new SQLite database table if it doesn' already exist

        Parameters:
            db_name (str): name of the database

        A table will be create with the table name of workouts and it will sotre:
            id: Primary key
            date: the date of the workout
            exercise: the name of the exercise
            weight: The weigh used in pounds
            reps: reps preformed
            sets: sets preformed
            category: The workout category (Strenght, Hypertrophy, Endurance)
    '''

    con = sqlite3.connect(db_name)
    cur = con.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS workouts
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL, 
                exercise TEXT NOT NULL, 
                weight REAL NOT NULL, 
                reps INTEGER NOT NULL, 
                sets INTEGER NOT NULL, 
                category TEXT NOT NULL
                )
                ''')
    
    # commit and close the connection
    con.commit()
    con.close()

# Inserting Data into database
def insert_workout(db_name, date, exercise, weight, reps, sets, category):

    '''
        This function will insert the data into the table

        Parameters:
            db_name: name of the database
             date: the date of the workout
            exercise: the name of the exercise
            weight: The weigh used in pounds
            reps: reps preformed
            sets: sets preformed
            category: The workout category (Strenght, Hypertrophy, Endurance)
    
    '''
    
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    cur.execute(
        '''
        INSERT INTO workouts (date, exercise, weight, reps, sets, category)
        VALUES(?, ?, ?, ?, ?, ?)
        ''',
        (date, exercise, weight, reps, sets, category)
    )

    # commit and close the connection
    con.commit()
    con.close()

# categorizing the workout into strenght, hypertrophy or endurance based on the reps 
def categorize_workout(reps):
    
    '''
        This function is used to categorize the workout based on the reps 

        Parameters:
            reps(int): the reps preformed in the workout

        returns:
            str: workout category (Strenght, hypertrophy, Endurance)
    '''


    if reps <= 5:
        return "Strenght"
    elif 6 <= reps <= 12:
        return "Hypertrophy"
    else:
        return "Endurance"

# main menu for users to enter their workouts
def menu():

    '''
        This is the menu where the user will input their workout details

        returns:
            tuple: return a tuple containing the workout details
    '''

    print("\n--- Enter Workout Details ---")
    exercise = input("Enter Exercise: ")
    weight = int(input("Weight for " + exercise + " (lbs): "))
    reps = int(input("Number of reps: "))
    sets = int(input("Number of sets: "))
    workout_date = input("Date (YYYY-MM-DD) or leave blank for today: ")

    if workout_date == "":
        workout_date = date.today().strftime("%Y-%m-%d")

    # Categorze the workout based on reps
    category = categorize_workout(reps)

    return workout_date, exercise, weight, reps, sets, category


def main():
    """
    The main function that runs the Gym Workout Logger

    It initializes the SQLite database, allows the user to log workouts,
    and prompts the user if they wish to log additional workouts.
    """

    db_name = 'workout_log.db'


    # Creates the workouts table 
    create_table(db_name)

    print("Welcome to the Gym Workout Logger!")

    # looping to allow the user to input multiple workouts
    while True:
        user_workouts = menu()
        if user_workouts:
            workout_date, exercise, weight, reps, sets, category = user_workouts
        
        # Inserting data into the database
        insert_workout(db_name,workout_date, exercise, weight, reps, sets, category)

        # Asking the user if they want to log more workouts
        keep_logging = input("Log another workout? (y/n): ").strip().lower()

        if keep_logging == 'n':
            print("Workout Saved")
            print("Thank you for using the Gym Workout Logger")
            break




if __name__ == "__main__":
    main()
