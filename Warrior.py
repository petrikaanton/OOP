from winreg import KEY_NOTIFY
#Warrioir -> Battle Army -> Defender -> Vampire

class Warrior:
    def __init__(self,health=50,damage=5):
        self.health = health
        self.damage = damage
        if health > 0:
            self.alive = True
        else:
            self.alive = False
    def __str__(self):
        return str(self.health)+' Health '+str(self.damage)+' Damage'

class Knight(Warrior):
    def __init__(self,health=50,damage=7):
        super().__init__(health,damage)

jozo = Warrior()
zuza = Knight()
print(jozo)
print(zuza)
