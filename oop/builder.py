class Soldier:
    def __init__(self):
        self._weapons = list()

    def add_weapon(self, weapon):
        self._weapons.append(weapon)

    def fight(self):
        print(f"Fighting with {', '.join([str(weapon) for weapon in self._weapons])}")


class Sword:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        return f"cool {self._color} sword"


class Shield:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        return f"important {self._color} shield"


class Arch:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        return f"long range {self._color} arch"


class SoldierBuilder:
    def __init__(self, color):
        self._color = color

    def create(self, weapons):
        soldier = Soldier()

        for weapon in weapons:
            if weapon == "sword":
                sword = Sword(self._color)
                soldier.add_weapon(sword)

            elif weapon == "shield":
                shield = Shield(self._color)
                soldier.add_weapon(shield)

            elif weapon == "arch":
                arch = Arch(self._color)
                soldier.add_weapon(arch)

        return soldier


if __name__ == '__main__':
    color1 = input("Enter first soldier's color: ")
    color2 = input("Enter second soldier's color: ")

    first_color_builder = SoldierBuilder(color1)
    second_color_builder = SoldierBuilder(color2)

    soldier1 = first_color_builder.create(["sword", "shield"])
    soldier2 = second_color_builder.create(["sword", "shield"])
    soldier3 = second_color_builder.create(["arch", "shield"])

    soldier1.fight()
    soldier2.fight()
    soldier3.fight()