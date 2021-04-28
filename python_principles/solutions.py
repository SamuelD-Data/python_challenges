# Python Principles

# establishing environment
import math

"""
1) Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters. 
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes(word):
    capital_places = []
    for place, letter in enumerate(word):
        if letter == letter.upper():
            capital_places.append(place)
    return capital_places

"""
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

def mid(word):
    if len(word) % 2 == 0:
        return ""
    else:
        mid_pos = math.floor(len(word) / 2)
        return word[mid_pos]

"""
Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.
"""

def online_count(statuses):
    online_count = 0
    for x in statuses:
        if statuses[x] == 'online':
            online_count += 1
    return online_count

"""
Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, both inclusive, and return it.
"""

def random_number():
    return random.randint(1, 100)

"""
Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.
"""

def only_ints(p1, p2):
    if type(p1) == int and type(p2) == int:
        return True
    else:
        return False

"""
Define a function named double_letters that takes a single parameter. The parameter is a string. 
Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""

def double_letters(string):
    answer = False
    for place, letter in enumerate(string[:len(string)-1]):
        if letter == string[place + 1]:
            answer = True
    return answer