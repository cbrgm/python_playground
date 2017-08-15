'''
Write a function named firstNonRepeatingCharacter that takes a string input, and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
'''
def first_non_repeating_letter(string):

    chars = []
    
    for char in string:
        if count_char(char.lower(),string.lower()) == 1:
            return char
    
    return ""

def count_char(char, string):
    counter = 0
    for letter in string:
        if letter == char:
            counter += 1
    return counter