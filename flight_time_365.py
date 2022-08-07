# Calculating flight times last 365 days. Max = 1000
import datetime


# Function to calculate cumulative flight time in previous 365 consecutive days
# Takes the raw dataframe as input argument
def flight_365(data):

    # Initial conditions and containers
    i = 0               #start index
    hours = []          #to hold flight hours for each day entered
    ftlast365 = []      #to hold sum of flight hours in the preceding 365 days
    last365 = []        #to hold the dates of last 365 days

    for day in data['Date']:

        # Append this day to the last365 container
        # Append the flight hours for that day to the hours container
        last365.append(day)
        hours.append(data['Flight Time'][i])

        # If date span is not more than 365 days,
        # Sum the corresponding flight time hours
        # Then record this as most recent entry in ftlast365
        if (last365[-1] - last365[0]).days <= 365:
            ftlast365.append(sum(hours))

        # If datespan exceeds 365 days
        # Remove the date at index 0 of last365 container
        # Also remove the correponding entry in hours list
        # Repeat until datespan is equal or less to 365 days
        # Now sum the hours list to get total flight time in last 365 days
        # Then record this as most recent entry in ftlast365
        else:
            while (last365[-1] - last365[0]).days > 365:
                del last365[0]
                del hours[0]
            ftlast365.append(sum(hours))

        i += 1 #next index

    # Create new column in the dataframe with cumulative flight times
    # over the preceding consecutive 365 days (for each date)
    data['FT Last 365'] = ftlast365

