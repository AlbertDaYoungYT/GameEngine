

class InbuiltEvents(object):
    ENGINE_STARTED: int = 0
    GAME_LOADED: int = 1
    SCENE_LOADING: int = 2
    ENGINE_SHUTTING_DOWN: int = 3
    ENGINE_SAVING: int = 4
    ENGINE_FIRST_START: int = 5
    

class Event:

    def __init__(self) -> None:
        self.id = "EventHandler"
        self.events = {}
        self.event_reqs = {}
    
    def add(self, event_id, name, callback, requirements=None):
        self.events[event_id][name] = callback
        self.event_reqs[event_id] = requirements

    def create(self, event_id):
        self.events[event_id] = {}
    
    def remove(self, event):
        self.events.pop(event)
        self.event_reqs.pop(event)
    
    def trigger(self, event_id, name):
        self.events[event_id][name](event_id)
    
    def update(self, event_id, data):
        if self.event_reqs[event_id] == data:
            for k, v in self.events[event_id].items():
                self.trigger(event_id, k)