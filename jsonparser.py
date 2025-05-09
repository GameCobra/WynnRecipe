import json

newData = []

with open('original.json', 'r') as file:
    data = json.load(file)

#print(getVal(data, [0, "skills"]))
def getVal(object, dir):
    try:
        value = object
        for i in dir:
            value = value[i]
        return value
    except:
        return 0

for item in data:
    newItem = {
        "name": item["name"], ##
        "level": item["lvl"], ##
        "stars": item["tier"], ##
        "skills": {
            "Weaponsmithing": "WEAPONSMITHING" in item["skills"], ##
            "Woodworking": "WOODWORKING" in item["skills"], ##
            "Scribing": "SCRIBING" in item["skills"], ##
            "Jeweling": "JEWELING" in item["skills"], ##
            "Alchemism": "ALCHEMISM" in item["skills"], ##
            "Cooking": "COOKING" in item["skills"], ##
            "Armouring": "ARMOURING" in item["skills"], ##
            "Tailoring": "TAILORING" in item["skills"] ##
        },

        "durrability": item["itemIDs"]["dura"], ##
        "str": {"min": getVal(item, ["str", "minimum"]), "max": getVal(item, ["str", "maximum"])},
        "int": {"min": getVal(item, ["int", "minimum"]), "max": getVal(item, ["int", "maximum"])},
        "agi": {"min": getVal(item, ["agi", "minimum"]), "max": getVal(item, ["agi", "maximum"])},
        "def": {"min": getVal(item, ["def", "minimum"]), "max": getVal(item, ["def", "maximum"])},
        "dex": {"min": getVal(item, ["dex", "minimum"]), "max": getVal(item, ["dex", "maximum"])},

        "strReq": 0,
        "intReq": 0,
        "agiReq": 0,
        "defReq": 0,
        "dexReq": 0,

        "earth":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },
        
        "thunder":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },
        
        "water":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },
        
        "fire":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },
        
        "air":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },
        
        "elemental":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },
        
        "neutral":{
            "dam": {"min": 0, "max":0},
            "dam%": {"min": 0, "max":0},
            "mainDam": {"min": 0, "max":0},
            "mainDam%": {"min": 0, "max":0},
            "spellDam": {"min": 0, "max":0},
            "spellDam%": {"min": 0, "max":0},
            "def": {"min": 0, "max":0}
        },

        "poision": {"min": 0, "max":0},
        "spellDam": {"min": 0, "max":0},
        "spellDam%": {"min": 0, "max":0},
        "manaSteal": {"min": 0, "max":0},
        "manaReg": {"min": 0, "max":0},
        "healthReg": {"min": 0, "max":0},
        "helthReg%": {"min": 0, "max":0},
        "health": {"min": 0, "max":0},
        "LifeSteal": {"min": 0, "max":0},
        "walkSpd": {"min": 0, "max":0},
        "sprintReg": {"min": 0, "max":0},
        "jumpHight": {"min": 0, "max":0},
        "sprint": {"min": 0, "max":0},

        "1stSpellCost": {"min": 0, "max":0},
        "1stSpellCost%": {"min": 0, "max":0},
        "2ndSpellCost": {"min": 0, "max":0},
        "2ndSpellCost%": {"min": 0, "max":0},
        "3edSpellCost": {"min": 0, "max":0},
        "3edSpellCost%": {"min": 0, "max":0},
        "4thSpellCost": {"min": 0, "max":0},
        "4thSpellCost%": {"min": 0, "max":0},

        "lootBonus": {"min": 0, "max":0},
        "xpBonus": {"min": 0, "max":0},
        "stealing": {"min": 0, "max":0},
        "lootQualty": {"min": 0, "max":0},
        "gatherXPBonus": {"min": 0, "max":0},
        "gatherSpeed": {"min": 0, "max":0},

        "dmg": {"min": 0, "max":0},
        "critDmg": {"min": 0, "max":0},
        "exploding": {"min": 0, "max":0},
        "mainAtkRange": {"min": 0, "max":0},
        "reflection": {"min": 0, "max":0},
        "slowEn": {"min": 0, "max":0},
        "thorns": {"min": 0, "max":0},
        "weakenEn": {"min": 0, "max":0},
    }
    newData.append(newItem)

print(newData[0]["skills"])