import websocket
import json
import time
import numpy as np
import matplotlib.pyplot as plt
import threading


class coin_data:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = []
        self.position_open = False
        self.ws = websocket.WebSocket()

    def connect(self):  #connect to websocket
        self.ws.connect(f"wss://stream.binance.com:9443/ws/{self.symbol}@aggTrade")
        if self.ws.connected:
            self.position_open = True
        else:
            raise Exception("error connecting with data")

    def price(self):    #return price
        data = json.loads(self.ws.recv())
        return float(data["p"])

    def stream_fn(self):   #save live data to data. Must be threaded to avoid problems
        while self.position_open:
            data = json.loads(self.ws.recv())
            self.data.append(float(data['p']))
            print(self.data)
            time.sleep(1)

    def stream(self):
        thread = threading.Thread(target=self.stream_fn)
        thread.start()

   #TODO
    def plot_price(self):
        return
     
    def close(self):
        self.position_open = False
        self.ws.close()
