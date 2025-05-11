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

        "durrability": max(getVal(item, ["itemIDs", "dura"]), getVal(item, ["consumableIDs", "dura"])) , ##
        "str": {"min": getVal(item, ["ids", "str", "minimum"]), "max": getVal(item, ["ids", "str", "maximum"])}, ##
        "int": {"min": getVal(item, ["ids", "int", "minimum"]), "max": getVal(item, ["ids", "int", "maximum"])}, ##
        "agi": {"min": getVal(item, ["ids", "agi", "minimum"]), "max": getVal(item, ["ids", "agi", "maximum"])}, ##
        "def": {"min": getVal(item, ["ids", "def", "minimum"]), "max": getVal(item, ["ids", "def", "maximum"])}, ##
        "dex": {"min": getVal(item, ["ids", "dex", "minimum"]), "max": getVal(item, ["ids", "dex", "maximum"])}, ##

        "strReq": item["itemIDs"]["strReq"],
        "intReq": item["itemIDs"]["intReq"],
        "agiReq": item["itemIDs"]["agiReq"],
        "defReq": item["itemIDs"]["defReq"],
        "dexReq": item["itemIDs"]["dexReq"],

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

        "poision": {"min": getVal(item, ["ids", "poison", "minimum"]), "max":getVal(item, ["ids", "poison", "maximum"])}, ##
        "spellDam": {"min": 0, "max":0},
        "spellDam%": {"min": 0, "max":0},
        "manaSteal": {"min": getVal(item, ["ids", "ms", "minimum"]), "max":getVal(item, ["ids", "ms", "maximum"])}, ##
        "manaReg": {"min": getVal(item, ["ids", "mr", "minimum"]), "max":getVal(item, ["ids", "mr", "maximum"])}, ##
        "healthReg": {"min": getVal(item, ["ids", "hprRaw", "minimum"]), "max":getVal(item, ["ids", "hprRaw", "maximum"])}, ##
        "helthReg%": {"min": getVal(item, ["ids", "hprPct", "minimum"]), "max":getVal(item, ["ids", "hprPct", "maximum"])}, ##
        "health": {"min": 0, "max":0},
        "LifeSteal": {"min": getVal(item, ["ids", "ls", "minimum"]), "max":getVal(item, ["ids", "ls", "maximum"])}, ##
        "walkSpd": {"min": getVal(item, ["ids", "wSdRaw", "minimum"]), "max":getVal(item, ["ids", "wSdRaw", "maximum"])}, ##
        "walkSpd%": {"min": getVal(item, ["ids", "wSdPct", "minimum"]), "max":getVal(item, ["ids", "wSdPct", "maximum"])}, ##
        "sprintReg": {"min": getVal(item, ["ids", "spritReg", "minimum"]), "max":getVal(item, ["ids", "spritReg", "maximum"])},
        "jumpHight": {"min": getVal(item, ["ids", "jh", "minimum"]), "max":getVal(item, ["ids", "jh", "maximum"])},
        "sprint": {"min": getVal(item, ["ids", "sprit", "minimum"]), "max":getVal(item, ["ids", "sprit", "maximum"])},

        "1stSpellCost": {"min": 0, "max":0},
        "1stSpellCost%": {"min": 0, "max":0},
        "2ndSpellCost": {"min": 0, "max":0},
        "2ndSpellCost%": {"min": 0, "max":0},
        "3edSpellCost": {"min": 0, "max":0},
        "3edSpellCost%": {"min": 0, "max":0},
        "4thSpellCost": {"min": 0, "max":0},
        "4thSpellCost%": {"min": 0, "max":0},

        "lootBonus": {"min": getVal(item, ["ids", "lb", "minimum"]), "max":getVal(item, ["ids", "lb", "maximum"])},
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