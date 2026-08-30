This module provides a focus mode feature. It starts a timer-based session during which the user is encouraged to stay focused and avoid distractions.
# blocker.py

import time

def start_focus_session(minutes):
    """
    Starts a focus session where user should avoid distractions
    """

    print("\n--- Focus Mode Activated ---")
    print("Stay focused. Do not use phone or social media!\n")

    for i in range(minutes):
        print(f"Minute {i+1} in progress...")
        
        # Wait for 60 seconds
        time.sleep(60)

    print("\nFocus session completed! Good job 🎉")
