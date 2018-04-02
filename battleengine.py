import random as r
import time
import os as o

def pmove():
    print(playerColorDef() + game.statShow('Player'))
    print()
    move = (co.b + 'What would you like to do?\nAttack - 1\nDefend - 2\nForefit - 3\n >>> ')
    if move == '1':
        c()
        playerAttack()
    elif move == '2':
        c()
        playerDefend()
    elif move == '3':
        end()
        c()
        break
    else:
        print(co.y + 'Please answer with a 1, 2, or a 3.')
    c()

def emove():
    game.statShow('Enemy')
    if cl.Enemy.htp >= 50:
        enemyAttack()
    elif cl.Enemy.htp >= 30 and cl.Enemy.htp < 50:
        move = r.randint(1, 10)
        if move <= 7:
            enemyAttack()
        else:
            enemyDefend()
    else:
        move = r.randint(1, 3)
        if move <= 2:
            enemyAttack()
        else:
            enemyDefend()

def playerAttack():
    dodge = r.randint(round((100 - edodge) * .5))
    if dodge <= 13:
        enemyDodge()
    c()
    print(co.g + cl.Dragon.name + ' attacks ' + cl.Enemy.name! + '!')
    s(1.5)
    print(playerColorDef())
    anim.attackAnim()
    c()
    if enemyD == True:
        damage = patt - edfc
        ehtp -= damage
    else:
        damage = patt - round(edfc * (r.randint(.25, .5)))
        ehtp -= damage


def enemyAttack():
    dodge = r.randint(round((100 - pdodge) * .5))
    if dodge <= 13:
        playerDodge()
    else:
        c()
        print(co.g + cl.Enemy.name + ' attacks ' + cl.Dragon.name + '!')
        s(1.5)
        print(enemyColorDef())
        anim.attackAnim()
        c()
        if playerD == True:
            damage = eatt - pdfc
            phtp -= damage
        else:
            damage = eatt - round(pdfc * (r.randint(.25, .5)))
            phtp -= damage

def playerDefense():
    print(cl.Dragon.name + ' stays back and defends.')
    s(2)
    anim.dodgeAnim()
    playerD = True

def enemyDefense():
    print(cl.Enemy.name + ' stays back and defends.')
    s(2)
    anim.dodgeAnim()
    enemyD = True

def playerDodge():
   c()
   print(cl.Dragon.name + ' dodges ' + cl.Enemy.name + '\'s attack!')
   s(2)
   anim.dodgeAnim()
   playerD = True

def enemyDodge():
    c()
    print(cl.Enemy.name + ' dodges ' + cl.Dragon.name + '\'s attack!')
    s(2)
    anim.dodgeAnim()

def playerSkillcheck():
    check = r.randint(1, cl.Dragon.lvl + 5))
    if check == 1:
        c()
        then = time.time()
        input('SKILL CHECK')
        reactionTIme = time.time() - then
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
        elif round(reactionTime * 1000) <= 5000 and round(reactionTime * 1000) <= 2000::
            patt -= 2
            print(co.g + 'Bad Skill Check.')
        else:
            patt -= 5
            print(co.g + 'Horrible Skill Check.')
        s(2)
        c()

def playerColorDef():
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
    if cl.Enemy.color == 'red':
       return co.r
    elif cl.Enemy.color == 'orange':
        return co.o
    elif cl.Enemy.color == 'yellow':
        return co.y
    elif cl.Enemy.color == 'green':
        return co.g
    elif cl.Enemy.color == 'blue':
        return co.b
    elif cl.Enemy.color == 'cyan':
        return co.c
    elif cl.Enemy.color == 'violet':
        return co.v
    elif cl.Enemy.color == 'magenta':
        return co.m
    else:
        return co.g

def run():
    phtp = cl.Dragon.htp
    patt = cl.Dragon.att
    pdfc = cl.Dragon.dfc
    playerD = False
    pdog = cl.Dragon.dog
    pspd = cl.Dragon.spd
    psta = cl.Dragon.sta
    ehtp = cl.Enemy.htp
    eatt = cl.Enemy.att
    edfc = cl.Enemy.dfc
    enemyD = False
    edog = cl.Enemy.dog
    espd = cl.Enemy.spd
    esta = cl.Enemy.sta
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
            playerSkillCheck()
            pmove()
            emove()
        elif pspd < espd:
            emove()
            playerSkillCheck()
            pmove()
        else:
            first = r.choice('Enemy', 'Player')
            if first == 'Enemy':
                emove()
                playerSkillCheck()
                pmove()
            elif first == 'Player':
                playerSkillCheck()
                pmove()
                emove()

if __name__ == '__main__':
    run()
