import colors as co
import time
import classes as cl
import os as o
import random
import time
import save as sav
import load as loa
import math
import game
import animations as anim

def askTrain():
    loa.load_game()
    loa.load_scores()
    training = input(co.b + 'What would you like to train on?\nAttack - 1\nDefence - 2\nDodge - 3\nSpeed - 4\nStamina - 5\nSee High Scores - 6\nReturn to the Training Center - 7\n >>> ')
    if training == '1':
        c()
        attackAsk()
    elif training == '2':
        c()
        defenseAsk()
    elif training == '3':
        c()
        dodgeAsk()
    elif training == '4':
        c()
        speedAsk()
    elif training == '5':
        c()
        staminaAsk()
    elif training == '6':
        print('Attack game high score - ' + str(cl.highScores.attack))
        print('Defense game high score - ' + str(cl.highScores.defense))
        print('Dodge game high score - ' + str(cl.highScores.dodge))
        print('Speed game high score - ' + str(cl.highScores.speed))
        print('Stamina game high score - ' + str(cl.highScores.stamina))
    elif training == '7':
        print('Returning to the training center.')
        s(2)
        c()
        game.run()
    else:
        print(co.y + 'Please answer with a 1, 2, 3, 4, or a 5.')
        s(2)
        c()

def attackAsk():
    tutorial = input(co.b + 'Do you want the tutorial on how to train for attack?\nYes - 1\nNo - 2\n >>> ')
    if tutorial == '1':
        print(co.c + 'To play, press enter as soon as you see ATTACK appear on the screen. That faster you respond, the more XP you get.')
        input('---Press Enter to continue---')
        c()
        attackTrain()
    elif tutorial == '2':
        c()
        attackTrain()
    else:
        print(co.y + 'Please respond with a 1 or a 2.')
        s(2)
        attackAsk()

def attackTrain():
    c()
    input(co.c + '---Press Enter to start---')
    c()
    s(random.randint(1, 10))
    then = time.time()
    react = input('ATTACK')
    print()
    reactionTime = time.time() - then
    s(2)
    if reactionTime <= 0.0001:
        c()
        print(co.r + 'You failed! Try again next time.')
        s(2)
    else:
        anim.attackAnim()
        xpGain = 0
        attGain = 0
        print(co.g + f"Your reaction time was {reactionTime*1000:.0f} ms")
        s(2)
        if round(reactionTime * 1000) < cl.highScores.attack:
            cl.highScores.attack = round(reactionTime * 1000)
        if cl.Dragon.hap >= 30:
            cl.Dragon.xp += 20 - round(reactionTime * 10)
            xpGain += 20 - round(reactionTime * 10)
            if cl.Dragon.hap >= 80:
                cl.Dragon.xp += 5
                xpGain += 20 - round(reactionTime * 10)
        if round(reactionTime * 10) < 7 and cl.Dragon.hap >= 30:
            cl.Dragon.att += 6 - math.floor(reactionTime * 10)
            attGain += 6 - math.floor(reactionTime * 10)
            if cl.Dragon.hap >= 80:
                cl.Dragon.att += 1
                attGain += 1
        cl.Dragon.hap -= round((100 - cl.Dragon.hap) * .25)
        if cl.Dragon.hap < 0:
            cl.Dragon.hap = 0
        gain(xpGain, attGain, 'attack')
    sav.save_game()
    sav.save_scores() 

def defenseAsk():
    tutorial = input(co.b + 'Do you want the tutorial on how to train for defense?\nYes - 1\nNo - 2\n >>> ')
    if tutorial == '1':
        print(co.c + 'To play, press enter as soon as you see DEFEND appear on the screen. Do not press anything when ATTACK appears on the screen. That faster you respond to DEFEND, the more XP you get.')
        input('---Press Enter to continue---')
        c()
        defenseTrain()
    elif tutorial == '2':
        c()
        defenseTrain()
    else:
        print(co.y + 'Please respond with a 1 or a 2.')
        s(2)
        defenseAsk()

def defenseTrain():
    c()
    input(co.c + '---Press Enter to start---')
    c()
    numbers = ['1', '2', '3']
    game = random.choice(numbers)
    if game == '1':
        s(random.randint(1, 5))
        print('ATTACK')
        print()
        s(2)
        s(random.randint(1, 5))
        print('ATTACK')
        print()
        s(2)
        s(random.randint(1, 5))
        then = time.time()
        input('DEFEND')
        breactionTime = time.time() - then
        s(2)
        c()
    elif game == '2':
        s(random.randint(1, 5))
        then = time.time()
        input('DEFEND')
        reactionTime = time.time() - then
        print()
        s(2)
        s(random.randint(1, 5))
        print('ATTACK')
        print()
        s(2)
        s(random.randint(1, 5))
        then = time.time()
        input('DEFEND')
        reactionTimeTwo = time.time() - then
        print()
        s(2)
        c()
        if reactionTime <= reactionTimeTwo:
            breactionTime = reactionTime
        else:
            breactionTime = reactionTimeTwo
    elif game == '3':
        s(random.randint(1, 5))
        print('ATTACK')
        print()
        s(2)
        s(random.randint(1, 5))
        then = time.time()
        input('DEFEND')
        reactionTime = time.time() - then
        print()
        s(random.randint(1, 5))
        then = time.time()
        input('DEFEND')
        reactionTimeTwo = time.time() - then
        s(2)
        c()
        if reactionTime <= reactionTimeTwo:
            breactionTime = reactionTime
        elif reactionTime >= reactionTimeTwo:
            breactionTime = reactionTimeTwo
    if int(round(breactionTime*1000)) <= 0:
        print(co.r + 'You failed! Try again next time.')
        s(2)
    else:
        xpGain = 0
        dfcGain = 0
        print(co.g + f"Your best reaction time was {breactionTime*1000:.0f} ms")
        s(2)
        if round(breactionTime * 1000) < cl.highScores.defense:
            cl.highScores.defense = round(breactionTime * 1000)
        if cl.Dragon.hap >= 30:
            cl.Dragon.xp += 20 - round(breactionTime * 10)
            xpGain += 20 - round(breactionTime * 10)
            if cl.Dragon.hap >= 80:
                cl.Dragon.xp += 5
                xpGain += 5
        if round(breactionTime * 10) < 7 and cl.Dragon.hap >= 30:
            cl.Dragon.dfc += 6 - math.floor(breactionTime * 10)
            dfcGain += 6 - math.floor(breactionTime * 10)
            if cl.Dragon.hap >= 80:
                cl.Dragon.dfc += 1
                dfcGain += 1
        gain(xpGain, dfcGain, 'defense')
    cl.Dragon.hap -= round((100 - cl.Dragon.hap) * .25)
    if cl.Dragon.hap < 0:
        cl.Dragon.hap = 0
    sav.save_game()
    sav.save_scores() 

def dodgeAsk():
    tutorial = input(co.b + 'Do you want the tutorial on how to train for dodge?\nYes - 1\nNo - 2\n >>> ')
    if tutorial == '1':
        print(co.c + 'To play, press enter _ seconds later as the prompt says. The closer you respond _ seconds later, the more XP you get.')
        input(co.c + '---Press Enter to continue---')
        c()
        dodgeTrain()
    elif tutorial == '2':
        c()
        dodgeTrain()
    else:
        print(co.y + 'Please respond with a 1 or a 2.')
        s(2)
        dodgeAsk()

def dodgeTrain():
    c()
    input(co.c + '---Press Enter to start---')
    c()
    x = random.randint(2, 7)
    s(random.randint(3, 8))
    print(co.g + 'There is an obstacle ' + str(x) + ' seconds away!')
    print()
    then = time.time()
    input()
    reactionTime = abs(time.time() - then - x)
    print(co.g + f"Your dodge time was {reactionTime*1000:.0f} ms")
    s(2)
    xpGain = 0
    dogGain = 0
    if round(reactionTime * 1000) < cl.highScores.dodge:
        cl.highScores.dodge = round(reactionTime * 1000)
    if cl.Dragon.hap >= 30:
        cl.Dragon.xp += 20 - round(reactionTime * 10)
        xpGain += 20 - round(reactionTime * 10)
        if cl.Dragon.hap >= 80:
            cl.Dragon.xp += 5
            xpGain += 5
    if round(reactionTime * 10) < 5 and cl.Dragon.hap >= 30:
        cl.Dragon.dog += 4 - math.floor(reactionTime * 10)
        dogGain += 4 - math.floor(reactionTime * 10)
        if cl.Dragon.hap >= 80:
            cl.Dragon.dog += 1
            dogGain += 1
        gain(xpGain, dogGain, 'dodge')
    cl.Dragon.hap -= round((100 - cl.Dragon.hap) * .25)
    if cl.Dragon.hap < 0:
        cl.Dragon.hap = 0
    sav.save_game()
    sav.save_scores() 


def speedAsk():
    tutorial = input(co.b + 'Do you want the tutorial on how to train for speed?\nYes - 1\nNo - 2\n >>> ')
    if tutorial == '1':
        print(co.c + 'To play, press enter twice as soon as you see START appear on the screen. The faster you respond, the more XP you get.')
        input('---Press Enter to continue---')
        c()
        speedTrain()
    elif tutorial == '2':
        c()
        speedTrain()
    else:
        print(co.y + 'Please respond with a 1 or a 2.')
        s(2)
        speedAsk()

def speedTrain():
    c()
    input(co.c + '---Press Enter to start---')
    c()
    s(random.randint(1, 10))
    input('START')
    then = time.time()
    input()
    reactionTime = time.time() - then
    print(co.g + f"Your speed time was {reactionTime*1000:.0f} ms")
    s(2)
    xpGain = 0
    spdGain = 0
    if round(reactionTime * 1000) < cl.highScores.speed:
        cl.highScores.speed = round(reactionTime * 1000)
    if cl.Dragon.hap >= 30:
        cl.Dragon.xp += 20 - round(reactionTime * 10)
        xpGain += 20 - round(reactionTime * 10)
        if cl.Dragon.hap >= 80:
            cl.Dragon.xp += 5
            xpGain += 5
    if round(reactionTime * 10) < 5 and cl.Dragon.hap >= 30:
        cl.Dragon.spd += 4 - math.floor(reactionTime * 10)
        spdGain += 4 - math.floor(reactionTime * 10)
        if cl.Dragon.hap >= 80:
            cl.Dragon.spd += 1
            spdGain += 1
        gain(xpGain, spdGain, 'speed')
    cl.Dragon.hap -= round((100 - cl.Dragon.hap) * .25)
    if cl.Dragon.hap < 0:
        cl.Dragon.hap = 0
    sav.save_game()
    sav.save_scores() 

def staminaAsk():
    tutorial = input(co.b + 'Do you want the tutorial on how to train for stamina?\nYes - 1\nNo - 2\n >>> ')
    if tutorial == '1':
        print(co.c + 'To play, press enter three times, trying to have one second in between each press as soon as you see START appear on the screen. \nThe closer the interval is to one second, the more XP you get.')
        input('---Press Enter to continue---')
        c()
        staminaTrain()
    elif tutorial == '2':
        c()
        staminaTrain()
    else:
        print(co.y + 'Please respond with a 1 or a 2.')
        s(2)
        staminaAsk()

def staminaTrain():
    c()
    input(co.c + '---Press Enter to start---')
    c()
    s(random.randint(1, 10))
    input('START')
    then = time.time()
    input()
    reactionTime = time.time() - then
    input()
    reactionTimeTwo = time.time() - reactionTime
    reactionTime -= 1
    reactionTimeTwo -= 1
    xpGain = 0
    staGain = 0
    if reactionTime < reactionTimeTwo:
        breactionTime = reactionTime
    else:
        breactionTime = reactionTimeTwo
    breactionTime = abs(breactionTime)
    print(co.g + f"Your best reaction time was {breactionTime*1000:.0f} ms")
    s(2)
    if round(breactionTime * 1000) < cl.highScores.stamina:
        cl.highScores.stamina = round(breactionTime * 1000)
    if cl.Dragon.hap >= 30:
        cl.Dragon.xp += 15 - round(breactionTime * 10)
        xpGain += 15 - round(breactionTime * 10)
        if cl.Dragon.hap >= 80:
            cl.Dragon.xp += 5
            xpGain += 5
    if round(breactionTime * 10) < 5 and cl.Dragon.hap >= 30:
        cl.Dragon.sta += 4 - math.floor(reactionTime * 10)
        staGain += 4 - math.floor(reactionTime * 10)
        if cl.Dragon.hap >= 80:
            cl.Dragon.sta += 1
            staGain += 1
    gain(xpGain, staGain, 'stamina')
    cl.Dragon.hap -= round((100 - cl.Dragon.hap) * .25)
    if cl.Dragon.hap < 0:
        cl.Dragon.hap = 0
    sav.save_game()
    sav.save_scores()

def gain(xp, skillAmount, skillName):
    print()
    print(co.g + cl.Dragon.name + ' gained ' + str(skillAmount) + ' ' + skillName + ' points.')
    s(2)
    print()
    print(co.g + cl.Dragon.name + ' gained ' + str(xp) + ' XP points.')
    s(3.5)

def c():
    o.system('clear')

def s(x):
    time.sleep(x)

def main():
    askTrain()

if __name__ == '__main__':
    askTrain()
