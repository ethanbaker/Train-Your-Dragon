import colors as co
import time
import classes as cl
import os as o
import random
import time

highScores = {
        'attack':0,
        'defence':0,
        'dodge':0,
        'speed':0,
        'stamina':0
        }

def askTrain():
    training = input('What would you like to train on?\nAttack - 1\nDefence - 2\nDodge - 3\nSpeed - 4\nStamina - 5\n >>> ')
    if training == '1':
        attackTrain()
    elif training == '2':
        defenceTrain()
    elif training == '3':
        dodgeTrain()
    elif training == '4':
        speedTrain()
    elif training == '5':
        staminaTrain()
    else:
        print(co.y + 'Please answer with a 1, 2, 3, 4, or a 5.')

def attackAsk():
    tutorial = input(co.b + 'Do you want the tutorial on how to train for attack?\nYes - 1\nNo - 2\n >>> ')
    if tutorial == '1':
        print(co.g + 'To play, press enter as soon as you see ATTACK appear on the screen. That faster you respond, the more XP you get.')
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
    reactionTime = time.time() - then
    print(f"Your reaction time was {reactionTime*1000:.0f} ms")
    if highScores['attack'] != 0 and reactionTime < highScores['attack']:
        highScores['attack'] = reactionTime
    cl.Dragon.xp += 20 - round(reactionTime * 10)
    if round(reactionTime * 10) < 6:
        cl.Dragon.att += 5 - round(reactionTime * 10)
    sav.save_game()
    sav.save_scores() 

def c():
    o.system('clear')

def s(x):
    time.sleep(x)

def main():
    askTrain()

if __name__ == '__main__':
    attackTrain()
