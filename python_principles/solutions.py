# Python Principles

# establishing environment
import math

"""
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
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

"""
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t". Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test". If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
"""

def add_dots(string):
    string = string.replace('','.')
    string = string[1:-1]
    return string

def remove_dots(string):
    string = string.replace('.', '')
    return string

"""
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens.
"""

def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False
    
"""
Write a function that takes a list of lists and flattens it into a one-dimensional list. Name your function flatten. It should take a single parameter and return a list.
"""

def flatten(l_of_lists):
    flat_list = []
    for l in l_of_lists:
        for i in l:
            flat_list.append(i)
    return flat_list

"""
Define a function named largest_difference that takes a list of numbers as its only parameter. Your function should compute and return the difference between the largest and smallest number in the list.
"""

def largest_difference(numbers):
    return max(numbers) - min(numbers)

"""
Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
"""

def div_3(num):
    return num % 3 == 0

"""
Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
"""

def get_row_col(coords):
    board_dict = {'A' : 0, 'B' : 1, 'C' : 2, '1' : 0, '2' : 1, '3' : 2}
    coords = list(coords)
    return (board_dict[coords[1]],board_dict[coords[0]])

"""
Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.
"""

def palindrome(word):
    return word[::-1] == word

"""
Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
"""
def up_down(num):
    return ((num - 1), (num + 1))

"""
Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the largest number of consecutive 0's
"""
def consecutive_zeros(string):
    return max([len(x) for x in string.split('1')])

"""
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
"""

def all_equal(l):
    if len(set(l)) > 1:
        return False
    else:
        return True

"""
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
"""

def triple_and(a, b, c):
    return a and b and c

"""
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string. For example, the call convert([1, 2, 3]) should return ["1", "2", "3"]. What makes this tricky is that your function body must only contain a single line of code.
"""

def convert(l):
    return [str(num) for num in l]

"""
The built-in zip function "zips" two lists. Write your own implementation of this function. Define a function named zap. The function takes two parameters, a and b. These are lists. Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b. You may assume a and b have equal lengths.
"""

def zap(a, b):
    zap_list = []
    for i in range(0,len(a)):
        zap_list.append((a[i], b[i]))
    return zap_list

"""
Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"

the code must contain the : symbol
otherwise return "missing :"

the code must contain ( and ) for the parameter list
otherwise return "missing paren"

the code must not contain ()
otherwise return "missing param"

the code must contain four spaces for indentation
otherwise return "missing indent"

the code must contain validate
otherwise return "wrong name"

the code must contain a return statement
otherwise return "missing return"

If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""

def validate(s):
    p = '(' + ')'
    if "def" not in s:
        return "missing def"
    elif ":" not in s:
        return "missing :"
    elif "(" not in s or ")" not in s:
        return "missing paren"
    elif p in s:
        return "missing param"
    elif "    " not in s:
        return "missing indent"
    elif "validate" not in s:
        return "wrong name"
    elif "return" not in s:
        return "missing return"
    else:
        return True
    
"""
