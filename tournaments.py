import battleengine as b
import os as o
from time import sleep as s
import colors as co
import load

def ask():
    load.load_game()
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
    c()
    b.run('bronze')
    if b.Enemy.win == False:
        win(None)
    else:
        lose()

def silverCup():
    c()
    b.run('silver')
    if b.Enemy.win == False:
        win(None)
    else:
        lose()

def goldCup():
    c()
    b.run('gold')
    if b.Enemy.win == False:
        win(None)
    else:
        lose()

def crystalCup():
    c()
    b.run('crystal')
    if b.Enemy.win == False:
        win('crystal')
    else:
        lose()

def win(x):
    if x == 'crystal':



def c():
    o.system('clear')

if __name__ == '__main__':
    ask()
