from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days = int(input("Enter number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future_date)
    except ValueError:
        print("Invalid input. Please enter an integer.")