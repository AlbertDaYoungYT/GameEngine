from Engine.Language import Language

class Item:
    def __init__(self, id: str, attr=None):
        if attr == None:    
            self.rarity = 0
            self.max_stack = 50
        else:
            for k, v in attr.__dict__.items():
                setattr(self, k, v)

        self.LANG = Language()

        self.id = id
        self.name = self.LANG.translate(f"ITEM_NAME_{id.upper()}")
        self.description = self.LANG.translate(f"ITEM_DESCRIPTION_{id.upper()}")
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.id
    
    def _setRarity(self, value):
        self.rarity = value
        return self
    
    def _getRarity(self):
        return self.rarity
    
    def _setMaxStack(self, value):
        self.max_stack = value
        return self
    
    def _getMaxStack(self):
        return self.max_stack
    
    def copyOf(self, other):
        return Item(self.id, attr=other)
    
class ItemStack(Item):
    def __init__(self, id, amount) -> None:
        self.id = id

        self.stack: Item = Item(id)
        self.amount = amount
    
    def __str__(self):
        return self.id
    
    def _getStack(self):
        return self.stack*self.amount
    
    def _setStack(self, value):
        self.amount = value
    
    def _takeHalf(self):
        self.amount = int(round(self.amount/2, 0))
        return ItemStack(self.id, int(round(self.amount/2, 0)))


class Items(object):
    IRON_NUGGET: Item = Item("iron_nugget")._setMaxStack(100)._setRarity(1)
#    GOLD_NUGGET: Item = Item("gold_nugget").copyOf(IRON_NUGGET)._setRarity(2)
#    DIAMOND: Item = Item("diamond").copyOf(IRON_NUGGET)._setRarity(5)


