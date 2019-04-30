# function with no statement
def func_no_statement():
    pass

#function with no return
def say_hello(name):
    print('Hello', name)

# function that triples a number
def triple(x):
    return x * 3

# function that adds two numbers
def add(x, y):
    return x + y

# function that captures arbitrary number of arguments
def output(*args):
    print(args)

# function with default parameter value
def incremet(x, y=1):
    return x + y

########################################################
# function that finds the max of three numbers
def max_of_three_1(x, y, z):
    if (x > y and x > z):
        return x
    elif (y > z):
        return y
    else:
        return z

# function that finds the max of two numbers
def max_of_two_1(x, y):
    if x > y:
        return x
    else:
        return y

# function that finds the max of two numbers 
def max_of_two_2(x, y):
    return x if x > y else y

# function that finds the max of two numbers
def max_of_three_2(x, y, z):
    return max_of_two_2(max_of_two_2(x, y), z)

# function that returns the sum of a list of numbers
def sum(vals):
    result = 0
    for val in vals:
        result = result + val
    return result

# function that finds the product of a list of numbers
def mult(vals):
    result = 1
    for i in vals:
        result = result * i
    return result

# function that revarse the text in a string
def reverse_string(text):
    result = []
    for c in text:
        result.insert(0, c)
    return ''.join(result)

def reverse_string_2(text):
    return text[::-1]

def reverse_string_3(text):
    result = ''
    for c in text:
        result = c + result
    return result

# function that finds the n!
def factorial(n):
    result = 1
    while n > 0:
        result = result * n
        n = n - 1
    return result

# function that checks if a number is within a given range
def check_range(n, start, stop):
    return True if n > start and n < stop else False

# function that counts the number of upper case and lowercase letters in a text
def count_upper_lower_case(text):
    upper_count = 0
    lower_count = 0
    for c in text:
        if c == ' ':
            pass
        elif c.isupper():
            upper_count = upper_count + 1
        else:
            lower_count = lower_count + 1
    return (upper_count, lower_count)

##########################################################
print(sum( [8, 2, 3, 0, 7] ))
print(mult( [8, 2, 3, -1, 7] ))
print(reverse_string_3('1234abcd'))
print(factorial(5))
print(check_range(18, 6, 12))
print(count_upper_lower_case('The quick Brow Fox'))