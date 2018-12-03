import random
import attr

class Character:
    def level_up(self):
        self._level += 1
    def display_level(self):
        print(self._name, "is level [", self._level, "]")
    def alterate_strength(self, modifier):
        self._stats._strength += modifier
    def alterate_pv(self, amount):
        self._pv += amount
    def drink_potion(self):
        self._pv = self._pvmax


class Stuff:
    def _show(self, itemSlot):
        getattr(self, itemSlot).display()
    def _equip(self, itemSlot, item):
        if type(item) == Item and item._slot._name == itemSlot:
            setattr(self, itemSlot, item)
    def _remove(self, itemSlot):
        setattr(self, itemSlot, Unequiped(slot = itemSlot))

    def show_inventory(self):
        for i in self._inventory:
            show_item(self._inventory[i])
            
    def show_item(self, item):
        print("------------------------------")
        print(f"*** {item._name} ***")
        print(f"    ({item._slot._name})")
        print(f"Force        : +{item._stats._strength} [req.{item._requirements._strength}]")
        print(f"Constitution : +{item._stats._constitution} [req.{item._requirements._constitution}]")
        print(f"Dexterité    : +{item._stats._dexterity} [req.{item._requirements._dexterity}]")
        print(f"Intelligence : +{item._stats._intelligence} [req.{item._requirements._intelligence}]")
        print("------------------------------")

    def show_stuff(self):
        self._show("_head")
        self._show("_chest")
        self._show("_legs")
        self._show("_foot")
        self._show("_leftHand")
        self._show("_rightHand")

    def show_head(self):
        self._show("_head")
    def equip_head(self, item):
        self._equip("_head", item)
    def remove_head(self):
        self._remove("_head")

    def show_chest(self):
        self._show("_chest")
    def equip_chest(self, item):
        self._equip("_chest", item)
    def remove_chest(self):
        self._remove("_chest")

    def show_legs(self):
        self._show("_legs")
    def equip_legs(self, item):
        self._equip("_legs", item)
    def remove_legs(self):
        self._remove("_legs")

    def show_foot(self):
        self._show("_foot")
    def equip_foot(self, item):
        self._equip("_foot", item)
    def remove_foot(self):
        self._remove("_foot")

    def show_leftHand(self):
        self._show("_leftHand")
    def equip_leftHand(self, item):
        self._equip("_leftHand", item)
    def remove_leftHand(self):
        self._remove("_leftHand")

    def show_rightHand(self):
        self._show("_rightHand")
    def equip_rightHand(self, item):
        self._equip("_rightHand", item)
    def remove_rightHand(self):
        self._remove("_rightHand")


@attr.s
class Stats:
    _strength = attr.ib(default=0)
    _constitution = attr.ib(default=0)
    _dexterity = attr.ib(default=0)
    _intelligence = attr.ib(default=0)


@attr.s
class Item(Stuff):
    _name = attr.ib()
    _slot = attr.ib()
    _requirements = attr.ib()
    _stats = attr.ib()

    def get_stats(self):
        return self._stats
        
    def display(self):
        print("------------------------------")
        print(f"*** {self._name} ***")
        print(f"    ({self._slot._name})")
        print(f"Force        : +{self._stats._strength} [req.{self._requirements._strength}]")
        print(f"Constitution : +{self._stats._constitution} [req.{self._requirements._constitution}]")
        print(f"Dexterité    : +{self._stats._dexterity} [req.{self._requirements._dexterity}]")
        print(f"Intelligence : +{self._stats._intelligence} [req.{self._requirements._intelligence}]")
        print("------------------------------")
        

@attr.s
class Unequiped(Stuff):
    _slot = attr.ib()
    _name = attr.ib(default="Vide")
    _requirements = attr.ib(default=Stats(0, 0, 0, 0))
    _stats = attr.ib(default=Stats(0, 0, 0, 0))

    def display(self):
        print("------------------------------")
        print(f"*** Vide ***")
        print("------------------------------")
        
    def get_stats(self):
        return self._stats


@attr.s
class Slot:
    _name = attr.ib(validator=attr.validators.in_(["_head",
                                                   "_chest",
                                                   "_legs",
                                                   "_foot",
                                                   "_leftHand",
                                                   "_rightHand"]))
        
    def get_name(self):
        return self._name


@attr.s
class Player(Character, Stuff):
    _name = attr.ib()
    _level = attr.ib(default=1)
    _stats = attr.ib(default=Stats(0, 0, 0, 0))
    _pvmax = attr.ib(default=100)
    _pv = attr.ib(default=100)
    _inventory = attr.ib(default=[])
    _head = attr.ib(default=Unequiped(slot = "_head"))
    _chest = attr.ib(Unequiped(slot = "_chest"))
    _legs = attr.ib(Unequiped(slot = "_legs"))
    _foot = attr.ib(Unequiped(slot = "_foot"))
    _leftHand = attr.ib(Unequiped(slot = "_leftHand"))
    _rightHand = attr.ib(Unequiped(slot = "_rightHand"))
        
    def _get_strength(self):
        strength = self._stats._strength
        strength += self._head._stats._strength
        return strength
    
    def _get_constitution(self):
        constitution = self._stats._constitution
        constitution += self._head._stats._constitution
        return constitution
    
    def _get_dexterity(self):
        dexterity = self._stats._dexterity
        dexterity += self._head._stats._dexterity
        return dexterity
    
    def _get_intelligence(self):
        intelligence = self._stats._intelligence
        intelligence += self._head._stats._intelligence
        return intelligence
        
    def display_stats(self):
        print("***************************")
        print("--- Point de vie [", self._pv, "/", self._pvmax, "]")
        print("Strength :          ", self._stats._strength)
        print("Constitution :      ", self._stats._constitution)
        print("Dexterity :         ", self._stats._dexterity)
        print("Intelligence :      ", self._stats._intelligence)
        print("***************************")


@attr.s(repr=False)
class Fight:
    player = attr.ib()
    monster = attr.ib()

    def __attrs_post_init__(self):
        self._attack()
    
    def _attack(self):
        self.monster.alterate_pv(-self.player._stats._strength)
        if self.monster._pv > 0:
            print(f"{self.player._name} enlève {self.player._stats._strength}PV à {self.monster._name}")
            self._defend()
        else:
            print(f"{self.player._name} enlève {self.player._stats._strength}PV à {self.monster._name} et le tue")
            print(f"Player win")
        
    def _defend(self):
        self.player.alterate_pv(-self.monster._stats._strength)
        if self.player._pv > 0:
            print(f"{self.monster._name} enlève {self.monster._stats._strength}PV à {self.player._name}")
            self._attack()
        else:
            print(f"{self.monster._name} enlève {self.monster._stats._strength}PV à {self.player._name} et le tue")
            print(f"Monster win")

    def pick_loots(self):
        numbre_loots = random.randint(0,3)
        for i in range(numbre_loots):
            self._generate_loot()
    
    def _generate_loot(self):
        return Item("Heaume du débutant", Slot("_head"), Stats(12, 0, 10, 6), Stats(3, 0, 7, 0))
    
    def end_fight(self):
        if self.player._stats._strength >= self.monster._stats._strength:
            print(f"{self.player._name} win")
        else:
            print(f"{self.monster._name} win")
    

@attr.s
class Monster(Character):
    _name = attr.ib()
    _level = attr.ib()
    _stats = attr.ib()
    _pv = attr.ib()
        
    def get_stats(self):
        return self._stats
    


beginnerHead = Item("Heaume du débutant", Slot("_head"), Stats(12, 0, 10, 6), Stats(3, 0, 7, 0))
beginnerChest = Item("Plastron du débutant", Slot("_chest"), Stats(12, 0, 10, 6), Stats(5, 0, 12, 0))
beginnerLegs = Item("Jambières du débutant", Slot("_legs"), Stats(12, 0, 10, 6), Stats(4, 0, 7, 0))
beginnerFoot = Item("Sandales du débutant", Slot("_foot"), Stats(12, 0, 10, 6), Stats(3, 0, 5, 0))
beginnerSword = Item("Epée du débutant", Slot("_rightHand"), Stats(12, 0, 10, 6), Stats(8, 0, 5, 0))
beginnerShield = Item("Bouclier du débutant", Slot("_leftHand"), Stats(12, 0, 10, 6), Stats(0, 0, 10, 0))

jacky = Player("Jacky le guerrier", 1, Stats(10,12,11,13), 40)

jacky.equip_head(beginnerHead)
jacky.equip_chest(beginnerChest)
jacky.equip_legs(beginnerLegs)
jacky.equip_foot(beginnerFoot)
jacky.equip_rightHand(beginnerSword)
jacky.equip_leftHand(beginnerShield)

gobelin1 = Monster("Toto le gobelin", 2, Stats(6,4,5,0), 36)
gobelin2 = Monster("Gérard le grand gobelin", 2, Stats(6,4,5,0), 36)
ogre1 = Monster("Pascal l'ogre puant'", 2, Stats(9,4,5,0), 50)

Fight(jacky, gobelin1)
Fight(jacky, gobelin2)
jacky.display_stats()
jacky.drink_potion()
jacky.display_stats()
Fight(jacky, ogre1)
