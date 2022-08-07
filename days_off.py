# Determining days off
# Min last 14 = 2
# Min last 28 = 8

import datetime


# Function to calculate off days in previous consecutive 14 days and 28 days
# Takes the raw dataframe as input argument
def days_off(data):
    i = 0               #start index
    off_days14 = []     #hold no. of days off in previous 14 days
    off_days28 = []     #hold no. of days off in previous 28 days
    last14 = []         #hold dates of last 14 days
    last28 = []         #hold dates of last 28 days

    for day in data['Date']:

        # Append this day to the last14 and last28 containers
        last14.append(day)
        last28.append(day)

        # If date span in last 14 container is not more than 14
        # Off days is difference between 14 and length of the last14 list
        # Record this to the off_days14 list
        if (last14[-1] - last14[0]).days <= 14:
            off_days14.append(14 - len(last14))

        # If date span in last 14 container exceeds 14
        # Remove the date at index 0 of last14 container
        # Repeat until datespan is not more than 14
        # Off days is difference between 14 and length of the last14 list
        # Record this to the off_days14 list
        else:
            while (last14[-1] - last14[0]).days > 14:
                del (last14[0])
            off_days14.append(14 - len(last14))

        # For off days in last 28 days, similar process to last 14 days is used
        if (last28[-1] - last28[0]).days <= 28:
            off_days28.append(28 - len(last28))
        else:
            while (last28[-1] - last28[0]).days > 28:
                del (last28[0])
            off_days28.append(14 - len(last14))

        i += 1 #next index

    #Creating new columns in the dataframe that contain the off days info
    data['Off Days Last 14'] = off_days14
    data['Off Days Last 28'] = off_days28
