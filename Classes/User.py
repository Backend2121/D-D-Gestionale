from Utils import generateID
import os
import jsonpickle


class User:

    def addCharacter(self, char) -> None:
        if len(self.charactersList) == 0:
            print("Len is 0")
            self.charactersList.append(char)
            self.save()
            print("Saved")
            return
        for a in self.charactersList:
            if char.name != a.name:
                self.charactersList.append(char)
        self.save()
                
    def removeCharacter(self, charName: str) -> None:
        for a in self.charactersList:
            if charName != a.name:
                print(f"charName: {charName}\n a.name: {a.name}")
                self.charactersList.remove(a)
        self.save()

    def removeAdventure(self, advName: str) -> None:
        for a in self.adventuresList:
            if advName == a.name:
                print(f"AdvName: {advName}\n a.name: {a.name}")
                self.adventuresList.remove(a)
        self.save()

    def addAdventure(self, adv) -> None:
        if len(self.adventuresList) == 0:
            self.adventuresList.append(adv)
            self.save()
            return
        for a in self.adventuresList:
            if adv.name != a.name:
                self.adventuresList.append(adv)
        self.save()

    def save(self) -> None:
        with open(f"{os.getcwd()}\\DB\\Users\\{self.name}.json", "w") as f:
            f.write(jsonpickle.dumps(self))

    def load(self) -> None:
        try:
            u: User = None
            with open(f"{os.getcwd()}\\DB\\Users\\{self.name}.json", "r") as f:
                u = jsonpickle.loads(f.read())
            self.id = u.id
            self.name = u.name
            self.adventuresList = u.adventuresList
            self.charactersList = u.charactersList
        except Exception as e:
            print(e)
            with open(f"{os.getcwd()}\\DB\\Users\\{self.name}.json", "w") as f:
                f.write(jsonpickle.dumps(self))

    def __init__(self, name: str, adventuresList: list = [], charactersList: list = []) -> None:
        self.id = generateID()
        self.name = name
        self.adventuresList = adventuresList
        self.charactersList = charactersList
