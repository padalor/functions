'''
@author: amayamunoz
'''
from Tools.demo.ss1 import colnum2name

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by 
calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract_two_numbers(num2, num1):
    differenceOfTwoNumbers = num2 - num1
    return differenceOfTwoNumbers 
   
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def divide_num_by_two(num1, num2):
    finalnumber = ((num1/2)*77) + 10000
    return finalnumber

    
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def check(num1, num2):
    if num1 == num2:
        return "true"
    else:
        return "false"
    
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def check_greater(num1,num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num1
    else:
        return num2 

#5) Define a function that takes in two words and returns a string that contains both words combined.

#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def take_in_three_num(num1, num2, num3):
    if num1 == num2 or num1 == num3:
        return "true"
    else: 
        return "false"

#7) Define a function that prints your name.
def name(name):
    return name
name = ""
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."

#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.

'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.