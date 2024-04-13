class Armour:
    def __init__(self, AC: int, extras: str = None, resistances: str = None) -> None:
        self.AC = AC
        self.extras = extras
        self.resistances = resistances
        