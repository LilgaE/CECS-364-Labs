# Evan Lilga
# CSCE 364; Spring 2022
# #3 - Lilga_lab3.py

# Another Covid data set :D
import pandas as pd


def loaddata():
    Sumoftotalcases = 0
    SumofNewCases = 0
    SumofDeath = 0
    SumofNewDeath = 0
    with open("United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv", "r") as Filein:
        next(Filein)
        for row in Filein:
            try:
                split = row.split(",")
                Sumoftotalcases += int(split[2])
                SumofNewCases += int(split[5])
                SumofDeath += int(split[7])
                SumofNewDeath += int(split[10])
            except ValueError:
                print(row)
                print("Value Error")
    print("Sum of total cases: " + str(Sumoftotalcases))
    print("Sum of new cases: " + str(SumofNewCases))
    print("Sum of total death: " + str(SumofDeath))
    print("Sum of new death: " + str(SumofNewDeath))


def databystate():
    state = []
    totalcases = []
    NewCases = []
    Death = []
    NewDeath = []
    with open("United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv", "r") as Filein:
        next(Filein)
        for row in Filein:
            split = row.split(",")
            state.append(str(split[1]))
            totalcases.append(int(split[2]))
            NewCases.append(int(split[5]))
            Death.append(int(split[7]))
            NewDeath.append(int(split[10]))

    df = pd.DataFrame(index=[state])
    df['Total Cases'] = totalcases
    df['New Cases'] = NewCases
    df['Total Death'] = Death
    df['New Death'] = NewDeath
    Userin = input("Please input the state you would like to accesses\n")
    Statedata = df.loc[Userin]
    print("Sum of Total Cases: " + str(Statedata['Total Cases'].sum()))
    print("Sum of new cases: " + str(Statedata['New Cases'].sum()))
    print("Sum of total death: " + str(Statedata['Total Death'].sum()))
    print("Sum of new death: " + str(Statedata['New Death'].sum()))


def main():
    Userin = 99
    while Userin != 0:
        print("1. All data")
        print("2. Data by state")
        print("0. EXIT")
        Userin = int(input("Please input the test you would like to run\n"))
        if Userin == 1:
            loaddata()
            print("\n\n")
        elif Userin == 2:
            databystate()
            print("\n\n")
        else:
            print("Please Try again")
    print("thanks")

main()