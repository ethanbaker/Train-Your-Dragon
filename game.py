from time import sleep as s
import os as o
import colors as co
import battleengine as ba
import load as loa
import save as sav
import classes as cl
import training as train
import tournaments as tourney
import play
import practice as prat

crystalCup = False

statBoard = '''
Name - {}   Heath - {}   Attack - {}   Defence - {}   Dodge - {}   Speed - {}   Stamina - {}   {}   {}

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
ttttt = True

def statShow(x):
    if ttttt == True:
        if cl.Dragon.color == 'red':
           print(co.r + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'orange':
            print(co.o + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'yellow':
            print(co.y + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'green':
            print(co.g + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'blue':
            print(co.b + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'cyan':
            print(co.c + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'violet':
            print(co.v + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        elif cl.Dragon.color == 'magenta':
            print(co.m + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))
        else:
            print(co.g + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, 'Happiness - ' + str(cl.Dragon.hap), 'Level - ' + str(cl.Dragon.lvl)))

def welcome():
    askTutorial = input(co.b + 'Welcome to Train Your Dragon! Would you like to go through the tutorial?\nYes - 1\nNo - 2\n >>> ').strip()
    if askTutorial == '1':
        tutorial()
        run()
    elif askTutorial == '2':
        c()
        run()
    else:
        print(co.y + 'Please answer with a 1 or a 2.')

def tutorial():
    c()
    print(co.g + 'Train Your Dragon is a game where you train your dragon to be stronger and beat opponents! In the game, you will get different \ncolored lines meaning different things.')
    print()
    s(2.5)
    print('Green lines are informational and are usually telling you important information.')
    print()
    s(2.5)
    print(co.b + 'Blue lines indicate a question.')
    print()
    s(2.5)
    print(co.y + 'Yellow lines appear when you don\'t answer in the correct format.')
    print()
    s(2.5)
    print(co.m + 'Magenta lines show that the game is saving or loading.')
    print()
    s(2.5)
    print(co.r + 'Red lines show warnings.')
    print()
    s(2.5)
    print(co.c + 'Cyan lines are directional and show you how to play.')
    print()
    s(2.5)
    input('---Press Enter to continue---')
    print()
    c()
    print(co.g + 'Your goal is to have the strongest Dragon in the world! In order to achieve this, you must train your dragon.')
    print()
    s(2.5)
    print(co.g + 'Your dragon\'s health is automatically set at 100. If it gets to zero, your dragon faints and you lose the battle.')
    print()
    s(2.5)
    print('Your dragon has some stats that can be leved up. These are attack, defense, dodge, speed, and stamina. The stats and their affects are listed below.')
    print()
    s(2.5)
    print('The more attack points your dragon has, the more damage your dragon does to other opponents.')
    print()
    s(2.5)
    print('The more defense points your dragon has, the less damage other opponents can do to your dragon.')
    print()
    s(2.5)
    print('The more dodge points your dragon has, the more likey they are to dodge an opponents attack.')
    print()
    s(2.5)
    print('If your dragon has more speed points than the opponent, they get to attack first.')
    print()
    s(2.5)
    print('If your dragon\'s stamina points drop below 0, your dragon will be exhausted and be unable to dodge.')
    print()
    s(2.5)
    print('Your dragon also has happiness points. These show how happy your dragon is. The less happy your dragon is, the less XP you will \nget and the attribute points you will get.')
    print()
    input(co.c + '---Press Enter to continue---')
    c()
    print(co.g + 'When you battle other dragons, you can attack or defend.')
    print()
    s(2.5)
    print(co.g + 'Attacking deals damage to the other dragon.')
    s(2.5)
    print(co.g + 'Defending reduces the amount of damage you will take when your enemy attacks you by a ton.')
    s(2.5)
    print(co.g + 'During the battle, random skill checks appear. The faster you press enter and respond, the more bonus attack points and \nXP you will gain.')
    print()
    input('---Press Enter to Continue')
    print()
    print(co.g + 'Good luck!')
    s(1.5)
    c()

def run():
    while crystalCup == False:
        if cl.Dragon.att > 55:
            cl.Dragon.att = 55
        if cl.Dragon.dfc > 30:
            cl.Dragon.att = 30
        if cl.Dragon.dog > 35:
            cl.Dragon.dog = 35
        if cl.Dragon.spd > 50:
            cl.Dragon.spd = 50
        if cl.Dragon.sta > 50:
            cl.Dragon.sta = 50
        statShow('')
        print(co.g + 'Welcome to the Dragon Center! From here you can train your dragon, practice battling other trainers, play in tournaments, or \nplay with your dragon!')
        print()
        action = input(co.b + 'What would you like to do?\nTrain - 1\nPractice Battles - 2\nPlay in Tournaments - 3\nPlay with ' + cl.Dragon.name + ' - 4\n >>> ')
        if action == '1':
            if cl.Dragon.hap < 20:
                print(co.r + cl.Dragon.name + ' is not happy enough to train with you. Try playing with them to increase their happiness.')
                s(2)
                c()
            else:
                train.main()
        elif action == '2':
            if cl.Dragon.hap < 20:
                print(co.r + cl.Dragon.name + ' is not happy enough to train with you. Try playing with them to increase their happiness.')
                s(2)
                c()
            else:
                prat.ask()
        elif action == '3':
            if cl.Dragon.lvl < 15:
                print(co.r + 'Sorry, you must be level 15 or above to play in tournaments.')
                s(2)
                c()
                run()
            else:
                if cl.Dragon.hap < 20:
                    print(co.r + cl.Dragon.name + ' is not happy enough to fight with you. Try playing with them to increase their happiness.')
                    s(2)
                    c()
                else:
                    tourney.main()
        elif action == '4':
            play.main()
        elif action == 'RESET':
            print(co.y + 'Reseting high scores...')
            s(2)
            c()
            run()
            cl.highScores.attack = 100000
            cl.highScores.defense = 100000
            cl.highScores.dodge = 100000
            cl.highScores.speed = 100000
            cl.highScores.stamina = 100000
        else:
            print(co.y + 'Please answer with a 1, 2, 3, or a 4.')
            s(2)
            c()
            run()


def c():
    o.system('clear')

def main():
    c()
    run()


if __name__ == '__main__':
    statShow(False)
