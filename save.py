import json
import classes as cl

def save_game():
    with open('dragon.json', 'w') as saved:
        saved.write(json.dumps({
            "htp":cl.Player.htp,
            "att":cl.Player.att,
            "dfc":cl.Player.dfc,
            "sta":cl.Player.sta,
            "dog":cl.Player.dog,
            "spd":cl.Player.spd,
            "hap":cl.Player.hap,
            "name":cl.Player.name
            }))
