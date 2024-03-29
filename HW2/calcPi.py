##A.J. Delcimmuto
##HW2
import math




##iterative

def fixed_point_iteration(f, x):
    step = 0
    while not approx_fixed_point(f, x):
        x = f(x)
        step += 1
    return x, step

def approx_fixed_point(f,x):
    if abs(f(x) - x) <= 1e-15:
        return True
    else:
        return False



##newtonian
def newton_update(f, df):
    def update(x):
        return x - (f(x) / df(x))
    return update



def find_zero(f, df,x):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero,x)



def approx_eq(x,y):
    if abs(x - y) < 1e-15:
        return True
    else:
        return False

def improve(update,close,guess,iterations = 0):
    while not close(guess):
        guess = update(guess)
        iterations += 1
    return guess,iterations


#TESTING FUNCTION CALLS
#TEST FOR FIXED POINT
print(fixed_point_iteration(lambda x:math.sin(x)+x, 3.0))
#TEST FOR NEWTONIAN
print(find_zero(lambda x:math.sin(x), lambda x:math.cos(x),3.0))


#CALCULATION FOR PI - BOTH ITERATE THE SAME AMMOUNT
#CALCULATION FOR DOTTIE - 86 iterations for fixed point 4 for newtons method
#for this problem we used higher order functions to figure out if newtons method or fixed point iteration lasts longer
