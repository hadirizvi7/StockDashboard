class WatchListItem:
    def __init__(self, ticker: str, response: dict) -> None:
        self.name = ticker
        self.price = response['regularMarketPrice']['fmt']
        self.cap = response['marketCap']['fmt']
        self.volume = response['regularMarketVolume']['fmt']
        self.changePercent = response['regularMarketChangePercent']['fmt']
        self.change = response['regularMarketChange']['fmt']
    
    def __str__(self):
        return "{name} {price} {cap} {volume} {change} {changePercent}".format(
            name = self.name, 
            price = self.price,
            cap = self.cap,
            volume = self.volume,
            changePercent = self.changePercent,
            change = self.change
        )
'''
currentPrice = float(response['regularMarketPrice']['raw']) * float(numShares)
        self.openPrice = float(response['regularMarketOpen']['raw']) * float(numShares)
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
            output = "{ticker} {diff} -{percentChange}%".format(
                ticker = ticker,
                diff = diff,
                percentChange = percentChange
            )
            console.print(output, style = "bold red")
'''
class Position:
    def __init__(self, ticker: str, response: dict, numShares: float) -> None:
        self.name = ticker
        self.currentPrice = float(response['regularMarketPrice']['raw'])  * numShares
        self.openPrice = float(response['regularMarketOpen']['raw'])  * numShares

    def __str__(self) -> str:
        diff = float("{:.2f}".format(self.currentPrice - self.openPrice))
        if diff >= 0:
            percentChange = float("{:.2f}".format((self.currentPrice/self.openPrice) * 100 - 100))
            output = "{ticker} +{diff} +{percentChange}%".format(
                ticker = self.name,
                diff = diff,
                percentChange = percentChange
            )
            return output
        else:
            percentChange = float("{:.2f}".format((self.openPrice/self.currentPrice) * 100 - 100))
            output = "{ticker} {diff} -{percentChange}%".format(
                ticker = self.name,
                diff = diff,
                percentChange = percentChange
            )
            return output
        return ""

class ProfitLossItem:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return ""

class Balance:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return ""