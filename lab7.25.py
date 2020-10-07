# CIS 2348 Homework 1 Fall 2020.
# Dwayne Ellis
# Student ID: 0833810
# Lab 7.25: Exact change - functions

# Define exact change
def exact_change(user_total):
    dollar = user_total // 100
    user_total %= 100
    quarter = user_total // 25
    user_total %= 25
    dime = user_total // 10
    user_total %= 10
    nickel = user_total // 5
    user_total %= 5
    penny = user_total
    return dollar, quarter, dime, nickel, penny

# Define Main
if __name__ == '__main__':
    user_total = int(input())

    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)

    if user_total <= 0:
        print('no change')

    if num_dollars > 1:
        print('%d dollars' % num_dollars)

    elif num_dollars == 1:
        print('%d dollar' % num_dollars)

    if num_quarters > 1:
        print('%d quarters' % num_quarters)

    elif num_quarters == 1:
        print('%d quarter' % num_quarters)

    if num_dimes > 1:
        print('%d dimes' % num_dimes)

    elif num_dimes == 1:
        print('%d dime' % num_dimes)

    if num_nickels > 1:
        print('%d nickels' % num_nickels)

    elif num_nickels == 1:
        print('%d nickel' % num_nickels)

    if num_pennies > 1:
        print('%d pennies' % num_pennies)

    elif num_pennies == 1:
        print('%d penny' % num_pennies)
