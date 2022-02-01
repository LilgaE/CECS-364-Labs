#Evan Lilga
#CECS 364
#Lab 2

#main with menu
#NO DATA DUMPS    BE SMART AND MAKE IT FOR RETARDS
#LIST COMPREHENTION
#

import csv
from _socket import gethostname


def FF():
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as CDCdata:
        print("\n\n")
        for i in range(0, 3):
            print(next(CDCdata))

def full():
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as test:
        print("\n")
        for i in range(0, 3):
            next(test)
        for row in test:
            print(row)

def Firstfive():
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as test:
        for i in range(0, 3):
            next(test)
        for j in range(0, 5):
            print(next(test))


def High():
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as test:
        next(test)
    #highest reported cases
    #AKA Sort with max print 1

def HighTen():
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as test:
        next(test)
    #highest reported cases
    #AKA Sort with max print next 10

def monthAve():
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as test:
        next(test)
    #print average of each month
    #Number of days in given month
    #Not that hard :D

def main():
    print("\n\nHello "+gethostname()+", welcome to the CDC data analysis")
    print("1. Data headers")
    print("2. Full Data set")
    print("3. Five most recent dates")
    print("4. Highest reported cases on a single day")
    print("5. 10 Highest reported cases for days")
    print("6. Average per month")

    Userin = int(input("Please input the test you would like to run\n"))


    if (Userin == 1):
        FF()
        print("\n\n")
    if (Userin == 2):
        full()
        print("\n\n")
    if (Userin == 3):
        Firstfive()
        print("\n\n")
    if (Userin == 4):
        High()
        print("\n\n")
    if (Userin == 5):
        HighTen()
        print("\n\n")
    if (Userin == 6):
        monthAve()
        print("\n\n")

main()