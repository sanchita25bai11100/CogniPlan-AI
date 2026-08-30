This module updates the study plan based on user performance. It increases or decreases study time depending on whether the user completed the assigned tasks.
# adaptive.py

def update_schedule(schedule):
    updated_schedule = {}

    print("\n--- Updating Schedule Based on Performance ---")

    for subject in schedule:
        status = input(f"Did you complete {subject}? (yes/no): ")

        if status.lower() == "no":
            # Increase time if not completed
            updated_schedule[subject] = schedule[subject] + 1
        else:
            # Decrease time if completed (minimum 1 hour)
            updated_schedule[subject] = max(1, schedule[subject] - 1)

    return updated_schedule
