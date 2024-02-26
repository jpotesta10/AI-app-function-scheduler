import schedule
import time

def your_function():
    # Define the functionality you want to run at a specific time
    print("Your function is running 3 times every day at a set time with a 4.5-minute interval.")

# Set the desired time to start the daily runs
start_time = "22:39"

# Set the number of times to run daily
daily_runs = 3
run_count = 0

# Schedule the function to run every day at the specified time
schedule.every().day.at(start_time).do(your_function)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    
    # Check if it's time to start the daily runs
    current_time = time.strftime("%H:%M")
    if current_time == start_time and run_count < daily_runs:
        for _ in range(daily_runs):
            your_function()
            time.sleep(10)  # Sleep for 10 seconds (convert minutes to seconds if needed)
            run_count += 1

