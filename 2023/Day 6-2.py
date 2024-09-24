
import math

def fun(race):
    # better function
    
    a = ((-race[0] + (z := ((race[0] ** 2) - 4 * race[1]) ** .5)) / -2) 
    b = ((-race[0] - z) / -2)

    if a % 1 != 0 or b % 1 != 0:
        return math.floor(b) - math.ceil(a) + 1

    return b - a - 2 + 1

time, distance = [int("".join(l.split()[1:])) for l in open("f.txt").read().split("\n")]        
print(fun((time, distance)))

