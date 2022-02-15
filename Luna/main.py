# Writen by Stabs-
# Beginnings of the infamous Luna
# The Stock Trading Bot

# TODO
#  Get current price data for the day to find when to buy/sell that day
#  How Fast can we get the data from? -Can we get data anymore?
#  Create a comparison function
#  Get stock names with averages
#  List of top 10 stocks of the day
#  List of top 10 stocks of the Week
#  List of top 10 stocks of the Month
#  List of top 10 stocks of the Year
#  For above use present change
#  Challenges going through all 39952 stocks, 82221 funds, 11403 ETFs
#  Tax calculations for selling short term vs long term stock.
#  Dividend return on stock
#  Dividend tax information
#  Candle stick graph
#  Maybe Crypto an HFT
#  Maybe some tax stuff

import datetime  # Gets current date
import time
from _socket import gethostname  # For Users Name
import investpy  # Gets stock data
import matplotlib.pyplot as plt  # Plots Stock Data
import pandas as pd  # Processes stock data

# test0 are the example functions given from https://investpy.readthedocs.io/_info/usage.html
def test0():
    try:
        Stockname = str(input("Please input the company name or ticker\n"))
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
    except ConnectionError():
        print("Connection Error Please try again")
    except RuntimeError:
        print("Stocks not found.")
    except TypeError:
        print("Type Error")
    except:
        print("Unkown Error")


# test1 is me messing with the outputs of some functions from the investpy library
def test1():
    try:
        Stockname = str(input("Please input the company name or ticker\n"))
        current = datetime.datetime.now()
        cur = str(current.day) + '/' + str(current.month) + '/' + str(current.year)
        past = str(current.day) + '/' + str(current.month) + '/' + str(current.year - 1)
        search_result = investpy.search_quotes(text=Stockname, products=['stocks'],
                                               countries=['united states'], n_results=1)
        print(search_result)
        print("\n\n")
        recent_data = search_result.retrieve_historical_data(from_date=past, to_date=cur)

        print("\n\nAverage return for past year")
        print(str(recent_data['Change Pct'].mean()) + "%")
        print("\n\n")
        print(recent_data.info())
        print("\n\n")
        print(recent_data.sort_values('High').head())
        print("\n\n")
        print(recent_data.Open.head())
        print("\n\n")
        print(recent_data.Close.head())
        print("\n\n")
    except RuntimeError:
        print("Stocks not found.")
    except ConnectionError():
        print("Connection Error Please try again")
    except TypeError:
        print("Type Error")
    except:
        print("Unkown Error")


# Plotting is a combination of investpy and matplotlib.pyplot library to visualize the data better.
def plotting():
    try:
        Stockname = str(input("Please input the company name\n"))
        current = datetime.datetime.now()
        cur = str(current.day) + '/' + str(current.month) + '/' + str(current.year)
        past = str(current.day) + '/' + str(current.month) + '/' + str(current.year - 1)
        search_result = investpy.search_quotes(text=Stockname, products=['stocks'],
                                               countries=['united states'], n_results=1)
        print(search_result)
        recent_data = search_result.retrieve_historical_data(from_date=past, to_date=cur)
        test = recent_data[['Open', 'High', 'Low', 'Close']]
        print(test.head())
        plt.close('all')
        test.plot()
        plt.title(search_result.name + " Stock Data")
        plt.ylabel("Price (USD)")
        plt.show()
    except ConnectionError():
        print("Connection Error Please try again")
    except RuntimeError:
        print("Stocks not found.")
    except TypeError:
        print("Type Error")
    except:
        print("Unkown Error")


# Used to pull in all US stocks and compare their year/month/week average return on the stock
def compare():
    listofnames = []
    listofmeans = []
    current = datetime.datetime.now()
    cur = str(current.day) + '/' + str(current.month) + '/' + str(current.year)
    pastyear = str(current.day) + '/' + str(current.month) + '/' + str(current.year - 1)
    pastmonth = str(current.day) + '/' + str(current.month - 1) + '/' + str(current.year)
    pastweek = str(current.day - 7) + '/' + str(current.month) + '/' + str(current.year)
    with open("Symbollist .txt", "r") as Filein:
        for row in Filein:
            split = row.split(",")
            listofnames.append(split[7])
    for name in listofnames:
        try:
            data = nasdaqdatalink.get_table('ZACKS/FC', ticker=name)
            print(data.head())
            search_result = investpy.search_quotes(text=name, products=['stocks'], countries=['united states'],
                                                   n_results=1)
            print(search_result)
            time.sleep(30) # Website limitaions
            recent_data = search_result.retrieve_historical_data(from_date=pastweek, to_date=cur)
            print(recent_data)
            listofmeans.append(str(recent_data['Change Pct'].mean()) + "%")
        except RuntimeError:
            print("Stocks not found.")
        except ConnectionError:
            print("connection error")
            break
        except IndexError:
            print("Index error")
        except TypeError:
            print("Type Error")
        except:
            print("Unkown Error")
    print(listofnames)
    print(listofmeans)


# main asks what function the user would like to use and runs that function, also repeats until the user is done
def main():
    pd.set_option('display.max_columns', None)
    print("\n\nHello " + gethostname() + ", my name is Luna and I will help you with your stock needs.")
    Userin = 99
    while Userin != 0:
        print("1. Demo function")
        print("2. Messing around")
        print("3. PLOT")
        print("4. compare")
        print("0. EXIT")
        Userin = int(input("Please input the test you would like to run\n"))
        if Userin == 1:
            test0()
            print("\n\n")
        elif Userin == 2:
            test1()
            print("\n\n")
        elif Userin == 3:
            plotting()
            print("\n\n")
        elif Userin == 4:
            compare()
            print("\n\n")
        else:
            print("Please Try again")

    print("Thank you for using Luna the stock trading bot\n")
    print("And never forget\n")
    print(
        "\"Nobody knows if a stock is going to go up, down,\nsideways or in fucking circles,\nleast of all "
        "stockbrokers, right?\"")
    # QUOTE FROM THE WOLF OF WALL STREET


main()

# investpy,
#    author = {Alvaro Bartolome del Canto},
#    title = {investpy - Financial Data Extraction from Investing.com with Python},
#    year = {2018-2021},
#    publisher = {GitHub},
#    journal = {GitHub Repository},
#    how published = {\url{https://github.com/alvarobartt/investpy}},
