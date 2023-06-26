class WatchListItem:
    def __init__(self, ticker: str, response: dict) -> None:
        self.name = ticker
        self.price = response['regularMarketPrice']['fmt']
        self.cap = response['marketCap']['fmt']
        self.volume = response['regularMarketVolume']['fmt']
        self.changePercent = response['regularMarketChangePercent']['fmt']
        self.change = response['regularMarketChange']['fmt']
    
    def __str__(self):
        return "{name} @ {price} {cap} {volume} {change} {changePercent}".format(
            name = self.name, 
            price = self.price,
            cap = self.cap,
            volume = self.volume,
            changePercent = self.changePercent,
            change = self.change
        )

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
        

class Trend:
    def __init__(self, ticker, response) -> None:
        self.name = ticker
        self.price = response['regularMarketPrice']['fmt']
        self.change = response['regularMarketChange']['fmt']
        self.changePercent = response['regularMarketChangePercent']['fmt']


    def __str__(self) -> str:
        return "{name} {price} {change} {changePercent}".format(
            name = self.name,
            price = self.price,
            change = self.change,
            changePercent = self.changePercent
        )

class Balance:
    def __init__(self, amount: str, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        output = []
        stack = []
        formattedValue = self.amount
        if len(self.amount) > 3 and "," not in self.amount:
            for digit in reversed(list(self.amount)):
                stack.append(digit)
                if len(stack) == 3:
                    stack.append(",")
                    output.append(stack)
                    stack = []
            output.append(stack)
            formattedValue = ""
            for item in reversed(output):
                formattedValue += "".join(list(reversed(item)))
        
        return "{value}.00 {currency}".format(
            currency = self.currency.upper(),
            value = formattedValue
        )