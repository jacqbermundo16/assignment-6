# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# steps
# 1 ask 4 numbers
def askNumbers():
    _first = float(input('First Number: '))
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
            # if the order will be a-b-c-d
            if _c > _d:
                print(f"{_a}, {_b}, {_c}, {_d}")
            # if the order will be a-b-d-c
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
            # if the order will be a-d-b-c
            if _b > _c:
                print(f"{_a}, {_d}, {_b}, {_c}")
            # if the order will be a-d-c-b
            else:
                print(f"{_a}, {_d}, {_c}, {_b}")

    # if b is the highest number
    elif _b > _a and _b > _c and _b > _d :
        # if the second highest is a
        if _a > _c and _a > _d:
            # if the order will be b-a-c-d
            if _c > _d:
                print(f"{_b}, {_a}, {_c}, {_d}")
            # if the order will be b-a-d-c
            else:
                print(f"{_b}, {_a}, {_d}, {_c}")

            # if the second highest is c 
        elif _c > _a and _c > _d :
            #if the order will be b-c-a-d
            if _a > _d:
                print(f"{_b}, {_c}, {_a}, {_d}") 
            #if the order will be b-c-d-a
            else:
                print(f"{_b}, {_c}, {_d}, {_a}") 

        # if the second highest is d
        else:
            # if the order will be b-d-a-c
            if _a > _c:
                print(f"{_b}, {_d}, {_a}, {_c}")
            # if the order will be a-d-c-b
            else:
                print(f"{_b}, {_d}, {_c}, {_a}")
 
    # if c is the highest number 
    elif _c > _a and _c > _b and _c > _d :
        # if the second highest is a
        if _a > _b and _a > _d:
            # if the order will be c-a-b-d
            if _b > _d:
                print(f"{_c}, {_a}, {_b}, {_d}")
            # if the order will be c-a-d-b
            else:
                print(f"{_c}, {_a}, {_d}, {_b}")

            # if the second highest is b 
        elif _b > _a and _b > _d :
            #if the order will be c-b-a-d
            if _a > _d:
                print(f"{_c}, {_b}, {_a}, {_d}") 
            #if the order will be c-b-d-a
            else:
                print(f"{_c}, {_b}, {_d}, {_a}") 

        # if the second highest is d
        else:
            # if the order will be c-d-a-b
            if _a > _b:
                print(f"{_c}, {_d}, {_a}, {_b}")
            # if the order will be c-d-b-a 
            else:
                print(f"{_c}, {_d}, {_b}, {_a}")
    
    # if d is the highest number
    else:
        # if the second highest is a
        if _a > _b and _a > _c:
            # if the order will be d-a-b-c
            if _b > _c:
                print(f"{_a}, {_a}, {_b}, {_c}")
            # if the order will be d-a-b-c
            else:
                print(f"{_d}, {_a}, {_b}, {_c}")

            # if the second highest is b 
        elif _b > _a and _b > _c :
            #if the order will be d-b-a-c
            if _a > _c:
                print(f"{_d}, {_b}, {_a}, {_c}") 
            #if the order will be d-b-c-a
            else:
                print(f"{_d}, {_b}, {_c}, {_a}") 

        # if the second highest is c
        else:
            # if the order will be d-c-a-b
            if _a > _b:
                print(f"{_d}, {_c}, {_a}, {_b}")
            # if the order will be d-c-b-a 
            else:
                print(f"{_d}, {_c}, {_b}, {_a}")
        
        

a, b, c, d = askNumbers()
order = arrangeNumbers(a, b, c, d)

