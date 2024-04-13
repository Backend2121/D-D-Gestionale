from Utils import generateID
import os
import jsonpickle


class Item:

    def save(self) -> None:
        """Creates the containing folder and the {item.name}.json itself"""
        if not os.path.exists(f"{os.getcwd()}\\DB\\Items"):
            os.mkdir(f"{os.getcwd()}\\DB\\Items\\")

        with open(f"{os.getcwd()}\\DB\\Items\\{self.name}.json", 'w') as f:
            f.write(jsonpickle.dumps(self))

    def __init__(self, name: str = None, description: str = None, itemType=None, profilePic: str = None) -> None:
        self.id = generateID()
        self.name = name
        self.profilePic = profilePic
        self.description = description
        self.type = itemType
