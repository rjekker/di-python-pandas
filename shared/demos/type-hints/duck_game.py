from typing import Protocol

class Weapon(Protocol):
    def shoot(self) -> str:
        raise NotImplementedError

class Gun:
    def shoot(self) -> str:
        return "Bang"

class Laser: # We are NOT inheriting
    def shoot(self) -> str:
        return "dzzzj"


class Player:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        print(self.weapon.shoot())


p = Player(Laser()) # But a Laser IS of type Weapon