# Python Principles

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