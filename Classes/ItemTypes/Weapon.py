class Weapon:
    def __init__(self, damageType: str, damageDice: str, extras: str = None) -> None:
        self.damageType = damageType
        self.damageDice = damageDice
        self.extras = extras
