import time

class Tick:

    def __init__(self):
        self.id = "Tick"
        self.ticks = 0
        self.tick_timers = {}

    def __str__(self, tick_id) -> int:
        return self.tick_timers[tick_id]
    
    def _inc(self, tick_id):
        self.tick_timers[tick_id] += 1
    
    def _dec(self, tick_id) -> int:
        self.tick_timers[tick_id] -= 1
    
    def _get(self, tick_id):
        return self.tick_timers[tick_id]
    
    def _reset(self, tick_id):
        self.tick_timers[tick_id] = 0
    
    def _remove(self, tick_id):
        del self.tick_timers[tick_id]

    def _getTotalTicks(self) -> int:
        return self.ticks
    
    def _register(self, tick_id):
        self.tick_timers[tick_id] = 0
        return tick_id
    
    def tick(self, target_tick_time) -> None:
        start = time.time()
        for ticker, v in self.tick_timers.items():
            self._inc(ticker)
        self.ticks += 1
        time.sleep(target_tick_time)
        return time.time() - start