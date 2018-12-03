import random
import attr


class Stuff:
    def _show(self, itemslot):
        getattr(self, itemslot).display()

    def _equip(self, itemslot, item):
        if type(item) == Item and item.slot.name == itemslot:
            self.stats.strength += item.stats.strength
            self.stats.constitution += item.stats.constitution
            self.stats.dexterity += item.stats.dexterity
            self.stats.intelligence += item.stats.intelligence
            setattr(self, itemslot, item)

    def _remove(self, itemslot):
        item = getattr(self, itemslot)
        self.stats.strength -= item.stats.strength
        self.stats.constitution -= item.stats.constitution
        self.stats.dexterity -= item.stats.dexterity
        self.stats.intelligence -= item.stats.intelligence
        setattr(self, itemslot, Unequiped(slot=itemslot))

    @staticmethod
    def show_item(item):
        print("------------------------------")
        print(f"*** {item.name} ***")
        print(f"    ({item.slot.name})")
        print(f"Force        : +{item.stats.strength} [req.{item.requirements.strength}]")
        print(f"Constitution : +{item.stats.constitution} [req.{item.requirements.constitution}]")
        print(f"Dexterité    : +{item.stats.dexterity} [req.{item.requirements.dexterity}]")
        print(f"Intelligence : +{item.stats.intelligence} [req.{item.requirements.intelligence}]")
        print("------------------------------")

    def show_stuff(self):
        self._show("head")
        self._show("chest")
        self._show("legs")
        self._show("foot")
        self._show("left_hand")
        self._show("right_hand")

    def show_head(self):
        self._show("head")

    def equip_head(self, item):
        self._equip("head", item)

    def remove_head(self):
        self._remove("head")

    def show_chest(self):
        self._show("chest")

    def equip_chest(self, item):
        self._equip("chest", item)

    def remove_chest(self):
        self._remove("chest")

    def show_legs(self):
        self._show("legs")

    def equip_legs(self, item):
        self._equip("legs", item)

    def remove_legs(self):
        self._remove("legs")

    def show_foot(self):
        self._show("foot")

    def equip_foot(self, item):
        self._equip("foot", item)

    def remove_foot(self):
        self._remove("foot")

    def show_left_hand(self):
        self._show("left_hand")

    def equip_left_hand(self, item):
        self._equip("left_hand", item)

    def remove_left_hand(self):
        self._remove("left_hand")

    def show_right_hand(self):
        self._show("right_hand")

    def equip_right_hand(self, item):
        self._equip("right_hand", item)

    def remove_right_hand(self):
        self._remove("right_hand")


@attr.s
class Stats:
    strength = attr.ib(default=0)
    constitution = attr.ib(default=0)
    dexterity = attr.ib(default=0)
    intelligence = attr.ib(default=0)


@attr.s
class Item(Stuff):
    name = attr.ib()
    slot = attr.ib()
    requirements = attr.ib()
    stats = attr.ib()

    def get_stats(self):
        return self.stats

    def display(self):
        print("------------------------------")
        print(f"*** {self.name} ***")
        print(f"    ({self.slot.name})")
        print(f"Force        : +{self.stats.strength} [req.{self.requirements.strength}]")
        print(f"Constitution : +{self.stats.constitution} [req.{self.requirements.constitution}]")
        print(f"Dexterité    : +{self.stats.dexterity} [req.{self.requirements.dexterity}]")
        print(f"Intelligence : +{self.stats.intelligence} [req.{self.requirements.intelligence}]")
        print("------------------------------")


@attr.s
class Unequiped(Stuff):
    slot = attr.ib()
    name = attr.ib(default="Vide")
    requirements = attr.ib(default=Stats(0, 0, 0, 0))
    stats = attr.ib(default=Stats(0, 0, 0, 0))

    @staticmethod
    def display(self):
        print("------------------------------")
        print(f"*** Vide ***")
        print("------------------------------")

    def get_stats(self):
        return self.stats


@attr.s
class Slot:
    name = attr.ib(validator=attr.validators.in_(["head",
                                                  "chest",
                                                  "legs",
                                                  "foot",
                                                  "left_hand",
                                                  "right_hand"]))

    def getname(self):
        return self.name


@attr.s
class Player(Stuff):
    name = attr.ib()
    level = attr.ib(default=1)
    stats = attr.ib(default=Stats(0, 0, 0, 0))
    max_hp = attr.ib(default=100)
    hp = attr.ib(default=100)
    inventory = attr.ib(default=[])
    head = attr.ib(default=Unequiped(slot="head"))
    chest = attr.ib(default=Unequiped(slot="chest"))
    legs = attr.ib(default=Unequiped(slot="legs"))
    foot = attr.ib(default=Unequiped(slot="foot"))
    left_hand = attr.ib(default=Unequiped(slot="left_hand"))
    right_hand = attr.ib(default=Unequiped(slot="right_hand"))

    def __attrs_post_init__(self):
        self.hp = self.max_hp

    def level_up(self):
        self.level += 1

    def display_level(self):
        print(self.name, "is level [", self.level, "]")

    def alter_strength(self, modifier):
        self.stats.strength += modifier

    def alter_hp(self, amount):
        self.hp += amount

    def drink_potion(self):
        self.hp = self.max_hp

    def show_inventory(self):
        for i in self.inventory:
            self.show_item(self.inventory[i])

    def _get_strength(self):
        strength = self.stats.strength
        strength += self.head.stats.strength
        return strength

    def _get_constitution(self):
        constitution = self.stats.constitution
        constitution += self.head.stats.constitution
        return constitution

    def _get_dexterity(self):
        dexterity = self.stats.dexterity
        dexterity += self.head.stats.dexterity
        return dexterity

    def _get_intelligence(self):
        intelligence = self.stats.intelligence
        intelligence += self.head.stats.intelligence
        return intelligence

    def display_stats(self):
        print("***************************")
        print("--- Point de vie [", self.hp, "/", self.max_hp, "]")
        print("Strength :          ", self.stats.strength)
        print("Constitution :      ", self.stats.constitution)
        print("Dexterity :         ", self.stats.dexterity)
        print("Intelligence :      ", self.stats.intelligence)
        print("***************************")


@attr.s(repr=False)
class Fight:
    player = attr.ib()
    monster = attr.ib()

    def __attrs_post_init__(self):
        if self.player.hp > 0:
            self._attack()
        else:
            print(f"{self.player.name} est mort")

    def _attack(self):
        delta_attack = int(self.player.stats.strength * random.random()
                           - self.monster.stats.constitution * random.random())
        if delta_attack > 0:
            self.monster.alter_hp(-delta_attack)
            if self.monster.hp > 0:
                print(f"{self.player.name} enlève {delta_attack}hp à {self.monster.name}")
                self._defend()
            else:
                print(f"{self.player.name} enlève {delta_attack}hp à {self.monster.name} et le tue")
                print(f"{self.player.name} gagne le combat")
        else:
            print(f"{self.player.name} rate son attaque sur {self.monster.name}")
            self._defend()

    def _defend(self):
        delta_attack = int(self.monster.stats.strength * random.random()
                           - self.player.stats.constitution * random.random())
        if delta_attack > 0:
            self.player.alter_hp(-delta_attack)
            if self.player.hp > 0:
                print(f"{self.monster.name} enlève {delta_attack}hp à {self.player.name}")
                self._attack()
            else:
                self.player.hp = 0
                print(f"{self.monster.name} enlève {delta_attack}hp à {self.player.name} et le tue")
                print(f"{self.monster.name} gagne le combat")
        else:
            print(f"{self.monster.name} rate son attaque sur {self.player.name}")
            self._attack()

    def pick_loots(self):
        number_loots = random.randint(0, 3)
        for i in range(number_loots):
            self._generate_loot()

    @staticmethod
    def _generate_loot(self):
        return Item("Heaume du débutant", Slot("head"), Stats(12, 0, 10, 6), Stats(3, 0, 7, 0))

    def end_fight(self):
        if self.player.stats.strength >= self.monster.stats.strength:
            print(f"{self.player.name} gagne le combat")
        else:
            print(f"{self.monster.name} gagne le combat")


@attr.s
class Monster:
    name = attr.ib()
    level = attr.ib()
    stats = attr.ib()
    hp = attr.ib()

    def get_stats(self):
        return self.stats

    def alter_hp(self, amount):
        self.hp += amount


beginnerHead = Item("Heaume du débutant", Slot("head"), Stats(12, 0, 10, 6), Stats(3, 18, 7, 0))
beginnerChest = Item("Plastron du débutant", Slot("chest"), Stats(12, 0, 10, 6), Stats(5, 21, 12, 0))
beginnerLegs = Item("Jambières du débutant", Slot("legs"), Stats(12, 0, 10, 6), Stats(4, 8, 7, 0))
beginnerFoot = Item("Sandales du débutant", Slot("foot"), Stats(12, 0, 10, 6), Stats(3, 5, 5, 0))
beginnerSword = Item("Epée du débutant", Slot("right_hand"), Stats(12, 0, 10, 6), Stats(43, 0, 5, 0))
beginnerShield = Item("Bouclier du débutant", Slot("left_hand"), Stats(12, 0, 10, 6), Stats(0, 15, 10, 0))

jacky = Player("Jacky le guerrier", 1, Stats(10, 12, 11, 13), 400)

jacky.equip_head(beginnerHead)
jacky.equip_chest(beginnerChest)
jacky.equip_legs(beginnerLegs)
jacky.equip_foot(beginnerFoot)
jacky.equip_right_hand(beginnerSword)
jacky.equip_left_hand(beginnerShield)


gobelin1 = Monster("Toto le gobelin", 2, Stats(86, 4, 5, 0), 336)
gobelin2 = Monster("Gérard le grand gobelin", 2, Stats(93, 4, 5, 0), 236)
ogre1 = Monster("Pascal l'ogre puant", 2, Stats(110, 4, 5, 0), 150)

Fight(jacky, gobelin1)
Fight(jacky, gobelin2)
Fight(jacky, ogre1)

jacky.display_stats()