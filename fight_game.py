import random
import time

class Fighter():
    def __init__(self,name, health=100, damage=15, defense=10):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

class Mage():
    def __init__(self,name, health=100, damage=45, defense=5):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

class Fight:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def start(self):
        while self.p1.health > 0 and self.p2.health > 0:
            
            mage_damage = mage.damage + random.randint(5,11)
            mage_defense = mage.defense + random.randint(0,6)
            
            fighter_damage = fighter.damage + random.randint(0,6)
            fighter_defense = fighter.defense + random.randint(5,11)          
                  
            self.p1.health -= mage_damage - fighter_defense
            print(f"{mage.name} {mage_damage-fighter_defense} hasar verdi ve savaşcının kalan canı {self.p1.health}")
            if self.p1.health <=0:
                print(f"Kazanan :{mage.name} ve kalan canı {self.p2.health} ")
                break
            time.sleep(1)
           
            self.p2.health -= fighter_damage - mage_defense
            print(f"{fighter.name} {fighter_damage-mage_defense} hasar verdi ve büyücünün kalan canı {self.p2.health}")
            if self.p1.health <=0:
                print(f"Kazanan :{fighter.name} ve kalan canı {self.p1.health}")
                break
            time.sleep(1)

            
fighter = Fighter(input("Savaşcının adı ne olsun > "))
mage = Mage(input("Büyücünün adı ne olsun > "))
print(fighter.damage,fighter.defense)
print(mage.damage,mage.defense)
game = Fight(fighter,mage)
game.start()