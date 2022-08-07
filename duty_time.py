# Calculating daily duty times. Max = 10
import datetime


# Function to calculate duty times

def duty(data):

    # Initialize conditions
    i = 0               #start index
    duty_times = []     #list to hold the duty time for each day

    for _ in range(len(data)):
        on = data['On Duty'][i]         #time on duty
        off = data['Off Duty'][i]       #time off duty

        # Convert the times to timedeltas
        t_on_d = datetime.timedelta(hours=on.hour, minutes=on.minute)
        t_off_d = datetime.timedelta(hours=off.hour, minutes=off.minute)

        # Get time differences and add to the duty_times list
        duty_time = t_off_d - t_on_d
        seconds = (duty_time.total_seconds())
        duty_times.append(round(seconds / 3600, 1))

        i += 1

    # Finally create a new colum in the dataframe containing duty time info
    data['Duty Time'] = duty_times
