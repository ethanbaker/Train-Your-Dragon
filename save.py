import json
import classes as cl
from time import sleep as s
import colors as co

def save_anim():
    c()
    print(co.m + 'Saving game.')
    s(.35)
    c()
    print(co.m + 'Saving game..')
    s(.35)
    c()
    print(co.m + 'Saving game...')
    s(.35)
    c()
    print(co.m + 'Saving game.')
    s(.35)
    c()
    print(co.m + 'Saving game..')
    s(.35)
    c()
    print(co.m + 'Saving game...')
    s(.35)
    c()

def c():
    print(co.cl)


def save_game():
    save_anim()

    with open('dragon.json', 'w') as saved:
        saved.write(json.dumps({
            "htp":cl.Dragon.htp,
            "att":cl.Dragon.att,
            "dfc":cl.Dragon.dfc,
            "sta":cl.Dragon.sta,
            "dog":cl.Dragon.dog,
            "spd":cl.Dragon.spd,
            "hap":cl.Dragon.hap,
            "name":cl.Dragon.name,
            "color":cl.Dragon.color,
            "xp":cl.Dragon.xp,
            "lvl":cl.Dragon.lvl,
            }))


