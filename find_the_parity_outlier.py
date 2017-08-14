# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

def find_outlier(integers):
    if integers[0] % 2:
        for value in integers:
            if value % 2 == 1:
                return value
    else:
        for value in integers:
            if value % 2 != 0:
                return value