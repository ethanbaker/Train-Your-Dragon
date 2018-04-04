from time import sleep as s
import os as o
import animations as anim
import battleengine as b
import random as r
import colors as co
import classes as cl

def main():
    print(co.g + 'You play with ' + cl.Dragon.name + '.')
    print(b.playerColorDef)
    s(1.5)
    anim.playAnim()
    cl.Dragon.hap += 45
    cl.Dragon.hap += cl.Dragon.lvl * 5
    cl.Dragon.hap += r.randint(1, 15)
    c()

def c():
    o.system('clear')

if __name__ == '__main__':
    main()
