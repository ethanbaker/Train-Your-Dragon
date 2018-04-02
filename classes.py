import random as r

names = ['Jeremy', 'Matthew', 'John', 'Willard', 'Aaorn', 'Ashley', 'Lauren', 'Jamiese', 'Catherine', 'Caroline']
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'violet', 'cyan', 'magenta']

class Base():
    htp = 100
    att = 10
    dfc = 5
    dog = 5
    sta = 10
    spd = 10
    hap = 100
    name = ''
    color = ''
    xp = 0
    lvl = 1

class Dragon(Base):
    pass

class LevelOnePractice(Base):
    att = r.randint(10, 17)
    dfc = r.randint(5, 12)
    dog = r.randint(6, 11)
    spd = r.randint(9, 12)
    sta = r.randint(9, 12)
    name = r.choice(names)
    color = r.choice(colors)

class LevelTwoPractice(Base):
    att = r.randint(23, 32)
    dfc = r.randint(17, 25)
    dog = r.randint(16, 21)
    spd = r.randint(17, 19)
    sta = r.randint(17, 19)
    name = r.choice(names)
    color = r.choice(colors)

class LevelThreePractice(Base):
    att = r.randint(36, 43)
    dfc = r.randint(26, 31)
    dog = r.randint(28, 34)
    spd = r.randint(26, 30)
    sta = r.randint(26, 30)
    name = r.choice(names)
    color = r.choice(colors)
    
class highScores():
        attack = 10000
        defense = 10000
        dodge = 10000
        speed = 10000
        stamina = 10000



if __name__ == '__main__':
    print(str(LevelThreePractice.att))
