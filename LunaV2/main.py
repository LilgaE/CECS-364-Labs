# Writen by Stabs-
# Second version of Luna
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
#  Volume * ((high + low)/2) Average amount traded
#  Volume Change from day to day
#

import datetime  # Gets current date
import time
from _socket import gethostname  # For Users Name
import matplotlib.pyplot as plt  # Plots Stock Data
import pandas as pd  # Processes stock data
import nasdaqdatalink

nasdaqdatalink.ApiConfig.api_key = "H9RVg-d39XS_GaKb2Eyh"


# test0 are the example functions given from https://investpy.readthedocs.io/_info/usage.html
def test0():
    try:
        # Stockname = str(input("Please input the company name or ticker\n"))
        data = nasdaqdatalink.get_table('ZACKS/FC', ticker='MMM')
        print(data.info())
        for col in data.columns:
            print(col)
        print(data.head().to_csv())
        print(data[['comp_name_2', 'per_cal_year', 'per_cal_qtr', 'qtr_nbr', 'tot_revnu', 'gross_profit']])
    except ConnectionError():
        print("Connection Error Please try again")
    except RuntimeError:
        print("Stocks not found.")
    except TypeError:
        print("Type Error")
    except:
        print("Unknown Error")


# test1 is me messing with the outputs of some functions from the investpy library
def test1():
    try:
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker='MMM')
        print(data.info())
        for col in data.columns:
            print(col)
        print(data.head().to_csv())
        print(data[['open', 'high', 'low', 'close', 'volume', 'split_ratio']])
        print(data['open'].mean())

    except RuntimeError:
        print("Stocks not found.")
    except ConnectionError():
        print("Connection Error Please try again")
    except TypeError:
        print("Type Error")
    except:
        print("Unknown Error")


# Plotting is a combination of investpy and matplotlib.pyplot library to visualize the data better.
def plotting():
    try:
        Stockname = str(input("Please input the company ticker\n"))
        current = datetime.datetime.now()
        cur = str(current.year) + '-' + str(current.month) + '-' + str(current.day)
        past = str(current.year - 3) + '-' + str(current.month) + '-' + str(current.day)
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=Stockname, date={'gte': '2016-01-01'})
        test = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        test = test.set_index('date')
        print(test.head())
        plt.close('all')
        test.plot()
        plt.title(Stockname + " Stock Data")
        plt.ylabel("Price (USD)")
        plt.show()
    except ConnectionError():
        print("Connection Error Please try again")
    except RuntimeError:
        print("Stocks not found.")
    except TypeError:
        print("Type Error")
    except:
        print("Unknown Error")


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
            data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=name, date={'gte': '2016-01-01'})
            print(data)
            time.sleep(30)  # Website limitaions
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
            print("Unknown Error")
    print(listofnames)
    print(listofmeans)


# main asks what function the user would like to use and runs that function, also repeats until the user is done
def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
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



#SHOULD NOT BE USED AS A FINANCIAL ADVICE