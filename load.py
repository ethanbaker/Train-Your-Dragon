import classes as cl
import json
from time import sleep as s
import colors as co
def load_anim():
    c()
    print(co.m + 'Loading game.')
    s(.35)
    c()
    print(co.m + 'Loading game..')
    s(.35)
    c()
    print(co.m + 'Loading game...')
    s(.35)
    c()
    print(co.m + 'Loading game.')
    s(.35)
    c()
    print(co.m + 'Loading game..')
    s(.35)
    c()
    print(co.m + 'Loading game...')
    s(.35)
    c()

def load_game():
    load_anim()

    with open('dragon.json', 'r') as pfile:
        jlp = json.load(pfile)
        cl.Dragon.htp = jlp['htp']
        cl.Dragon.att = jlp['att']
        cl.Dragon.dfc = jlp['dfc']
        cl.Dragon.dog = jlp['dog']
        cl.Dragon.sta = jlp['sta']
        cl.Dragon.spd = jlp['spd']
        cl.Dragon.hap = jlp['hap']
        cl.Dragon.name = jlp['name']
        cl.Dragon.color = jlp['color']
        cl.Dragon.xp = jlp['xp']
        cl.Dragon.lvl = jlp['lvl']

def load_scores():
    with open('highScores.json', 'r') as ppfile:
        jp = json.load(ppfile)
        cl.highScores.attack = jp['attack']
        cl.highScores.defense = jp['defense']
        cl.highScores.dodge = jp['dodge']
        cl.highScores.speed = jp['speed']
        cl.highScores.stamina = jp['stamina']

def c():
    print(co.cl)
