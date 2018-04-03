import battleengine as b
import os as o
from time import sleep as s
import colors as co

def ask():
    tourney = input(co.b + 'What tournament would you like to enter?\nBronze - 1\nSilver - 2\nGold - 3\nCrystal - 4\n >>> ')
    if tourney == '1':
        bronzeCup()
    elif tourney == '2':
        silverCup()
    elif tourney == '3':
        goldCup()
    elif tourney == '4':
        crystalCup()
    else:
        print(co.y + 'Please answer with a 1, 2, 3, or 4.')
        s(2)
        c()
        ask()

def bronzeCup():
    b.run('bronze')
    if b.Enemy.win == False:
        win()
    else:
        lose()

def silverCup():
    b.run('silver')
    if b.Enemy.win == False:
        win()
    else:
        lose()

def goldCup():
    b.run('gold')
    if b.Enemy.win == False:
        win()
    else:
        lose()

def crystalCup():
    b.run('crystal')
    if b.Enemy.win == False:
        win()
    else:
        lose()

def c():
    o.system('clear')
