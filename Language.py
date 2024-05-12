


class Languages:
    class English(object):
        TYPES_IMMUNE_NAME = "Immune"
    
    def __init__(self, **kwargs):
        self.host_language = self.English()

        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def translate(self, msg):
        return self.host_language.__getattribute__(msg)