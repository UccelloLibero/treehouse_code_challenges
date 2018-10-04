# Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years". This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine(int, str_timedelta):
    if str_timedelta == "minutes":
        return starter + datetime.timedelta(minutes = int)
    elif str_timedelta == "hours":
        return starter + datetime.timedelta(hours = int)
    elif str_timedelta == "days":
        return starter + datetime.timedelta(days = int)
    elif str_timedelta == "years":
        return starter + datetime.timedelta(days = int * 365)
