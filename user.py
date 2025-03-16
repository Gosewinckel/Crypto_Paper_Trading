import coin_data
import coins
import threading

class User:
    def __init__(self):
        self.USD = 50000
        self.coins = {}
        self.assets = 50000
        self.coin_streams = []
        self.coin_data = {}

    def deposit(self, amount):
        if amount <= 0:
            raise Exeption("amount must be positive")
        self.USD += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.USD:
            raise Exception("must enter a valid amount")
        self.USD -= amount

    def buy(self, coin, amount):
        if coin is not in coins.coins:
            raise Exception("coin is not available or does not exist")
        crypto = coin_data.coin_data(coins.coins[coin])
        self.coin_data[coin] = crypto
        crypto.connect()
        if crypto.price() * amount > self.USD:
            raise Exception("insufficient funds")
        self.USD -= crypto.price()*amount
        crypto.stream()
        self.coin_streams.append(crypto.data)
        self.coins[coin] += amount

    def sell(self, coin, amount):
        if coin is not in self.coins.keys():
            raise Exception("you don't own this coin")
        if amount > self.coins[coin]:
            raise Exception("enter valid amount")
        self.USD += self.coins[coin].price()*amount
        self.coins[coin] -= amount
        self.coin_streams.remove()
        self.coin_data[coin].close()

    def total_assets(self):
        total = self.USD
        for coin in self.coin_data:
            total += coin.price()
        return total
