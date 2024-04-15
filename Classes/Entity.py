import os
from Utils import generateID
import jsonpickle
from PyQt5.QtGui import QPixmap
from Utils import directoryExistsCreate, validateName


class Entity:

    def setHp(self, amount: int) -> None:
        if amount == None:
            return
        self.hp -= amount

    def setState(self, state: str) -> None:
        if '+' in state:
            self.states.append(state.replace('+', ''))
        else:
            self.states.remove(state.replace('-', ''))

    def save(self) -> None:
        """Creates the containing folder and the .json of the entity, also functions as the .json updater"""
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Monsters")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\NPCs")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Characters")
        match self.entityType:
            case "Monster":
                with open(f"{os.getcwd()}\\DB\\Monsters\\{self.name}.json", 'w') as f:
                    f.write(jsonpickle.dumps(self))
            case "NPC":
                with open(f"{os.getcwd()}\\DB\\NPCs\\{self.name}.json", 'w') as f:
                    f.write(jsonpickle.dumps(self))
            case "Character":
                with open(f"{os.getcwd()}\\DB\\Characters\\{self.name}.json", 'w') as f:
                    f.write(jsonpickle.dumps(self))
                
    def __init__(self, entityType: str, alignment: str = None, name: str = None, hp: int = None, speed: int = None, states: list = [], armorClass: int = None, attacks: dict = None, strength: int = None, dexterity: int = None, constitution: int = None,
                 intelligence: int = None, wisdom: int = None, charisma: int = None, equip: dict = None, skills: dict = None, size: str = None,
                 profilePic: str = None, extras: dict = None) -> None:
        self.id = generateID()
        self.entityType = entityType
        self.name = name
        self.hp = hp
        self.maxHp = hp
        self.speed = speed
        self.states = states
        self.armorClass = armorClass
        self.alignment = alignment 
        self.size = size
        self.profilePic = profilePic

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.attacks = attacks
        self.equip = equip
        self.skills = skills
        self.extras = extras
