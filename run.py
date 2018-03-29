import colors as c
from time import sleep as s
import os as o

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
    print(c.c + 'Welcome to train your dragon!')
    print(c.rc([c.red, c.orange, c.yellow, c.blue, c.green, c.violet, c.cyan, c.magenta]) + dragonAscii)
    s(2)

def askLoad():
    load = input(c.y + 'Would you like to make a new game or load an old save?\nNew - 1\nOld - 2\n >>> '.strip().lower())
    if load == '1':
        pass
        #TODO Clear dragon.json
        #TODO Set dragon.json = main attributes
        #TODO Game run file
        print(c.cl)
    elif load == '2':
        pass
        #TODO Set dragon.json = old attributes
        #TODO Game run file
        print(c.cl)    
    else:
        print(c.y + "Please respond with a 1 or a 2.")
        s(1.5)
        askLoad()

if __name__ == '__main__':
    o.system('clear')
    main()
    print(c.c)
