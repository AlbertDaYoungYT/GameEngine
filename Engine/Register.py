


class Register:

    def __init__(self):
        self.id = "Register"
        self.register = {}
    
    def register(self, name, value):
        self.register[name] = value
    
    def get(self, name):
        return self.register[name]
    
    def get_all(self):
        return self.register.values()
    
    
    def update(self):
        for k, v in self.register.items():
            v.update(k)
    
