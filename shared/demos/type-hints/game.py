class Weapon:
    def shoot(self) -> str:
        raise NotImplementedError


class Gun(Weapon):
    def shoot(self) -> str:
        return "Bang"


class Laser(Weapon):
    def shoot(self) -> str:
        return "dzzzj"


class Player:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(self.weapon.shoot())


p = Player("Reindert", Laser())