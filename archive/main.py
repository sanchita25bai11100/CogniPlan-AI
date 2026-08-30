This is the main file of the project. It connects all modules and provides a menu-based interface for the user to interact with the system. It handles user input and calls different functions like generating the study plan, updating it, evaluating answers, and starting focus mode.

print("Welcome to AI Study Planner")
from planner import generate_schedule
from adaptive import update_schedule
from evaluator import evaluate_answer
from blocker import start_focus_session

def main():
    schedule = {}

    while True:
        print("\n===== AI STUDY PLANNER =====")
        print("1. Create Study Plan")
        print("2. Update Plan")
        print("3. Evaluate Answer")
        print("4. Start Focus Mode")
        print("5. Exit")

        choice = input("Enter your choice: ")

        #  OPTION 1: Create Plan
        if choice == "1":
            subjects = input("Enter subjects (comma separated): ").split(",")
            subjects = [sub.strip() for sub in subjects]

            hours = int(input("Enter total study hours: "))

            difficulty = {}
            for sub in subjects:
                level = int(input(f"Enter difficulty for {sub} (1-5): "))
                difficulty[sub] = level

            schedule = generate_schedule(subjects, hours, difficulty)

            print("\n--- Your Study Plan ---")
            for sub, hr in schedule.items():
                print(f"{sub}: {hr} hours")

        #  OPTION 2: Update Plan
        elif choice == "2":
            if not schedule:
                print("No plan found. Create one first.")
            else:
                schedule = update_schedule(schedule)

                print("\n--- Updated Study Plan ---")
                for sub, hr in schedule.items():
                    print(f"{sub}: {hr} hours")

        #  OPTION 3: Evaluate Answer
        elif choice == "3":
            student = input("Enter your answer: ")
            model = input("Enter correct answer: ")

            score = evaluate_answer(student, model)
            print(f"Your Score: {score} / 10")

        #  OPTION 4: Focus Mode
        elif choice == "4":
            mins = int(input("Enter duration in minutes: "))
            start_focus_session(mins)

        #  EXIT
        elif choice == "5":
            print("Exiting... Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")

# Run program
main()
