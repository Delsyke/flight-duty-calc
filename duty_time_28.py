import datetime


# Function to calculate cumulative duty time in previous consecutive 28 days
# Takes the raw dataframe as input argument
def duty_28(data):

    # Initial conditions and containers
    i = 0               #start index
    hours = []          #to hold duty hours for each day entered
    dtlast28 = []       #to hold sum of duty hours in the preceding 28 days
    last28 = []         #to hold the dates of last 28 days

    for day in data['Date']:

        # Append this day to the last28 container
        # Append the duty hours for that day to the hours container
        last28.append(day)
        hours.append(data['Duty Time'][i])

        # If date span is not more than 28 days,
        # Sum the corresponding duty time hours
        # Then record this as most recent entry in dtlast28
        if (last28[-1] - last28[0]).days <= 28:
            dtlast28.append(sum(hours))


        # If datespan exceeds 28 days
        # Remove the date at index 0 of last28 container
        # Also remove the correponding entry in hours list
        # Repeat until datespan is equal or less to 28 days
        # Now sum the hours list to get total duty time in last 28 days
        # Then record this as most recent entry in dtlast28
        else:
            while (last28[-1] - last28[0]).days > 28:
                del last28[0]
                del hours[0]
            dtlast28.append(sum(hours))

        i += 1      #next index

    # Create new column in the dataframe with cumulative duty times
    # over the preceding consecutive 28 days (for each date)
    data['DT Last 28'] = dtlast28