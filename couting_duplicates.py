# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
def duplicate_count(text):
    text = text.lower()
    occurences = 0
    maps = {}
    
    for char in text:
        if char not in maps:
            maps[char] = 1
        else:
            maps[char] += 1
    
    for key in maps:
        if maps[key] > 1:
          occurences += 1
    
    return occurences