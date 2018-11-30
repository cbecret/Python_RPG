import random

class Character:
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def level_up(self):
        self._level += 1
    def display_level(self):
        print(self._name, "is level [", self.get_level(), "]")
    def alterate_strength(self, modifier):
        self._stats._strength += modifier
    def get_pvmax(self):
        return self._pvmax
    def get_pv(self):
        return self._pv
    def alterate_pv(self, amount):
        self._pv += amount
    def drink_potion(self):
        self._pv = self.get_pvmax()


class Stuff:
    def _get(self, itemSlot):
        return self[itemSlot]
    def _show(self, itemSlot):
        getattr(self, itemSlot).display()
    def _equip(self, itemSlot, item):
        if type(item) == Item and item._slot.get_name() == itemSlot:
            setattr(self, itemSlot, item)
    def _remove(self, itemSlot):
        setattr(self, itemSlot, Unequiped(slot = itemSlot))

    def show_inventory(self):
        for i in self._inventory:
            show_item(self._inventory[i])
            
    def show_item(self, item):
        print("------------------------------")
        print(f"*** {item._name} ***")
        print(f"    ({item._slot.get_name()})")
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
 
    def get_head(self):
        return self._get("_head")
    def show_head(self):
        self._show("_head")
    def equip_head(self, item):
        self._equip("_head", item)
    def remove_head(self):
        self._remove("_head")
        
    def get_chest(self):
        return self._get("_chest")
    def show_chest(self):
        self._show("_chest")
    def equip_chest(self, item):
        self._equip("_chest", item)
    def remove_chest(self):
        self._remove("_chest")
        
    def get_legs(self):
        return self._get("_legs")
    def show_legs(self):
        self._show("_legs")
    def equip_legs(self, item):
        self._equip("_legs", item)
    def remove_legs(self):
        self._remove("_legs")
        
    def get_foot(self):
        return self._get("_foot")
    def show_foot(self):
        self._show("_foot")
    def equip_foot(self, item):
        self._equip("_foot", item)
    def remove_foot(self):
        self._remove("_foot")
        
    def get_leftHand(self):
        return self._get("_leftHand")
    def show_leftHand(self):
        self._show("_leftHand")
    def equip_leftHand(self, item):
        self._equip("_leftHand", item)
    def remove_leftHand(self):
        self._remove("_leftHand")
        
    def get_rightHand(self):
        return self._get("_rightHand")
    def show_rightHand(self):
        self._show("_rightHand")
    def equip_rightHand(self, item):
        self._equip("_rightHand", item)
    def remove_rightHand(self):
        self._remove("_rightHand")


class Stats:
    def __init__(self, strength = 0, constitution = 0, dexterity = 0, intelligence = 0):
        self._strength = strength
        self._constitution = constitution
        self._dexterity = dexterity
        self._intelligence = intelligence
        
    def get_strength(self):
        return self._strength


class Item(Stuff):
    def __init__(self, name, slot, requirements = Stats(), stats = Stats()):
        self._name = name
        if type(slot) == Slot:
            self._slot = slot
        self._requirements = requirements
        self.__stats = stats
        
    def get_stats(self):
        return self.__stats
        
    def display(self):
        print("------------------------------")
        print(f"*** {self._name} ***")
        print(f"    ({self._slot.get_name()})")
        print(f"Force        : +{self.get_stats._strength} [req.{self._requirements._strength}]")
        print(f"Constitution : +{self.get_stats._constitution} [req.{self._requirements._constitution}]")
        print(f"Dexterité    : +{self.get_stats._dexterity} [req.{self._requirements._dexterity}]")
        print(f"Intelligence : +{self.get_stats._intelligence} [req.{self._requirements._intelligence}]")
        print("------------------------------")
        

class Unequiped(Stuff):
    def __init__(self, slot):
        self._name = "Vide"
        self._slot = slot
        self._requirements = Stats(0,0,0,0)
        self.__stats = Stats(0,0,0,0)

    def display(self):
        print("------------------------------")
        print(f"*** Vide ***")
        print("------------------------------")
        
    def get_stats(self):
        return self.__stats


class Slot:
    def __init__(self, name):
        if name in ["_head", "_chest", "_legs", "_foot", "_leftHand", "_rightHand"]:
            self._name = name
        else:
            raise NameError('Equipement invalide')
        
    def get_name(self):
        return self._name


class Player(Character, Stuff):
    def __init__(self, name, level, stats, pvmax, inventory = [],
                 head = Unequiped(slot = "_head"),
                 chest = Unequiped(slot = "_chest"),
                 legs = Unequiped(slot = "_legs"),
                 foot = Unequiped(slot = "_foot"),
                 leftHand = Unequiped(slot = "_leftHand"),
                 rightHand = Unequiped(slot = "_rightHand"),
                ):
        self._name = name
        self._level = level
        self.__stats = stats
        self._pvmax = pvmax
        self._pv = pvmax
        self._inventory = inventory
        self._head = head
        self._chest = chest
        self._legs = legs
        self._foot = foot
        self._leftHand = leftHand
        self._rightHand = rightHand
        
    def _get_strength(self):
        strength = self.get_stats()._strength
        strength += self._head.get_stats()._strength
        return strength
    
    def _get_constitution(self):
        constitution = self.get_stats()._constitution
        constitution += self._head.get_stats()._constitution
        return constitution
    
    def _get_dexterity(self):
        dexterity = self.get_stats()._dexterity
        dexterity += self._head.get_stats()._dexterity
        return dexterity
    
    def _get_intelligence(self):
        intelligence = self.get_stats()._intelligence
        intelligence += self._head.get_stats()._intelligence
        return intelligence
    
    def get_stats(self):
        return self.__stats
        
    def display_stats(self):
        print("***************************")
        print("--- Point de vie [", self.get_pv(), "/", self.get_pvmax(), "]")
        print("Strength :          ", self._get_strength())
        print("Constitution :      ", self._get_constitution())
        print("Dexterity :         ", self._get_dexterity())
        print("Intelligence :      ", self._get_intelligence())
        print("***************************")

    
class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self._attack()
    
    def _attack(self):
        self.monster.alterate_pv(-self.player.get_stats().get_strength())
        if self.monster.get_pv() > 0:
            print(f"{self.player.get_name()} enlève {self.player.get_stats().get_strength()}PV à {self.monster.get_name()}")
            self._defend()
        else:
            print(f"{self.player.get_name()} enlève {self.player.get_stats().get_strength()}PV à {self.monster.get_name()} et le tue")
            print(f"Player win")
        
    def _defend(self):
        self.player.alterate_pv(-self.monster.get_stats().get_strength())
        if self.player.get_pv() > 0:
            print(f"{self.monster.get_name()} enlève {self.monster.get_stats().get_strength()}PV à {self.player.get_name()}")
            self._attack()
        else:
            print(f"{self.monster.get_name()} enlève {self.monster.get_stats().get_strength()}PV à {self.player.get_name()} et le tue")
            print(f"Monster win")

    def pick_loots(self):
        numbre_loots = random.randint(0,3)
        for i in range(numbre_loots):
            self._generate_loot()
    
    def _generate_loot(self):
        return Item("Heaume du débutant", Slot("_head"), Stats(12, 0, 10, 6), Stats(3, 0, 7, 0))
    
    def end_fight(self):
        if self.player.get_stats()._strength >= self.monster.get_stats().get_strength():
            print(f"{self.player._name} win")
        else:
            print(f"{self.monster._name} win")
    
class Monster(Character):
    def __init__(self, name, level, stats, pv):
        self._name = name
        self._level = level
        self.__stats = stats
        self._pv = pv
        
    def get_stats(self):
        return self.__stats
   
 
if __name__ == '__main__':

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
