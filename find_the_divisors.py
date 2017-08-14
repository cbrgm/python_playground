# Create a function named divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime'

def divisors(integer):
    result = []
    
    for int in range(2,integer):
        if integer % int == 0:
            result.append(int)
    
    if len(result) == 0:
        return str(integer) + " is prime"
    else:
        return result