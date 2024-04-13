import os.path
import unittest
from Classes.Entity import Entity
from Classes.Character import Character
from Classes.Item import Item
from Utils import createFolderStructure


class Tester(unittest.TestCase):
    def testSaveMonster(self) -> None:
        m = Entity(entityType="Monster")
        # save() is the tested function
        m.save()
        assert (os.path.exists(f"{os.getcwd()}\\DB\\Monsters\\{m.name}.json"))
        os.remove(f"{os.getcwd()}\\DB\\Monsters\\{m.name}.json")

    def testSaveNPC(self) -> None:
        m = Entity(entityType="NPC")
        # save() is the tested function
        m.save()
        assert (os.path.exists(f"{os.getcwd()}\\DB\\NPCs\\{m.name}.json"))
        os.remove(f"{os.getcwd()}\\DB\\NPCs\\{m.name}.json")

    def testSaveItem(self) -> None:
        m = Item()
        # save() is the tested function
        m.save()
        assert (os.path.exists(f"{os.getcwd()}\\DB\\Items\\{m.name}.json"))
        os.remove(f"{os.getcwd()}\\DB\\Items\\{m.name}.json")

    def testSaveCharacter(self) -> None:
        m = Character(entityType="Character")
        # save() is the tested function
        m.save()
        assert (os.path.exists(f"{os.getcwd()}\\DB\\Characters\\{m.name}.json"))
        os.remove(f"{os.getcwd()}\\DB\\Characters\\{m.name}.json")

    def testFolderStructure(self) -> None:
        assert createFolderStructure()
