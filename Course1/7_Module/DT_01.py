import math

def builtin_sqrt(x):
    return math.sqrt(x)

def userwritten_sqrt(x, tolerance=1e-6):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    guess = x / 2.0 if x > 1 else 1.0  
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2.0
    
    return guess

print("My built in sqrt of 25:", builtin_sqrt(25))
print("My built in sqrt of 2:", builtin_sqrt(2))
print("My built in sqrt of 0.25:", builtin_sqrt(0.25))

print("**********************")
print("My userwritten sqrt of 25:", userwritten_sqrt(25))
print("My userwritten sqrt of 2:", userwritten_sqrt(2))
print("My userwritten sqrt of 0.25:", userwritten_sqrt(0.25))