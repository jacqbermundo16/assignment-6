# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# steps
# 1 ask 4 numbers
def askNumbers():
    _first = float(input('First Number:'))
    _second = float(input('Second Number: '))
    _third =  float(input('Third Number: ')) 
    _fourth= float(input('Fourth Number: '))
    return _first, _second, _third, _fourth

# determine the highest number of the four
def arrangeNumbers(_a, _b, _c, _d):
    # if a is the highest of four
    if _a > _b and _a > _c and _a > _d:
        # if the second highest is b
        if _b > _c and _b > _d :
            # if the order will be-b-c-d
            if _c > _d:
                print(f"{_a}, {_b}, {_c}, {_d}")
            # if the order will be a-b-c-d
            else:
                print (f"{_a}, {_b}, {_d}, {_c}")

        # if the second highest is c 
        elif _c > _b and _c > _d :
            #if the order will be a-c-b-d
            if _b > _d:
                print(f"{_a}, {_c}, {_b}, {_d}") 
            #if the order will be a-c-d-b
            else:
                print(f"{_a}, {_c}, {_d}, {_b}") 

        # if the second highest is d
        
    

    else:
        print('others')
        

a, b, c, d = askNumbers()
highest = arrangeNumbers(a, b, c, d)
print(highest)
