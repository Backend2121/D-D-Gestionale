class Spell:
    def __init__(self, effect: str, castingType: str = None, castingTime: str = None, damageType: str = None, damageDice: str = None, extra: str = None) -> None:
        self.castingType = castingType
        self.castingTime = castingTime
        self.effect = effect
        self.damageType = damageType
        self.damageDice = damageDice
        self.extra = extra
