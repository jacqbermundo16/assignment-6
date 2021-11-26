#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

def question1():
    # import 2 random numbers
    _addend1 = int(random.randint(0,99))
    _addend2 = int(random.randint(0,99))
    # get the sum
    _sum1 = int(_addend1 + _addend2)
    # return values
    return _addend1, _addend2, _sum1
    
# ask question 1
def askQuestion1(addend1f, addend2f):
    _ans1 = int(input(f"1. {addend1f} + {addend2f} = "))
    return _ans1

# check if answer #1 is true
def checkAnswer1(ans1f, sum1f):
    if ans1f == sum1f:
        _check1 = int(1)
        return _check1
    # if not
    else:
        _check1 = int(0)
        return _check1

# repeaat th steps above
# create a function that adds all the points 
# display the results
print("Addition Quiz")
addend1, addend2, sum1 = question1()
ans1 = askQuestion1(addend1, addend2)
check1 = checkAnswer1(ans1, sum1)
# these re to checkif the program works well
print(sum1)
print(ans1)
print(check1)