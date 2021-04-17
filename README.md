# stock-visualization-python-
Stock data representation using data collected from AlphaVanatage

Purpose: 
This program will print data (open, close, low, high, volume) of your choice, for a ticker of your choise, in the past 100 trading sessions.

Functionality: 
The program works by obtaining data by making a call to the AlphaVantage API. 
For this one must have an API Key from AlphaVanatge. One can be obtained from https://www.alphavantage.co at no cost.
After obtaining the data, the program parses the data in order to obtain only what the user requested.
i.e. if the user requests the volume for AAPL, the program will extract only the volume data fro AAPL.
Finally, the program prints the data requested, and plots the data for the user using Matplotlib


Future Modifications/Improvements: 
I plan to develop this into a webpage where users can actively see real time data of their favorite stocks.
I plan to develop a user friendly UI, along with a quick backend to optimize user experience. 
Additionally, I hope to provide more data such as options data if a free source becomes available. 
