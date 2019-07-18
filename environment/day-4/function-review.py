# def function_name(parameters, here):
#     internal code
#     return return_value

# 1. Write a function that checks to see if a given year is a leap year, by replacing "pass" with your own code, and returns either the boolean value True or False.
def is_leap_year(year):
    if (year%100)==0:
        return (year%400)==0
    else:
        return (year%4)==0
        
print(is_leap_year(2008))