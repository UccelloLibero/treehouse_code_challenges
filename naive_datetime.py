#starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime instead and assign this converted datetime to the variable local.

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)
pacific = pytz.timezone("US/Pacific")
local = pacific.localize(starter)

#Now create a variable named pytz_string by using strftime with the local datetime. Use the fmt string for the formatting.
pytz_string = local.strftime(fmt)


#Create a function named to_timezone that takes a timezone name as a string. Convert starter to that timezone using pytz's timezones and return the new datetime.

import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(tz_string):
    tz_string = pytz.timezone(tz_string)
    return starter.astimezone(tz_string)
