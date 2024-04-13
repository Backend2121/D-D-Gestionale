from Utils import generateID
from Classes.Tile import Tile
import os
import jsonpickle
from Utils import directoryExistsCreate


class Map:
    def __init__(self, name: str = None, size: tuple[int, int] = None, tileList: list[list[Tile]] = None,
                 weather: str = None) -> None:
        self.id = generateID()
        self.name = name
        self.size = size
        self.tileList = tileList
        self.weather = weather
        self.tilePalette = []
        directoryExistsCreate(f"{os.getcwd()}\\DB")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Images")
        for image in os.listdir(f"{os.getcwd()}\\DB\\Images"):
            self.tilePalette.append(f"DB/Images/{image}")

    def save(self) -> None:
        directoryExistsCreate(f"{os.getcwd()}\\DB")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Maps")
        with open(f"{os.getcwd()}\\DB\\Maps\\{self.name}.json", 'w') as f:
            print("Saving map")
            f.write(jsonpickle.dumps(self))
