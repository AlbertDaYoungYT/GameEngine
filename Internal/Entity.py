import Internal


from typing import Any, Dict, Optional, Union

from Internal.Item import ItemStack
import Internal.Types
from Engine.Language import Language
from Internal.Inventory import Inventory
from Engine.Time import Tick


class Entity:
    class Meta:
        pass
    class Inventory(Inventory):
        def __init__(self, id) -> None:
            self.inventory_id = id
            super().__init__()
        
        def __repr__(self) -> str:
            return "".format(self.inventory_id)
        
        def __eq__(self, other) -> bool:
            return self.inventory_id == other.inventory_id
        
    class Hand:
        def __init__(self, id):
            self.id = id
            self.in_hand = self.inventory.hand

        def __repr__(self) -> str:
            return "".format(self.id)
        
        def _getHand(self) -> ItemStack:
            return self.Inventory(self.id).hand
        
        def _setHand(self, itemStack: ItemStack) -> None:
            self.inventory.hand = itemStack

    def __init__(self, TICKER: Tick, LANG: Language, id, attr=None):
        if attr == None:
            self.health = 100
            self.health_type = Internal.Types.HealthTypes.NORMAL(self.TICKER, self.LANGUAGE)

            self.inventory: Inventory = Inventory(id)
        else:
            for k, v in attr.__dict__.items():
                setattr(self, k, v)
        
        self.TICKER = TICKER
        self.LANGUAGE = LANG

        self.id = id
        self.name = self.LANGUAGE.translate(f"ENTITY_{self.id}_NAME")
        self.description = self.LANGUAGE.translate(f"ENTITY_{self.id}_DESCRIPTION")

        self.inventory = Inventory(self.id)
        self.hand = self.Hand(self.id)

        self.damage_effect = None
        self.damage_tick_callback = None
        self.damage_tick_callback_data = None

    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.id
    
    def _dropEntityInventory(self):
        return self.inventory._clear(drop=True)
    
    def _entityDead(self):
        self.health = 0
    
    def _isEntityDead(self):
        return self.health == 0
    
    def damageEntity(self, damage: float, tick_callback=None, tick_callback_data=None, set_damage_effect=None):
        self.damage_effect = set_damage_effect
        self.damage_tick_callback = tick_callback
        self.damage_tick_callback_data = tick_callback_data

        if self.health - damage < 0: self._entityDead()
        else:
            self.health -= int(round(damage, 0))
    
    def update(self):
        if self._isEntityDead():
            self._dropEntityInventory()
        if self.damage_tick_callback != None:
            self.damage_tick_callback(*self.damage_tick_callback_data)


    
    def copyOf(self, other):
        return Entity(self.TICKER, self.LANGUAGE, self.id, attr=other)