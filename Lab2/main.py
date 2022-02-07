#Evan Lilga
#CECS 364
#Lab 2

#
#
#
#

import csv
from _socket import gethostname
COVIDLIST = []
DATAOLNY = []

def Copy():
    COVIDLIST = []
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as Filein:
        for row in Filein:
            COVIDLIST.append(row)
    return COVIDLIST


def CopyData():
    DATAOLNY = []
    with open("data_table_for_daily_case_trends__the_united_states.csv", "r") as Filein2:
        for i in range(0, 3):
            next(Filein2)
        for row2 in Filein2:
            DATAOLNY.append(row2)
    return DATAOLNY

def FF(File):
    print("\n\n")
    print(File[0])
    print(File[1])
    print(File[2])

def full(File):
    print("\n\n")
    for row in File:
        print(row)

def Firstfive(File):
    print("\n\n")
    for j in range(0, 5):
        print(File[j])


def High(File):
    highest = 0
    split = []
    for row in File:
        split = row.split(",")
        if int(split[2]) > highest:
            highest = int(split[2])
            max = row
    print("\n\n")
    print(max)

def HighTen(File):
    highest = 0
    split = []
    topten = []
    print("\n\n")
    for row in File:
        split = row.split(",")
        topten.append(int(split[2]))
    topten.sort()
    topten.reverse()
    for row2 in range(0, 9):
        print(topten[row2])

def monthAve(File):
    Number = []
    Date = []
    split = []
    split2 = []
    month = ""

    for row in File:
        split = row.split(",")
        split2 = split[1].split(" ")
        Date.append(split2[0])
        Number.append(int(split[2]))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Jan":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("January average :" + str(CaseCount/MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Feb":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("Febuary average :" + str(CaseCount/MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Mar":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("March average :" + str(CaseCount/MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Apr":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("April average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "May":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("May average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Jun":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("June average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Jul":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("July average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Aug":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("August average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Sep":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("September average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Oct":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("October average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Nov":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("November average :" + str(CaseCount / MonthDays))
    MonthDays = 0
    DataDay = 0
    CaseCount = 0
    for row2 in Date:
        if row2 == "Dec":
            MonthDays += 1
            CaseCount += Number[DataDay]
            DataDay += 1
        else:
            DataDay += 1
    print("December average :" + str(CaseCount / MonthDays))



    #print average of each month
    #Number of days in given month
    #Not that hard :D

def main():
    print("\n\nHello "+gethostname()+", welcome to the CDC data analysis")
    COVIDLIST   = Copy()
    DATAOLNY = CopyData()
    Userin = 99
    while(Userin != 0):
        print("1. Data headers")
        print("2. Full Data set")
        print("3. Five most recent dates")
        print("4. Highest reported cases on a single day")
        print("5. 10 Highest reported cases for days")
        print("6. Average per month")
        print("0. To exit")
        Userin = int(input("Please input the test you would like to run\n"))
        if (Userin == 1):
            FF(COVIDLIST)
            print("\n\n")
        if (Userin == 2):
            full(DATAOLNY)
            print("\n\n")
        if (Userin == 3):
            Firstfive(DATAOLNY)
            print("\n\n")
        if (Userin == 4):
            High(DATAOLNY)
            print("\n\n")
        if (Userin == 5):
            HighTen(DATAOLNY)
            print("\n\n")
        if (Userin == 6):
            monthAve(DATAOLNY)
            print("\n\n")

main()