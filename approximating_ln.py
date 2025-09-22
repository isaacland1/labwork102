# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jimmy Ho
# Daniel Izmerly
# NAME Isaac Andrew Land
# Name: Nicholas Morales
# Section: ENGR-102-505
# Assignment: Lab 6.15 
# Date: 22 September 2025

import math

x_value = float(input("Enter a value for x: \n"))

if not(0 < x_value <= 2):
    x_value = float(input("Out of range! Try again: \n"))
 

tolerance_value = float(input("Enter the tolerance: \n"))

#Set up variables
exact_value = float(math.log(x_value))
approx_value = 0
index = 1
addition = 0

if 0 < x_value <= 2:
    while math.fabs((exact_value - approx_value)) >= tolerance_value:
        addition = ((x_value**index)/index)
        print(exact_value - approx_value)
        if (index % 2) == 0:
            approx_value -= addition
    

        elif (index % 2) != 0:
            approx_value += addition
    index += 1




print(f'ln({x_value}) is approximately {approx_value}')
print(f'ln({x_value}) is exactly {exact_value}')
print(f'The difference is {math.fabs(exact_value - approx_value)}')