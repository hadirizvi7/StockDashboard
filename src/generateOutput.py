from data_pull import data_pull
import rich, sys
from rich.console import Console
from objects import WatchListItem, Position
console = Console()

def printWatchListToConsole(watchList: list):
    console.print("\nWATCHLIST", style = "white")
    for item in watchList:
        response = data_pull(item)
        print(response)
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