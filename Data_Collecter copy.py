import matplotlib.pyplot as plt
import json
import urllib.request
import time
import pandas as pd
from datetime import datetime
import sys

#To successfully use this program, obtain an API key from AlphaVantage

def getData(symbol, dataKind):
    """
    This function takes in 3 parameters and returns data according to parameter specifications.
    Prameters:
        symbol - string, ticker of the stock entered by user - cast to uppercase
        dataKind - string, type of data as specified by user. Options include, '1. open', '2. high', '3. low', '4. close', '5. volume'
    Return:
        masterDF - dataframe, contains daily data that user requested. 
    """
    try:
        link = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&outputsize=compact&apikey=ENTER_KEY'
        htmltext = urllib.request.urlopen(link)
        data = json.load(htmltext)
        myDict = {}
        print(type(data))
        price_data = data['Time Series (Daily)']
        for key, value in price_data.items():
            date_num = datetime.strptime(key,"%Y-%m-%d")
            price = value[dataKind]
            myDict[date_num] = float(price)
        masterDF = pd.DataFrame.from_dict(myDict, orient = 'index')
        masterDF.index.name = "Time"
        masterDF.columns = [symbol]
        return masterDF

    except:
        print('Error occured when fetching data.')
        exit(0)

def graph(df):
    """
    Function responsible for plotting the data user requested. 
    Parameters:
        df - dataframe, contains data needed to be plotted
    """
    df.plot()
    plt.show()


def main():
    """
    Takes user input and makes the function calls necessary to pull data from Alphavantage API and plot the data 
    using matplotlib.
    """
    ticker = input('Enter stock symbol: ')
    dataOptions = [
        "1. open",
        "2. high",
        "3. low",
        "4. close",
        "5. volume"
        ]
    print(dataOptions) 
    data_option = input('What data would you like to view for ' + ticker + ": ") # input what data user wants to see

    dataFrame = getData(ticker.upper(), data_option) # call getData function to get data user wants
    print(dataFrame) # print the data for user

    graph(dataFrame) # call graph function


if __name__ == "__main__":
    main()