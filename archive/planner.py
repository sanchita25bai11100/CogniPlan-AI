This file contains the logic for generating a study timetable. It allocates study hours to different subjects based on their difficulty level using a rule-based approach.
# planner.py
# Generates a study timetable based on subjects and difficulty

def generate_schedule(subjects, hours, difficulty):
    schedule = {}

    # Calculate total difficulty weight
    total_weight = sum(difficulty.values())

    for subject in subjects:
        # Allocate hours based on difficulty
        weight = difficulty[subject] / total_weight
        allocated_time = round(weight * hours)

        schedule[subject] = allocated_time

    return schedule
