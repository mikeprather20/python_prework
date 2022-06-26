#QUESTIONS:

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
#The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    """Simple User Greeting"""
    print("Hello, " + user_name.title() + "!")
user_name = input('Please Enter Username:' + " ")

hello_name(user_name)


print("\n")
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    """Print Only Odds"""
    for num in range (1,101):
        if num % 2 != 0:
            print(num)

first_odds()


print("\n")
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    """Maximum Value"""
    max = a_list[0] 
    for index in range(len(a_list)): 
        if a_list[index] > max:
            max = a_list[index]
    return max

a_list = [3, 55, 130, 105, 68]

print(max_num_in_list(a_list))


print("\n")
#Question 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
#The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    """What Year Is A Leap Year"""

    if (a_year % 400 == 0):
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

a_year= int(input('Please enter a year to check for a T/F leap year:' + " "))

print(is_leap_year(a_year))


print("\n")
#Question 5
#Write a function to check to see if all numbers in the list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    """List Of Consecutive Numbers"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


# double check code

a_list = [1,2,3,4,5,6,7] #should be true
print(is_consecutive(a_list))

a_list = [1,2,3,4,6,7] #should be false
print(is_consecutive(a_list))
