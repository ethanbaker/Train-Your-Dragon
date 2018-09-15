import random as r
from time import sleep as s

dragonNames = ['Sobek', 'Viper', 'Glycon', 'Typhon', 'Errol', 'Ramoth', 'Thorn', 'Eldrax', 'Pyre', 'Alduim']
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'violet', 'cyan', 'magenta']

class Base():
    htp = 100
    att = 10
    dfc = 5
    dog = 5
    sta = 10
    spd = 10
    hap = 100
    name = 'Base'
    color = 'Base'
    xp = 0
    lvl = 1

class Dragon(Base):
    pass

class Level(Base):
    htp = 100
    win = None
    def __init__(self, level):
        if level == 1:
            self.att = r.randint(10, 17)
            self.dfc = r.randint(5, 12)
            self.dog = r.randint(6, 11)
            self.spd = r.randint(9, 12)
            self.sta = r.randint(9, 12)
            self.name = r.choice(dragonNames)
            self.color = r.choice(colors)
        elif level == 2:        
            self.att = r.randint(23, 32)
            self.dfc = r.randint(17, 25)
            self.dog = r.randint(16, 21)
            self.spd = r.randint(17, 19)
            self.sta = r.randint(17, 19)
            self.name = r.choice(dragonNames)
            self.color = r.choice(colors)
        elif level == 3:
            self.att = r.randint(36, 43)
            self.dfc = r.randint(26, 31)
            self.dog = r.randint(28, 34)
            self.spd = r.randint(26, 30)
            self.sta = r.randint(26, 30)
            self.name = r.choice(dragonNames) 
            self.color = r.choice(colors)
        elif level == 'bronze':
            self.att = 18
            self.dfc = 7
            self.dog = 13
            self.spd = 19
            self.sta = 13
            self.name = 'Mushu'
            self.color = 'orange'
        elif level == 'sliver':
            self.att = 26
            self.dfc = 14
            self.dog = 21
            self.spd = 29
            self.sta = 24
            self.name = 'Saphira' 
            self.color = 'blue'
        elif level == 'gold':
            self.att = 35
            self.dfc = 19
            self.dog = 27
            self.spd = 35
            self.sta = 30
            self.name = 'Jade'
            self.color = 'cyan'
        elif level == 'crystal':
            self.att = 50
            self.dfc = 25
            self.dog = 40
            self.spd = 50
            self.sta = 40
            self.name = 'Valyrym'
            self.color = 'red'

class highScores():
        attack = 10000
        defense = 10000
        dodge = 10000
        speed = 10000
        stamina = 10000


