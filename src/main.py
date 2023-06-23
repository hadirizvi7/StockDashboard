from tkinter.ttk import Style
import rich, sys
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich import print
from rich.layout import Layout
from configparser import ConfigParser
from data_pull import data_pull
from objects import WatchListItem, Position
from generateOutput import printWatchListToConsole, printPositionsToConsole, printBalanceToConsole

def configure():
    CONFIG_PATH = "/Users/hadi/Desktop/Projects/StockDashboard/src/settings.cfg"
    config_object = ConfigParser()
    config_object.read(CONFIG_PATH)

    watchListData = list(dict(config_object.items('watchlist')).keys())
    watchList = [item.upper() for item in watchListData]

    positions = dict(config_object.items('positions'))
    balance = dict(config_object.items('cash'))

    return watchList, positions, balance

if __name__ == "__main__":
    watchList, positions, balance = configure()
    printWatchListToConsole(watchList)
    printPositionsToConsole(positions)
    printBalanceToConsole(balance)

#layout = Layout()
'''
layout.split_column(
    Layout(name="upper"),
    Layout(name="mid"),
    Layout(name="lower")
)
'''
'''
console.print("\nPOSITIONS", style = "white")
for ticker, numShares in positions.items():
    response = data_pull(ticker)
    ticker = ticker.upper()
    if not response['valid']:
        console.print("Invalid Ticker: {}".format(ticker), style = "bold red")
        continue
    currentPrice = float(response['regularMarketPrice']['raw']) * float(numShares)
    openPrice = float(response['regularMarketOpen']['raw']) * float(numShares)
    diff = float("{:.2f}".format(currentPrice - openPrice))
    if diff >= 0:
        percentChange = float("{:.2f}".format((currentPrice/openPrice) * 100 - 100))
        output = "{ticker} +{diff} +{percentChange}%".format(
            ticker = ticker,
            diff = diff,
            percentChange = percentChange
        )
        console.print(output, style = "bold green")
    else:
        percentChange = float("{:.2f}".format((openPrice/currentPrice) * 100 - 100))
        output = "{ticker} +{diff} -{percentChange}%".format(
            ticker = ticker,
            diff = diff,
            percentChange = percentChange
        )
        console.print(output, style = "bold red")
'''
#layout["upper"].update(upper_output)
#print(layout)