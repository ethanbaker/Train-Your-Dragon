import random as r
import time
import os as o
import classes as cl
import colors as co
import game
import animations as anim
import load

numbers = [.25, .3, .35, .4, .45, .5]

class Enemy(cl.LevelOnePractice):
    pass

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

def statShow(x):
    if x == 'Enemy':
        if Enemy.color == 'red':
           print(co.r + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'orange':
           print(co.o + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'yellow':
           print(co.y + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'green':
           print(co.g + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'blue':
           print(co.b + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'cyan':
           print(co.c + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'violet':
           print(co.v + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        elif Enemy.color == 'magenta':
           print(co.m + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
        else:
           print(co.g + statBoard.format(Enemy.name, Enemy.htp, Enemy.att, Enemy.dfc, Enemy.dog, Enemy.spd, Enemy.sta, '', ''))
    else:
        if cl.Dragon.color == 'red':
            print(co.r + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '  ', '  '))
        elif cl.Dragon.color == 'orange':
            print(co.o + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '  ', '  '))
        elif cl.Dragon.color == 'yellow':
            print(co.y + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))
        elif cl.Dragon.color == 'green':
            print(co.g + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))
        elif cl.Dragon.color == 'blue':
            print(co.b + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))
        elif cl.Dragon.color == 'cyan':
            print(co.c + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))
        elif cl.Dragon.color == 'violet':
            print(co.v + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))
        elif cl.Dragon.color == 'magenta':
            print(co.m + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))
        else:
            print(co.g + statBoard.format(cl.Dragon.name, cl.Dragon.htp, cl.Dragon.att, cl.Dragon.dfc, cl.Dragon.dog, cl.Dragon.spd, cl.Dragon.sta, '', ''))

def pmove():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    c()
    print(playerColorDef())
    statShow(None)
    print()
    move = input(co.b + 'What would you like to do?\nAttack - 1\nDefend - 2\nForefit - 3\n >>> ')
    if move == '1':
        c()
        playerAttack()
    elif move == '2':
        c()
        playerDefense()
    elif move == '3':
        c()
        psta = 0
    else:
        print(co.y + 'Please answer with a 1, 2, or a 3.')
    c()

def emove():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    print(enemyColorDef())
    statShow('Enemy')
    s(3.5)
    if Enemy.htp >= 50:
        enemyAttack()
    elif Enemy.htp >= 30 and Enemy.htp < 50:
        move = r.randint(1, 10)
        if move <= 7:
            enemyAttack()
        else:
            enemyDefense()
    else:
        move = r.randint(1, 3)
        if move <= 2:
            enemyAttack()
        else:
            enemyDefense()

def playerAttack():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    dodge = r.randint(1, round((100 - edog) * .5))
    if psta >= 0:
        if dodge <= 7:
            enemyDodge()
        else:
            c()
            print(co.g + cl.Dragon.name + ' attacks ' + Enemy.name + '!')
            s(1.5)
            print(playerColorDef())
            anim.attackAnim()
            c()
            if enemyD == True:
                damage = patt - edfc
                Enemy.htp -= damage
                enemyD = False
            else:
                damage = patt - round(edfc * (r.choice(numbers)))
                Enemy.htp -= damage
    else:
        c()
        print(co.g + cl.Dragon.name + ' attacks ' + Enemy.name + '!')
        s(1.5)
        print(playerColorDef())
        anim.attackAnim()
        c()
        if enemyD == True:
            damage = patt - edfc
            Enemy.htp -= damage
            enemyD = False
        else:
            damage = patt - round(edfc * (r.choice(numbers)))
            Enemy.htp -= damage


def enemyAttack():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    dodge = r.randint(1, round((100 - pdog) * .5))
    if esta <= 0:
        if dodge <= 7:
            playerDodge()
        else:
            c()
            print(co.g + Enemy.name + ' attacks ' + cl.Dragon.name + '!')
            s(1.5)
            print(enemyColorDef())
            anim.attackAnim()
            c()
            if playerD == True:
                damage = eatt - pdfc
                cl.Dragon.htp -= damage
                playerD = False
            else:
                damage = eatt - round(pdfc * (r.choice(numbers)))
                cl.Dragon.htp -= damage

    else:
        c()
        print(co.g + Enemy.name + ' attacks ' + cl.Dragon.name + '!')
        s(1.5)
        print(enemyColorDef())
        anim.attackAnim()
        c()
        if playerD == True:
            damage = eatt - pdfc
            cl.Dragon.htp -= damage
            playerD = False
        else:
            damage = eatt - round(pdfc * (r.choice(numbers)))
            cl.Dragon.htp -= damage

def playerDefense():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    print(cl.Dragon.name + ' stays back and defends.')
    s(2)
    print(playerColorDef())
    anim.defenseAnim()
    playerD = True

def enemyDefense():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    print(Enemy.name + ' stays back and defends.')
    s(2)
    print(enemyColorDef())
    anim.defenseAnim()
    enemyD = True

def playerDodge():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    c()
    print(cl.Dragon.name + ' dodges ' + Enemy.name + '\'s attack!')
    s(2)
    print(playerColorDef())
    anim.dodgeAnim()
    playerD = True
    psta -= 2

def enemyDodge():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    c()
    print(Enemy.name + ' dodges ' + cl.Dragon.name + '\'s attack!')
    s(2)
    print(enemyColorDef())
    anim.dodgeAnim()
    esta -= 2

def playerSkillCheck():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    check = r.randint(1, (cl.Dragon.lvl + 5))
    if check == 1:
        c()
        then = time.time()
        input('SKILL CHECK')
        reactionTime = time.time() - then
        if round(reactionTime * 1000) <= 350:
            patt += 10
            cl.Dragon.xp += 50
            print(co.g + 'Amazing Skill Check!')
        elif round(reactionTime * 1000) <= 750 and round(reactionTime * 1000) > 350:
            patt += 5
            cl.Dragon.xp += 30
            print(co.g + 'Great Skill Check!')
        elif round(reactionTime * 1000) <= 1000 and round(reactionTime * 1000) > 750:
            patt += 2
            cl.Dragon.xp += 10
            print(co.g + 'Good Skill Check!')
        elif round(reactionTime * 1000) <= 2000 and round(reactionTime * 1000) > 1000:
            print(co.g + 'Okay Skill Check.')
        elif round(reactionTime * 1000) <= 5000 and round(reactionTime * 1000) <= 2000:
            patt -= 2
            print(co.g + 'Bad Skill Check.')
        else:
            patt -= 5
            print(co.g + 'Horrible Skill Check.')
        s(2)
        c()

def playerColorDef():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    if cl.Dragon.color == 'red':
       return co.r
    elif cl.Dragon.color == 'orange':
        return co.o
    elif cl.Dragon.color == 'yellow':
        return co.y
    elif cl.Dragon.color == 'green':
        return co.g
    elif cl.Dragon.color == 'blue':
        return co.b
    elif cl.Dragon.color == 'cyan':
        return co.c
    elif cl.Dragon.color == 'violet':
        return co.v
    elif cl.Dragon.color == 'magenta':
        return co.m
    else:
        return co.g

def enemyColorDef():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    if Enemy.color == 'red':
       return co.r
    elif Enemy.color == 'orange':
        return co.o
    elif Enemy.color == 'yellow':
        return co.y
    elif Enemy.color == 'green':
        return co.g
    elif Enemy.color == 'blue':
        return co.b
    elif Enemy.color == 'cyan':
        return co.c
    elif Enemy.color == 'violet':
        return co.v
    elif Enemy.color == 'magenta':
        return co.m
    else:
        return co.g

def run():
    global phtp, patt, pdfc, playerD, pdog, pspd, psta, ehtp, eatt, edfc, enemyD, edog, espd, esta
    phtp = cl.Dragon.htp
    patt = cl.Dragon.att
    pdfc = cl.Dragon.dfc
    playerD = False
    pdog = cl.Dragon.dog
    pspd = cl.Dragon.spd
    psta = cl.Dragon.sta
    ehtp = Enemy.htp
    eatt = Enemy.att
    edfc = Enemy.dfc
    enemyD = False
    edog = Enemy.dog
    espd = Enemy.spd
    esta = Enemy.sta
    if cl.Dragon.hap >= 90:
        patt += 1
        pdfc += 1
        pdog += 2
        pspd += 2
        psta += 2
    if cl.Dragon.hap <= 30:
        patt -= 1
        pdfc -= 1
        pdog -= 2
        pspd -= 2
        psta -= 2
    while phtp >= 1 and psta >= 1 and ehtp >= 1 and ehtp >= 1:
        if pspd > espd:
            pmove()
            playerSkillCheck()
            emove()
        elif pspd < espd:
            emove()
            pmove()
            playerSkillCheck()
        else:
            people = ['Enemy', 'Player']
            first = r.choice(people)
            if first == 'Enemy':
                emove()
                playerSkillCheck()
                pmove()
            elif first == 'Player':
                playerSkillCheck()
                pmove()
                emove()
    cl.Dragon.htp = 100
    Enemy.htp = 100

def c():
    o.system('clear')

def s(x):
    time.sleep(x)

if __name__ == '__main__':
    load.load_game()
    run()
