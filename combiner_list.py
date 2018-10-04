# Combiner List: Create a function named combiner that takes a single argument, which will be a list made up of strings and numbers.

# Return a single string that is a combination of all of the strings in the list and then the sum of all of the numbers. For example, with the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2". Be sure to use isinstance to solve this as I might try to trick you.

def combiner(list_1):
    strings = ""
    nums = 0
    for items in list_1:
        if isinstance (items, str):
            strings += items
        elif isinstance (items, (int, float)):
            nums += items
    combo_string = strings + str(nums)
    return combo_string
