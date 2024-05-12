
from typing import Any
from Language import Languages
from Time import Tick


class ResistanceTypes(object):
    FIRE: int = 0
    FALL: int = 1
    WATER: int = 2
    NORMAL: int = 3
    HEAVY: int = 4


class DamageTypes(object):
    class __Fire:
        def __init__(self, TICKER: Tick, LANG: Languages) -> None:
            self.TICKER = TICKER
            self.LANGUAGE = LANG

            #self.damage_random = 0.1
            self.damage_multiplier = 1.2
            self.damage_multiplier_falloff = 0.05
            self.continuous_damage = True
            self.continuous_damage_falloff = 0.15
            self.continuous_damage_length = 5 # Ticks
            self.continuous_damage_delay = 20 # Ticks or 1 Second

            self.damage_type = self.LANGUAGE.translate("TYPES_FIRE_DAMAGE")
            self.attack_type = self.LANGUAGE.translate("TYPES_FIRE_ATTACK")

            ##self. # Something Something i cant remember
        
        def doDamageTick(self, entity, target, tick):
            """Does damage every tick

            returns:
             - True: When the damage is givin
             - False: When the damage is finished
            """
            
            if self.continuous_damage and self.TICKER._getTick(tick) <= self.continuous_damage_length:
                do_damage_amount = entity.getDamageAmount() - (entity.getDamageAmount() * (self.continuous_damage_falloff * self.TICKER._getTick(tick)))
                do_damage_amount_after_resistance = do_damage_amount - (do_damage_amount * target.getResistance(ResistanceTypes.FIRE))
                target.damageEntity(do_damage_amount_after_resistance)

                self.TICKER._inc(tick)
                return True
            else:
                self.TICKER._remove(tick)
                return False
            
        
        def attack(self, entity, target):
            do_damage_amount = entity.getDamageAmount() * self.damage_multiplier
            do_damage_amount_after_resistance = do_damage_amount - (do_damage_amount * target.getResistance(ResistanceTypes.FIRE))
            target.damageEntity(do_damage_amount_after_resistance, tick_callback=self.doDamageTick, tick_callback_data=[entity, target, self.TICKER._register(self.__class__)], set_damage_effect=self.LANGUAGE.translate("TYPES_FIRE_EFFECT"))

    class __Normal:
        def __init__(self, TICKER: Tick, LANG: Languages) -> None:
            self.TICKER = TICKER
            self.LANGUAGE = LANG

            #self.damage_random = 0.1
            self.damage_multiplier = 1.0
            self.damage_multiplier_falloff = 0.05

            self.damage_type = self.LANGUAGE.translate("TYPES_FIRE_DAMAGE")
            self.attack_type = self.LANGUAGE.translate("TYPES_FIRE_ATTACK")
            
        
        def attack(self, entity, target):
            do_damage_amount = entity.getDamageAmount() * self.damage_multiplier
            do_damage_amount_after_resistance = do_damage_amount - (do_damage_amount * target.getResistance(ResistanceTypes.NORMAL))
            target.damageEntity(do_damage_amount_after_resistance)

    class __Heavy:
        def __init__(self, TICKER: Tick, LANG: Languages) -> None:
            self.TICKER = TICKER
            self.LANGUAGE = LANG

            self.damage_random = 0.5
            self.damage_multiplier = 1.5
            self.damage_multiplier_falloff = 0.5

            self.damage_type = self.LANGUAGE.translate("TYPES_FIRE_DAMAGE")
            self.attack_type = self.LANGUAGE.translate("TYPES_FIRE_ATTACK")
            
        
        def attack(self, entity, target):
            do_damage_amount = entity.getDamageAmount() * self.damage_multiplier
            do_damage_amount_after_resistance = do_damage_amount - (do_damage_amount * target.getResistance(ResistanceTypes.HEAVY))
            target.damageEntity(do_damage_amount_after_resistance)

    

class HealthTypes(object):
    class IMMUNE:
        def __init__(self, TICKER: Tick, LANG: Languages) -> None:
            self.TICKER = TICKER
            self.LANGUAGE = LANG

            self.name = self.LANGUAGE.translate("TYPES_IMMUNE_NAME")
            self.description = self.LANGUAGE.translate("TYPES_IMMUNE_DESCRIPTION")

            self.resistance = [1.0]*ResistanceTypes.__dict__.__len__()
        
    class NORMAL:
        def __init__(self, TICKER: Tick, LANG: Languages) -> None:
            self.TICKER = TICKER
            self.LANGUAGE = LANG

            self.name = self.LANGUAGE.translate("TYPES_NORMAL_NAME")
            self.description = self.LANGUAGE.translate("TYPES_NORMAL_DESCRIPTION")

            self.resistance = [0.0]*ResistanceTypes.__dict__.__len__()
    