from time import sleep as s
import os as o
import classes as cl
import math
import animations as anim
import load as loa
import colors as co
import training
import save as sav

def lvlCheck():
    loa.load_game()
    if cl.Dragon.xp >= math.floor(50 + (cl.Dragon.lvl * 5.25)):
        lvlUp()
    else:
        pass

def lvlUp():
    cl.Dragon.xp -= math.floor(50 + cl.Dragon.lvl * 5.25)
    cl.Dragon.lvl += 1
    print(co.g + cl.Dragon.name + ' leveled up!')
    s(2)
    print(training.colorDef())
    anim.lvlUpAnim()
    sav.save_game()

if __name__ == '__main__':
    lvlCheck()
