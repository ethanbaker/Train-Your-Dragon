import colors as co
from time import sleep as s
import os as o

import classes as cl
import game
import load as loads
import save as saves

dragonAscii = '''

                                                 __----~~~~~~~~~~~------___
                                      .  .   ~~//====......          __--~ ~~
                      -.            \_|//     |||\\  ~~~~~~::::... /~
                   ___-==_       _-~o~  \/    |||  \\            _/~~-
           __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
       _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
     .~       .~       |   \\ -_    /  /-   /   ||      \   /
    /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\ 
             '         ~-|      /|    |-~\~~       __--~~
                         |-~~-_/ |    |   ~\_   _-~            /\ 
                              /  \     \__   \/~                \__
                          _--~ _/ | .-~~____--~-/                  ~~==.
                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                    -_     ~\      ~~---l__i__i__i--~~_/
                                    _-~-__   ~)  \--______________--~~
                                  //.-~~~-~_--~- |-------~~~~~~~~
                                         //.-~~~--\ 
'''

def main():
    print(co.c + 'Welcome to Train Your Dragon!')
    print(co.rc([co.red, co.orange, co.yellow, co.blue, co.green, co.violet, co.cyan, co.magenta]) + dragonAscii)
    print(co.y + 'Version - BETA')
    s(2)
    askLoad()

def askLoad():
    load = input(co.b + 'Would you like to make a new game or load an old save?\nNew - 1\nOld - 2\n >>> ').strip().lower()
    if load == '1':
        cl.Dragon = cl.Base
        c()
        askColor()
        askName()
        saves.save_game()
        saves.save_scores()
        game.welcome()
        game.main()
    elif load == '2':
        loads.load_game()
        loads.load_scores()
        c()    
        game.main()
    else:
        print(co.y + "Please respond with a 1 or a 2.")
        s(1.5)
        c()
        askLoad()

def askColor():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'violet', 'magenta']
    color = input(co.b + 'What color do you want your dragon to be?\n' + co.r + 'Red\n' + co.o + 'Orange\n' + co.y + 'Yellow\n' + co.g + 'Green\n' + co.b + 'Blue\n' + co.c + 'Cyan\n' + co.m + 'Magenta\n' + co.v + 'Violet\n >>> ').strip().lower()
    if color not in colors:
        print(co.y + 'Please list one of the colors listed above.')
        s(1.5)
        c()
        askColor()
    else:
        cl.Dragon.color = color

def askName():
    name = input(co.b + 'What do you want to name your dragon?\n >>> ').title().strip()
    if name == '':
        print(co.y + 'Please give a name.')
        s(1.5)
        c()
    else:
        nameConfirm = input(co.b + 'Your dragon is going to be named ' + name + ', are you sure you want this name?\nYes - 1\nNo - 2\n >>> ')
        if nameConfirm == '1':
            cl.Dragon.name = name
        elif nameConfirm == '2':
            c()
            askName()
        else:
            print(co.y + 'Please answer with a 1 or a 2.')
    s(2)
def c():
    o.system('clear')

if __name__ == '__main__':
    try:
        c()
        main()
    except KeyboardInterrupt:
        exit
