# Your task is to write a function which returns the sum of following series upto nth term(parameter).

def series_sum(n):
    
    sum = 0
    
    for i in range(n):
        sum += 1/(1+(3*i))
        
    return format(sum, '.2f')
	
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()