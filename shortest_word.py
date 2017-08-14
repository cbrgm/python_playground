# x Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
# test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)

def find_short(s):
    arr = s.split(" ")
    length = 99
    
    for word in arr:
        if length > len(word):
            length = len(word)
    
    return length