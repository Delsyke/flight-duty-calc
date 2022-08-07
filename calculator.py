import datetime
import days_off
import duty_time
import duty_time_28
import flight_time_28
import flight_time_365
import rest_time
import styling


book = 'test.xlsx' #path to where output file will be saved


# Calculating the required figures and creating an excel workbook
# Takes the raw dataframe as input argument
def calculator(data):

    # use the functions from the imported modules to process the dataframe
    duty_time.duty(data)
    duty_time_28.duty_28(data)
    flight_time_28.flight_28(data)
    flight_time_365.flight_365(data)
    rest_time.rest(data)
    days_off.days_off(data)

    date_str = [] #initialize container to hold dates as strings

    # Format the dates in day column into strings and add to date_str list
    for day in data['Date']:
        date_str.append(datetime.datetime.strftime(day, '%d %b %Y'))

    # Create new column in the dataframe with the string formatted dates
    # And make this column the index of the dataframe
    data['Date'] = date_str
    data.set_index('Date', drop=True, inplace=True)

    # Save the dataframe as excel file and style it
    data.to_excel(book, 'Sheet1')
    styling.style(book)
