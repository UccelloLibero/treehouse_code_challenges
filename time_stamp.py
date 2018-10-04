# Create a function named timestamp_oldest that takes any number of POSIX timestamp arguments. Return the oldest one as a datetime object.
# Remember, POSIX timestamps are floats and lists have a .sort() method.

# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

import datetime

def timestamp_oldest(*args):
    return datetime.datetime.fromtimestamp(min(args))



# Create a variable named moscow that holds a datetime.timezone object at +4 hours.
import datetime

moscow = datetime.timezone(datetime.timedelta(hours=+4))

# Now create a timezone variable named pacific that holds a timezone at UTC-08:00.

pacific = datetime.timezone(datetime.timedelta(hours=-8))

# Finally, make a third variable named india that hold's a timezone at UTC+05:30.

india = datetime.timezone(datetime.timedelta(hours=+5, minutes=30))

# naive is a datetime with no timezone.
# Create a new timezone for US/Pacific, which is 8 hours behind UTC (UTC-08:00).
# Then make a new variable named hill_valley that is naive with its tzinfo attribute replaced with the US/Pacific timezone you made.

import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)

pacific = datetime.timezone(datetime.timedelta(hours=-8))

hill_valley = datetime.datetime(2015, 10, 22, 5, tzinfo=pacific)

# Great, but replace just sets the timezone, it doesn't move the datetime to the new timezone. Let's move one.
# Make a new timezone that is UTC+01:00.
# Create a new variable named paris that uses your new timezone and the astimezone method to change hill_valley to the new timezone.

europa = datetime.timezone(datetime.timedelta(hours=+1))

paris = hill_valley.astimezone(europa)


#starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime instead and assign this converted datetime to the variable local.
