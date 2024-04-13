from Utils import generateID

class Tile:
    def __init__(self,  coords: tuple[int, int], image: str = None, terrainType: str = None, occupiedBy = None) -> None:
        self.id = generateID()
        self.image = image
        self.terrainType = terrainType
        self.coords = coords
        self.occupiedBy = occupiedBy