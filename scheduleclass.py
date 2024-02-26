#Some features of Quantum Forge must run at set times each day.  
#This includes the Trend URL List feature and Generate Post feature (there are a short list of others).
#You can modify the 'timed.py' code to run a method of a class instead of a standalone function. 
#Here's an example of how you can schedule the execution of a method within a class:

import schedule
import time

class YourClass:
    def __init__(self):
        self.run_count = 0

    def your_method(self):
        # Define the functionality you want to run at a specific time
        print("Your method is running 3 times every day at a set time with a 4.5-minute interval.")

# Set the desired time to start the daily runs
start_time = "12:00"

# Set the number of times to run daily
daily_runs = 3

# Create an instance of YourClass
your_instance = YourClass()

# Schedule the method to run every day at the specified time
schedule.every().day.at(start_time).do(your_instance.your_method)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    
    # Check if it's time to start the daily runs
    current_time = time.strftime("%H:%M")
    if current_time == start_time and your_instance.run_count < daily_runs:
        for _ in range(daily_runs):
            your_instance.your_method()
            time.sleep(4.5 * 60)  # Sleep for 4.5 minutes (converted to seconds)
            your_instance.run_count += 1

#In this example, I've created a class YourClass, and the your_method method within the class is scheduled to run using schedule.every().day.at(start_time).do(your_instance.your_method).

#Adjust the class and method names as needed for your specific implementation.