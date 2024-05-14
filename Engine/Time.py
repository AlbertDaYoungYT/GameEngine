import threading
import time


def ms(x):
    return x * 1000

class Tick:

    def __init__(self):
        self.id = "Ticker"
        self.proc_time = time.time()
        self.proc_tick = 0
        self.tickers = {}
        self.ticker_procs = {}
        self.ticker_offset = {}
        self.ticker_callback = {}

        self.tickers_count = 0
        self.calculated_system_tickrate_time = 0.0

    def __str__(self):
        return self.id
    
    def _get(self, id):
        return self.tickers[id]
    
    def _register(self, id, offset, callback=None):
        self.tickers[id] = 1
        self.ticker_procs[id] = 1
        self.ticker_offset[id] = offset
        if callback is not None:
            self.ticker_callback[id] = callback
        self.tickers_count += 1
    
    def _getTickTime(self):
        return self.calculated_system_tickrate_time
    
    def tick(self, target_tick_time):
        start = time.time()
        for ticker, v in self.tickers.items():
            offset = self.ticker_offset[ticker]
            if offset // self.ticker_procs[ticker] == 0:
                self.tickers[ticker] += 1
                self.ticker_procs[ticker] = 1
                self.ticker_callback[ticker](self, ticker, v)
        for ticker, v in self.ticker_procs.items():
            self.ticker_procs[ticker] += 1
        self.proc_tick += 1
        self.calculated_system_tickrate_time = ms(time.time() - start)
        time.sleep(target_tick_time)
        return self.calculated_system_tickrate_time



if __name__ == "__main__":
    def callback_test(_self, t, v):
        print(ms(time.time() - _self.proc_time), t, v)
        exit(0)
    T = Tick("Test")
    T._register("Tester1", 20, callback=callback_test)
    while True:
        T.tick()
        print(T.proc_tick, T._get("Tester1"), T._getTickTime())