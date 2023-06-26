from data_pull import data_pull, get_trend
import rich, sys
from rich.console import Console
from objects import WatchListItem, Position, Balance, Trend
from rich import print
console = Console()

def printTrendToConsole():
    console.print("\nMARKET TREND", style = "white")
    trendList = ['^GSPC','^DJI','^IXIC']
    for ticker in trendList:
        response = data_pull(ticker)

        obj = Trend(ticker, response)
        output = str(obj)

        if float(output.split()[3][:-1]) >= 0:
            console.print(output, style = "bold green")
        else:
            console.print(output, style = "bold red")


def printWatchListToConsole(watchList: list):
    console.print("\nWATCHLIST", style = "white")
    for item in watchList:
        response = data_pull(item)
        if not response['valid']:
            console.print("Invalid Ticker: {}".format(item), style = "bold red")
            continue
        
        obj = WatchListItem(item, response)
        output = str(obj)
        if float(output.split()[5][:-1]) >= 0:
            console.print(output, style = "bold green")
        else:
            console.print(output, style = "bold red")

def printPositionsToConsole(positions: dict):
    console.print("\nPOSITIONS", style = "white")
    for ticker, numShares in positions.items():
        response = data_pull(ticker)
        ticker = ticker.upper()
        if not response['valid']:
            console.print("Invalid Ticker: {}".format(ticker), style = "bold red")
            continue
        obj = Position(ticker, response, float(numShares))
        output = str(obj)
        if "+" in output:
            console.print(output, style = "bold green")
        else:
            console.print(output, style = "bold red")

def printBalanceToConsole(cashHoldings: dict):
    console.print("\nBALANCES", style = "white")
    for currency, value in cashHoldings.items():
        obj = Balance(value, currency)
        output = str(obj)
        console.print(
            output, 
            style="white"
        )