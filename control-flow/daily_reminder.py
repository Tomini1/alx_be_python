def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task."
        case "medium":
            reminder = f"Note: '{task}' is a medium priority task. Plan accordingly."
        case "low": 
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level entered." 

    if time_bound == "yes":
        reminder += "It requires immediate attention today!"
        print(reminder)

daily_reminder()

