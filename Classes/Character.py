from Classes.Entity import Entity
from PyQt5.QtWidgets import *

from Classes.User import User


class Character(Entity):
    def __init__(self, entityType: str, owner: User, name: str = None, playerName: str = None, adventure: str = None,
                 profilePic: str = None, size: str = None, gameClass: str = None, level: int = None, race: str = None,
                 alignment: str = None, strength: int = None, dexterity: int = None, constitution: int = None,
                 intelligence: int = None, wisdom: int = None, charisma: int = None, armorClass: int = None, speed: int = None,
                 hp: int = None, states: list = [], attacks: dict = None, equip: dict = None,
                 skills: dict = None, extras: str = None):
        
        super().__init__(entityType=entityType, alignment=alignment, name=name, hp=hp, states=states, attacks=attacks,
                         strength=strength, dexterity=dexterity, constitution=constitution, intelligence=intelligence,
                         wisdom=wisdom, charisma=charisma, equip=equip, skills=skills, size=size, profilePic=profilePic,
                         armorClass=armorClass, extras=extras, speed=speed)

        # Attributes unique to Character
        self.gameClass = gameClass
        self.level = level
        self.race = race
        self.playerName = playerName
        self.adventure = adventure
        self.owner = owner
