# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# steps
# 1 ask 4 numbers
def askNumbers():
    _first = int(input('First Number:'))
    _second = int(input('Second Number: '))
    _third =  int(input('Third Number: ')) 
    _fourth= int(input('Fourth Number: '))
    return _first, _second, _third, _fourth


# determine the highest numberof the four
# determine the second highest
# determine the third highest
# determine the lowest of the four
# print the results from the highest number to the lowest
a,  b, c, d = askNumbers()
