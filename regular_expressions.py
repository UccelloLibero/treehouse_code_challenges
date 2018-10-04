#Write a function named first_number that takes a string as an argument. The function should search, with a regular expression, the first number in the string and return the match object.

import re

def first_number(str):
    return re.search(r'\d', str)

#Now, write a function named numbers() that takes two arguments: a count as an integer and a string. Return an re.search for exactly count numbers in the string. Remember, you can multiply strings and integers to create your pattern.

#For example: r"\w" * 5 would create r"\w\w\w\w\w".

def numbers(c_int, c_str):
    return re.search(r'\d' * c_int, c_str)


#Create a function named phone_numbers that takes a string and returns all of the phone numbers in the string using re.findall(). The phone numbers will all be in the format 555-555-5555.

import re


def phone_numbers(str):
    return re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', str)

#Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(a_c, a_s):
    a_c = int(a_c)
    r_str = re.findall(r'\w+' * a_c, a_s)
    return r_str


#Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.

def find_emails(string):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', string)

#Create a variable named good_numbers that is an re.findall() where the pattern matches anything in string except the numbers 5, 6, and 7.

import re

string = '1234567890'

good_numbers = re.findall(r'[^567]', string)

#Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.

import re

string = 'Perotto, Pier Giorgio'

names = re.match(r"""
    ([\w ]*),\s
    ([\w\s\w]*)
""", string, re.X)

#Create a new variable named contacts that is an re.search() where the pattern catches the email address and phone number from string. Name the email pattern email and the phone number pattern phone. The comma and spaces * should not* be part of the groups.

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r"""
    (?P<email>[-\w\d.+]+@[-\w\d.]+)
    ,\s
    (?P<phone>\d{3}-\d{3}-\d{4})
""", string, re.X|re.M)


#Great! Now, make a new variable, twitters that is an re.search() where the pattern catches the Twitter handle for a person. Remember to mark it as being at the end of the string. You'll also want to use the re.MULTILINE flag.

twitters = re.search(r'''
    (?P<twitter>@[^t][\w\d]+)
''', string, re.X|re.M)


#Create a variable named players that is an re.search() or re.match() to capture three groups: last_name, first_name, and score. It should include re.MULTILINE.

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    (?P<last_name>[-\w ]*)
    ,\s
    (?P<first_name>[-\w ]*)
    :\s
    (?P<score>\d{2})
''', string, re.X|re.M)

# Wow! OK, now, create a class named Player that has those same three attributes, last_name, first_name, and score. I should be able to set them through __init__.

class Player():
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score
