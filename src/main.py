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
    CONFIG_PATH = "/Users/hadi/Desktop/Projects/StockDashboard/src/config_files/sample.cfg"
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