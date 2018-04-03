import time
import os as o
import colors as co
import training as tr
import classes as cl
import battleengine as b

def ask():
    c()
    print(co.g + 'Welcome to the practice center!')
    print()
    level = input(co.b + 'What level would you like to practice with?\nLevel One - 1\nLevel Two - 2\nLevel Three - 3\n >>> ')
    if level == '1':
        c()
        lvlOne()
    elif level == '2':
        c()
        lvlTwo()
    elif level == '3':
        c()
        lvlTwo()
    else:
        print('Please answer with a 1, 2, or 3.')
        s(2)
        c()

def lvlOne():
    b.run(1)

def lvlTwo():
    b.run(2)

def lvlThree():
    b.run(3)

def c():
    o.system('clear')

def s(x):
    time.sleep(x)

if __name__ == '__main__':
    ask()
