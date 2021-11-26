#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

def question1():
    _addend1 = int(random.randint(0,99))
    _addend2 = int(random.randint(0,99))
    _sum1 = int(_addend1 + _addend2)
    return _addend1, _addend2, _sum1
    
def askQuestion1(addend1f, addend2f):
    _ans1 = int(input(f"1. {addend1f} + {addend2f} = "))
    return _ans1


print("Addition Quiz")
addend1, addend2, sum1 = question1()
ans1 = askQuestion1(addend1, addend2)
print(sum1)
print(ans1)