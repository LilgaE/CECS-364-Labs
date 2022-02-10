# Writen by Stabs-
# Beginnings of the infamous Luna
# Stock Trading Bot


from _socket import gethostname  # For Users Name
import investpy  # Gets stock data
import pandas as pd  # Processes stock data
import matplotlib.pyplot as plt  # Plots Stock Data
import datetime  # Gets current date


# test0 are the example functions given from https://investpy.readthedocs.io/_info/usage.html
def test0():
    Stockname = input("Please input the company name or ticker\n")
    search_result = investpy.search_quotes(text=Stockname, products=['stocks'],
                                           countries=['united states'], n_results=1)
    print(search_result)
    print("\n\n")

    recent_data = search_result.retrieve_recent_data()
    print(recent_data)
    print("\n\n")

    default_currency = search_result.retrieve_currency()
    print(default_currency)
    print("\n\n")

    information = search_result.retrieve_information()
    print(information)
    print("\n\n")

    technical_indicators = search_result.retrieve_technical_indicators(interval="daily")
    print(technical_indicators)
    print("\n\n")

    data = investpy.economic_calendar()
    print(data.head())


# test1 is me messing with the outputs of some functions from the investpy library
def test1():
    Stockname = input("Please input the company name or ticker\n")
    current = datetime.datetime.now()
    cur = str(current.day) + '/' + str(current.month) + '/' + str(current.year)
    search_result = investpy.search_quotes(text=Stockname, products=['stocks'],
                                           countries=['united states'], n_results=1)
    print(search_result)
    print("\n\n")
    recent_data = search_result.retrieve_historical_data(from_date='01/01/2022', to_date=cur)

    print("\n\nPandas Describe function")
    print(recent_data['Change Pct'].describe())
    print("\n\n")
    print(recent_data.info())
    print("\n\n")
    print(recent_data.sort_values('High').head())
    print("\n\n")
    print(recent_data.Open.head())
    print("\n\n")
    print(recent_data.Close.head())
    print("\n\n")


# test2 is a combination of investpy and matplotlib.pyplot library to visualize the data better.
def Plotting():
    Stockname = input("Please input the company name\n")
    current = datetime.datetime.now()
    cur = str(current.day) + '/' + str(current.month) + '/' + str(current.year)
    search_result = investpy.search_quotes(text=Stockname, products=['stocks'],
                                           countries=['united states'], n_results=1)
    print(search_result)
    print("\n\n")
    recent_data = search_result.retrieve_historical_data(from_date='01/01/2022', to_date=cur)
    test = recent_data[['Open', 'High', 'Low', 'Close']]
    print(test.head())
    plt.close('all')
    test.plot()
    plt.title(search_result.name + " Stock Data")
    plt.ylabel("Price (USD)")
    plt.show()

# main asks what function the user would like to use and runs that function, also repeats until the user is done
def main():
    pd.set_option('display.max_columns', None)
    print("\n\nHello " + gethostname() + ", my name is Luna and I will help you with your stock needs.")
    Userin = 99
    while Userin != 0:
        print("1. Demo function")
        print("2. Messing around")
        print("3. PLOT")
        print("0. EXIT")
        Userin = int(input("Please input the test you would like to run\n"))
        if Userin == 1:
            test0()
            print("\n\n")
        elif Userin == 2:
            test1()
            print("\n\n")
        elif Userin == 3:
            Plotting()
            print("\n\n")
        else:
            print("Please Try again")

    print("Thank you for using Luna the stock trading bot\n")
    print("And never forget\n")
    print(
        "\"Nobody knows if a stock is going to go up, down,\nsideways or in fucking circles,\nleast of all "
        "stockbrokers,\nright?\"")
    # QUOTE FROM THE WOLF OF WALL STREET


main()

# investpy,
#    author = {Alvaro Bartolome del Canto},
#    title = {investpy - Financial Data Extraction from Investing.com with Python},
#    year = {2018-2021},
#    publisher = {GitHub},
#    journal = {GitHub Repository},
#    how published = {\url{https://github.com/alvarobartt/investpy}},
