# Python Principles

"""
1) Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters. 
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes2(word):
    capital_places = []
    for place, letter in enumerate(word):
        if letter == letter.upper():
            capital_places.append(place)
    return capital_places

"""

"""