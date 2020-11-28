# coding=utf-8

# author : Ed Goodwin
# date : 11.28.2020
# file : main.py
# project : pythonForEverybody
# desc : Going through the book Python For Everybody. This is a record of the exercises from the book.
#

import random
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Exercise 2.2
def seek_input():
    inpname = input("Enter your name: ")
    print(str(inpname))


# Exercise 2.3
def calc_gross_pay():
    inphours = input("Enter hours worked: ")
    inprate = input("Enter hourly rate: ")
    pay = inphours * inprate
    output = "Pay: " + str(pay)
    print(output)

# Exercise 2.4
def math_calcs():
    width = 17
    height = 12.0

    print(width//2)
    print(width/2.0)
    print(height/3)
    print(1 + 2 * 5)

# Exercise 3.1, 3.2
def calc_gross_pay_overtime_inputs():
    inphours = input("Enter hours worked: ")
    inprate = input("Enter hourly rate: ")

    try:
        if inphours <= 40:
            pay = inphours * inprate
        else:
            pay = (inprate * 40) + (1.5 * inprate * (inphours - 40))
        output = "Pay: " + str(pay)
        print(output)

    except:
        print("Error, please enter numeric input")

# Exercise 3.3
def grade_calc():
    inpgrade = input("Enter a score between 0.0 and 1.0: ")
    errormsg = "Error: Number out of range. Please enter score between 0.0 and 1.0"
    try:
        if inpgrade < 0.0:
            print(errormsg)
        elif inpgrade > 1.0:
            print(errormsg)
        elif inpgrade >= 0.9:
            print("A")
        elif inpgrade >= 0.8:
            print("B")
        elif inpgrade >= 0.7:
            print("C")
        elif inpgrade >= 0.6:
            print("D")
        else:
            print("F")
    except:
        print("Error: Invalid type. Please input a number between 0.0 and 1.0")

def calc_gross_pay_overtime(hours, rate):
    try:
        if hours <= 40:
            pay = hours * rate
        else:
            pay = (rate * 40) + (1.5 * rate * (hours - 40))
        output = \
            "Hours: " + str(hours) + "\n" + \
            "Rate: " + str(rate) + "\n" + \
            "Pay: " + str(pay)
        print(output)

    except:
        print("Error, please enter numeric input")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # seek_input()
    # calc_gross_pay()
    # math_calcs()
    # calc_gross_pay_overtime()
    # grade_calc()
    calc_gross_pay_overtime(15, 20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
