# Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid. validBraces should return true if the string is valid, and false if it's invalid.
# This Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets, and open and closed curly braces. Thanks to @arnedag for the idea!
# All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

def validBraces(string):
    braces = { '(': ')', '[': ']', '{': '}' }
    list = []
    for char in string:
        c = braces.get(char)
        if c:
            list.append(c)
        elif not list or list.pop() != char:
            return False
    return not list