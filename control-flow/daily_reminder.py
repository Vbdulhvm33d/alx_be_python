#defining the variables
task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
#deining the match expression line
match priority :
    case 1 :
        if priority is high and time_bound is yes:
            print(f"Reminder: {task} is is a high priority task that requires immediate attention today!")
        elif priority is high and time_bound is no:
            print(f"Reminder: {task} is an B1 task that can be done at your earliest convinience!")
    case 2 :
        if priority is medium and time_bound is yes:
            print(f"Reminder: {task} is is a mid priority task that should be done after the A1 tasks!")
        elif priority is medium and time_bound is no:
            print(f"Reminder: {task} is a mid priority task that should be done after the C1 tasks!")
    case 3 :
        if priority is low and time_bound is yes:
            print(f"Reminder: {task} is a low priority task that should be done before the B2 tasks!")
        elif priority is low and time_bound is no:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time. ")