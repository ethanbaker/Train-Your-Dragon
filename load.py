import classes as cl
import json

def load_game():
    with open('dragon.json', 'r') as pfile:
        jlp = json.load(pfile)
        cl.Player.htp = jp['htp']
        cl.Player.att = jp['att']
        cl.Player.dfc = jp['dfc']
        cl.Player.dog = jp['dog']
        cl.Player.sta = jp['sta']
        cl.Player.spd = jp['spd']
        cl.Player.hap = jp['hap']
        cl.Player.name = jp['name']


