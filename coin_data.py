import websocket
import json
import time

class coin_data:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = []
        self.ws = websocket.WebSocket()

    def connect(self):  #connect to websocket
        ws.connect(f"ws://stream.binance.com:9443/ws/{self.symbol}@aggTrade")

