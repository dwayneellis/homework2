# Dwayne Ellis
# CIS 2348
# October 6, 2020
# Lab 6.22 Brute force equation solver
# Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38 and
# 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients of two linear equations with variables x and y,
# use brute force to find an integer solution for x and y in the range -10 to 10.

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

def func_1(x, y):
    return a*x + b*y - c
def func_2(x, y):
    return d*x + e*y - f
final_x = 100
final_y = 100

for x in range(-10, 11):
    for y in range(-10, 11):
        if func_1(x, y) == func_2(x, y) and func_1(x, y) == 0:
            final_x = x
            final_y = y
if final_x != 100:
    print(final_x, final_y)
else:
    print('No solution')
