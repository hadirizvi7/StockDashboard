from data_pull import data_pull
import rich, sys
from rich.console import Console
from objects import WatchListItem, Position
console = Console()

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
        output = []
        stack = []
        formattedValue = value
        if len(value) > 3 and "," not in value:
            for digit in reversed(list(value)):
                stack.append(digit)
                if len(stack) == 3:
                    stack.append(",")
                    output.append(stack)
                    stack = []
            output.append(stack)
            formattedValue = ""
            for item in reversed(output):
                formattedValue += "".join(list(reversed(item)))
        
        console.print("{value}.00 {currency}".format(
            currency = currency.upper(),
            value = formattedValue
        ),
        style="white")