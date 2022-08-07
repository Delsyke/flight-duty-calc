# Calculating rest times Min=12
import datetime


# Function to calculate rest hours for each day
# Takes the raw dataframe as input argument
def rest(data):
    i = 0           #start index
    rests = [24]    #to hold rest hours for each day, initial rest is 24 hours

    for _ in range(len(data)):
        date_off = data['Date'][i] #date when duty ended
        time_off = data['Off Duty'][i]  #time when duty ended for that date
        date_on = data['Date'][i + 1] #date when next duty started
        time_on = data['On Duty'][i + 1] #time when next duty started


        # Adding the dates and times together and converting into timedeltas
        off_duty = date_off + datetime.timedelta(hours=time_off.hour, minutes=time_off.minute)
        on_duty = date_on + datetime.timedelta(hours=time_on.hour, minutes=time_on.minute)

        resting = (on_duty - off_duty).total_seconds()
        rests.append(round(resting / 3600, 1))

        i += 1 #next index

        # Preventing index out of limit error
        if i >= len(data) - 1:
            break

    # Create new column in the dataframe with rest periods for each day.
    data['Rest'] = rests
