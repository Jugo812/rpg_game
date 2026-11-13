from __future__ import annotations
from abc import ABC, abstractmethod
from core.exceptions import 

class Character(ABC):
    def __init__(self, hp: float, max_hp: float, mana: int):
        self._hp = hp
        self._hp_max = _hp_max
        self._mana = mana

    def take_damage(self, amount_of_damage: float):
        self._hp -= amount_of_damage
    
    def heal(self, amount: float):
        self._hp = self._hp + amount if self._hp + amount < self._hp_max else self._hp_max
