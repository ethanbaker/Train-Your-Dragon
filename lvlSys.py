from time import sleep as s
import os as o
import classes as cl
import math
import animations as anim

def lvlCheck():
    if cl.Dragon.xp == math.floor(50 + cl.Dragon.lvl * 5.25)
        lvlUp()
    else:
        pass

def lvlUp():
    cl.Dragon.xp -= math.floor(50 + cl.Dragon.lvl * 5.25)
    cl.Dragon.lvl += 1
    print(co.g + cl.Dragon.name + ' leveled up!')
    anim.lvlUpAnim()

