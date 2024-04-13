import jsonpickle
from Classes.Character import Character
from Classes.Entity import Entity
from Classes.Item import Item
from Classes.User import User
from Classes.Chat import Chat
from Classes.Map import Map
from Utils import generateID
import os

import Utils
from Utils import sendAlert


class Adventure:

    def loadFromDatabase(self, sub: str) -> None:
        """Loads every .json and appends the created object to self.entities"""
        entity: Entity = None
        for path in os.listdir(f"{os.getcwd()}\\DB\\{sub}"):
            if ".json" in path:
                try:
                    with open(f"{os.getcwd()}\\DB\\{sub}\\{path}", "r") as f:
                        entity = jsonpickle.loads(f.read(), classes=Entity)
                except:
                    sendAlert("Error", f"Unable to load: {os.getcwd()}\\DB\\{sub}\\{path}")
                    return
                try:
                    if self.entities != None:
                        add = True
                        for m in self.entities:
                            if m.name == entity.name:
                                add = False
                        if add:
                            if entity.entityType == "Character":
                                if entity.adventure == self.name:
                                    self.entities.append(entity)
                            else:
                                self.entities.append(entity)
                except AttributeError:
                    pass

    def loadEntities(self) -> None:
        # Ensure folder structure
        Utils.createFolderStructure()

        # Load Monsters
        self.loadFromDatabase("Monsters")
        self.loadFromDatabase("NPCs")
        self.loadFromDatabase("Characters")

    def loadItems(self) -> None:
        """Scans DB/Items (if it doesn't exist it creates it) and loads every .json found inside self.items"""
        Utils.directoryExistsCreate(f"{os.getcwd()}\\DB")
        Utils.directoryExistsCreate(f"{os.getcwd()}\\DB\\Items")
        for path in os.listdir(f"{os.getcwd()}\\DB\\Items"):
            if ".json" in path:
                try:
                    with open(f"{os.getcwd()}\\DB\\Items\\{path}", "r") as f:
                        item = jsonpickle.loads(f.read())
                except:
                    sendAlert("Error", f"Unable to load: {os.getcwd()}\\DB\\Items\\{path}")
                    return
                try:
                    if self.items != None:
                        add = True
                        for m in self.items:
                            if m.name == item.name:
                                add = False
                        if add:
                            self.items.append(item)
                except AttributeError:
                    pass

    def loadChat(self) -> None:
        if self.chat != None:
            self.chat.load(self)

    def loadMaps(self) -> None:
        """Scans DB/Maps (if it doesn't exist it creates it) and loads every .json found inside self.maps"""
        Utils.directoryExistsCreate(f"{os.getcwd()}\\DB")
        Utils.directoryExistsCreate(f"{os.getcwd()}\\DB\\Maps")
        for path in os.listdir(f"{os.getcwd()}\\DB\\Maps"):
            if ".json" in path:
                try:
                    with open(f"{os.getcwd()}\\DB\\Maps\\{path}", "r") as f:
                        newMap = jsonpickle.loads(f.read(), classes=Map)
                except:
                    sendAlert("Error", f"Unable to load: {os.getcwd()}\\DB\\Maps\\{path}")
                    return
                try:
                    if self.maps != None:
                        add = True
                        for m in self.maps:
                            if m.name == newMap.name:
                                add = False
                        if add:
                            self.maps.append(newMap)
                except AttributeError:
                    pass

    def __init__(self, name: str = None, owner: User = None, whoami: User = None, entities: list[Entity] = None,
                 items: list[Item] = [], maps: list[Map] = None, chat: Chat = None) -> None:
        # EA Analysis Done
        self.id = generateID()
        self.name = name
        self.owner = owner
        self.whoami = whoami
        self.entities = entities
        self.items = items
        self.maps = maps
        self.chat = chat
        self.loadedMap = None
        self.loadEntities()
        self.loadMaps()
        self.loadChat()
        self.save()

    def save(self) -> None:
        Utils.directoryExistsCreate(f"{os.getcwd()}\\DB")
        Utils.directoryExistsCreate(f"{os.getcwd()}\\DB\\Adventures")
        path = f"{os.getcwd()}\\DB\\Adventures\\{self.name}.json"
        with open(path, "w") as f:
            f.write(jsonpickle.dumps(self, path))
