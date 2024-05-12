import json


class Language:
    def __init__(self, **kwargs):
        self.id = "Language"
        self.lang = kwargs.get("language") if kwargs.get("language") else "en_US"
        self.lang_file = json.loads(open(f"./Resources/Lang/{self.lang}.json", "r").read())
        for k, w in self.lang_file.items():
            setattr(self, k, w)

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        return self.lang
    
    def _getLanguage(self):
        return self.lang
        
    def translate(self, msg):
        return self.__getattribute__(msg)