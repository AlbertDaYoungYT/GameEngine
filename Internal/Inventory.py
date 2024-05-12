
from Internal.Item import ItemStack

class Inventory(object):
    def __init__(self, inventory_id) -> None:
        self.inventory_id = inventory_id

        self.size = [8, 2]
        self.inventory = [None*self.size[0]]*self.size[1]
    
    def __str__(self) -> str:
        return str(self.inventory_id)
    
    def __eq__(self, other) -> bool:
        return self.inventory_id == other.inventory_id
    
    def _clear(self, drop=False):
        if drop:
            inv = self.inventory
            self.inventory = [None*self.size[0]]*self.size[1]
            return inv
        self.inventory = [None*self.size[0]]*self.size[1]
    
    def _setInventory(self, loc: list[int, int], itemStack: ItemStack):
        self.inventory[loc[0]][loc[1]] = itemStack
    
    def _getInventory(self):
        return self.inventory