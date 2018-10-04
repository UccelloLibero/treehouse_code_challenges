#Write a function named time_tango that takes a date and a time. It should combine them into a datetime and return it.

import datetime

def time_tango(date, time):
    return datetime.datetime.combine(date, time)



# Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.


import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(int):
    return starter + datetime.timedelta(hours=int)
