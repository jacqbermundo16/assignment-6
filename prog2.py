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

# repeat the steps above

def question2():
    # import 2 random numbers
    _addend1_2 = int(random.randint(0,99))
    _addend2_2 = int(random.randint(0,99))
    # get the sum
    _sum2 = int(_addend1_2 + _addend2_2)
    # return values
    return _addend1_2, _addend2_2, _sum2

# ask question 2
def askQuestion2(addend1_2f, addend2_2f):
    _ans2 = int(input(f"2. {addend1_2f} + {addend2_2f} = "))
    return _ans2

# check if answer #2 is true
def checkAnswer2(ans2f, sum2f):
    if ans2f == sum2f:
        _check2 = int(1)
        return _check2
    # if not
    else:
        _check2 = int(0)
        return _check2

def question3():
    # import 2 random numbers
    _addend1_3 = int(random.randint(0,99))
    _addend2_3 = int(random.randint(0,99))
    # get the sum
    _sum3 = int(_addend1_3 + _addend2_3)
    # return values
    return _addend1_3, _addend2_3, _sum3

# ask question 3
def askQuestion3(addend1_3f, addend2_3f):
    _ans3 = int(input(f"3. {addend1_3f} + {addend2_3f} = "))
    return _ans3

# check if answer #3 is true
def checkAnswer3(ans3f, sum3f):
    if ans3f == sum3f:
        _check3 = int(1)
        return _check3
    # if not
    else:
        _check3 = int(0)
        return _check3

def question4():
    # import 2 random numbers
    _addend1_4 = int(random.randint(0,99))
    _addend2_4 = int(random.randint(0,99))
    # get the sum
    _sum4 = int(_addend1_4 + _addend2_4)
    # return values
    return _addend1_4, _addend2_4, _sum4

# ask question 4
def askQuestion4(addend1_4f, addend2_4f):
    _ans4 = int(input(f"4. {addend1_4f} + {addend2_4f} = "))
    return _ans4

# check if answer #4 is true
def checkAnswer4(ans4f, sum4f):
    if ans4f == sum4f:
        _check4 = int(1)
        return _check4
    # if not
    else:
        _check4 = int(0)
        return _check4

def question5():
    # import 2 random numbers
    _addend1_5 = int(random.randint(0,99))
    _addend2_5 = int(random.randint(0,99))
    # get the sum
    _sum5 = int(_addend1_5 + _addend2_5)
    # return values
    return _addend1_5, _addend2_5, _sum5

# ask question 5
def askQuestion5(addend1_5f, addend2_5f):
    _ans5 = int(input(f"5. {addend1_5f} + {addend2_5f} = "))
    return _ans5

# check if answer #5 is true
def checkAnswer5(ans5f, sum5f):
    if ans5f == sum5f:
        _check5 = int(1)
        return _check5
    # if not
    else:
        _check5 = int(0)
        return _check5

def question6():
    # import 2 random numbers
    _addend1_6 = int(random.randint(0,99))
    _addend2_6 = int(random.randint(0,99))
    # get the sum
    _sum6 = int(_addend1_6 + _addend2_6)
    # return values
    return _addend1_6, _addend2_6, _sum6

# ask question 6
def askQuestion6(addend1_6f, addend2_6f):
    _ans6 = int(input(f"6. {addend1_6f} + {addend2_6f} = "))
    return _ans6

# check if answer #6 is true
def checkAnswer6(ans6f, sum6f):
    if ans6f == sum6f:
        _check6 = int(1)
        return _check6
    # if not
    else:
        _check6 = int(0)
        return _check6









# create a function that adds all the points 
# display the results
print("Addition Quiz")
addend1, addend2, sum1 = question1()
addend1_2, addend2_2, sum2 = question2()
addend1_3, addend2_3, sum3 = question3()
addend1_4, addend2_4, sum4 = question4()
addend1_5, addend2_5, sum5 = question5()
addend1_6, addend2_6, sum6 = question6()


ans1 = askQuestion1(addend1, addend2)
ans2 = askQuestion2(addend1_2, addend2_2)
ans3 = askQuestion3(addend1_3, addend2_3)
ans4 = askQuestion4(addend1_4, addend2_4)
ans5 = askQuestion5(addend1_5, addend2_5)
ans6 = askQuestion6(addend1_6, addend2_6)


check1 = checkAnswer1(ans1, sum1)
check2 = checkAnswer2(ans2, sum2)
check3 = checkAnswer3(ans3, sum3)
check4 = checkAnswer4(ans4, sum4)
check5 = checkAnswer5(ans5, sum5)
check6 = checkAnswer6(ans6, sum6)



# these re to checkif the program works well
print(sum1, ans1, check1)
print(sum2, ans2, check2)
print(sum3, ans3, check3)
print(sum4, ans4, check4)
print(sum5, ans5, check5)
print(sum6, ans6, check6)
