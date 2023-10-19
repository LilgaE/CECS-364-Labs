# Writen by Stabs-
# Second version of Luna
# The Stock Trading Bot
# YOU HAVE TO WANT SO SUCCEED AS BAD AS YOU WANT TO BREATH
# Using Zacks Investment Research $1,200 a year data

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
#  NumPy Arrays to put lists with values together
#  ANOVA for compare (DONT FORGET TESTS)(LIKE WHAT MADE YOU FAIL STATS) Scipy
#
#

import datetime  # Gets current date
from _socket import gethostname  # For Users Name
import matplotlib.pyplot as plt  # Plots Stock Data
import nasdaqdatalink
import pandas as pd  # Processes stock data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.ensemble import VotingClassifier

nasdaqdatalink.ApiConfig.api_key = "H9RVg-d39XS_GaKb2Eyh"


# test0 are the example functions given from https://investpy.readthedocs.io/_info/usage.html
def test0():
    try:
        # Stockname = str(input("Please input the company name or ticker\n"))
        data = nasdaqdatalink.get_table('ZACKS/FC', ticker='NOC')
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
    current = datetime.datetime.now()
    cur = str(current.day) + '/' + str(current.month) + '/' + str(current.year)
    pastyear = str(current.day) + '/' + str(current.month) + '/' + str(current.year - 1)
    pastmonth = str(current.day) + '/' + str(current.month - 1) + '/' + str(current.year)
    pastweek = str(current.day - 7) + '/' + str(current.month) + '/' + str(current.year)
    with open("Symbollist .txt", "r") as Filein:
        for row in Filein:
            split = row.split(",")
            listofnames.append(split[7])
    try:
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[0], date={'gte': '2016-01-01'})
        test0 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[1], date={'gte': '2016-01-01'})
        test1 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[2], date={'gte': '2016-01-01'})
        test2 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[3], date={'gte': '2016-01-01'})
        test3 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[4], date={'gte': '2016-01-01'})
        test4 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[5], date={'gte': '2016-01-01'})
        test5 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[6], date={'gte': '2016-01-01'})
        test6 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[7], date={'gte': '2016-01-01'})
        test7 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[8], date={'gte': '2016-01-01'})
        test8 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=listofnames[9], date={'gte': '2016-01-01'})
        test9 = pd.DataFrame(data[['date', 'open', 'high', 'low', 'close']])
        print(listofnames[0] + ' mean of open prices: ' + str(test0['open'].mean()))
        print(listofnames[0] + ' most recent open price: ' + str(test0['open'][0]))
        print(listofnames[1] + ' mean of open prices: ' + str(test1['open'].mean()))
        print(listofnames[1] + ' most recent open price: ' + str(test1['open'][1]))
        print(listofnames[2] + ' mean of open prices: ' + str(test2['open'].mean()))
        print(listofnames[2] + ' most recent open price: ' + str(test2['open'][2]))
        print(listofnames[3] + ' mean of open prices: ' + str(test3['open'].mean()))
        print(listofnames[3] + ' most recent open price: ' + str(test3['open'][3]))
        print(listofnames[4] + ' mean of open prices: ' + str(test4['open'].mean()))
        print(listofnames[4] + ' most recent open price: ' + str(test4['open'][4]))
        print(listofnames[5] + ' mean of open prices: ' + str(test5['open'].mean()))
        print(listofnames[5] + ' most recent open price: ' + str(test5['open'][5]))
        print(listofnames[6] + ' mean of open prices: ' + str(test6['open'].mean()))
        print(listofnames[6] + ' most recent open price: ' + str(test6['open'][6]))
        print(listofnames[7] + ' mean of open prices: ' + str(test7['open'].mean()))
        print(listofnames[7] + ' most recent open price: ' + str(test7['open'][7]))
        print(listofnames[8] + ' mean of open prices: ' + str(test8['open'].mean()))
        print(listofnames[8] + ' most recent open price: ' + str(test8['open'][8]))
        print(listofnames[9] + ' mean of open prices: ' + str(test9['open'].mean()))
        print(listofnames[9] + ' most recent open price: ' + str(test9['open'][9]))

    except RuntimeError:
        print("Stocks not found.")
    except ConnectionError:
        print("connection error")
    except IndexError:
        print("Index error")
    except TypeError:
        print("Type Error")
    except:
        print("Unknown Error")


def learnsomething():
    Stockname = str(input("Please input the company ticker\n"))
    Traindata = nasdaqdatalink.get_table('WIKI/PRICES', ticker=Stockname, date={'gte': '2016-01-01'})
    Testdata = nasdaqdatalink.get_table('WIKI/PRICES', ticker=Stockname, date={'gte': '2017-01-01'})
    print(Testdata)
    print(Traindata)


def Lab4():
    Stockname = str(input("Please input the company ticker\n"))
    data = nasdaqdatalink.get_table('WIKI/PRICES', ticker=Stockname, date={'gte': '2016-01-01'})
    cutdata = pd.DataFrame(data[['close', 'volume']])
    volsum = cutdata['volume'].sum()
    volmin = cutdata['volume'].min()
    volmax = cutdata['volume'].max()
    print("Volume")
    print(str(volmin) + ": Min value")
    print(str(volmax) + ": Max value")
    print(str(volsum) + ": Total Sum")
    print(str(volsum / cutdata['volume'].size) + ": Average")
    print("\n\n")
    print("Close price")
    cCount = 0
    iCount = 0
    closemin = cutdata['close'].min()
    closemax = cutdata['close'].max()
    print(str(closemin) + ": Min value")
    print(str(closemax) + ": Max value")
    print("\n\n")
    for x in range(1,478):
        if cutdata['volume'][x] >= cutdata['volume'][x-1]:
            print('Price will rise from yesterday')
            print(str(cutdata['close'][x-1]) + ' Price from yesterday')
            print(str(cutdata['close'][x]) + ' Price from today')
            if cutdata['close'][x-1] <= cutdata['close'][x]:
                print('correct')
                cCount += 1
            else:
                print('incorrect')
                iCount += 1
        else:
            print('Price will fall from yesterday')
            print(str(cutdata['close'][x - 1]) + ' Price from yesterday')
            print(str(cutdata['close'][x]) + ' Price from today')
            if cutdata['close'][x-1] >= cutdata['close'][x]:
                print('correct')
                cCount += 1
            else:
                print('incorrect')
                iCount += 1
    print(str(cCount) + ' Correct')
    print(str(iCount) + ' Incorrect')




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
        print("5. to be continued")
        print("6. Lab4")
        print("0. EXIT")
        Userin = int(input("Please input the test you would like to run\n"))
        if Userin == 0:
            print("Thank you for using Luna the stock trading bot\n")
            print("And never forget\n")
            print(
                "\"Nobody knows if a stock is going to go up, down,\nsideways or in fucking circles,\nleast of all "
                "stockbrokers, right?\"")
            # QUOTE FROM THE WOLF OF WALL STREET
        elif Userin == 1:
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
        elif Userin == 5:
            learnsomething()
            print("\n\n")
        elif Userin == 6:
            Lab4()
            print("\n\n")

        else:
            print("Please Try again")





main()

# SHOULD NOT BE USED AS FINANCIAL ADVICE
