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
            "dam": {"min": getVal(item, ["ids", "eDamRaw", "minimum"]), "max": getVal(item, ["ids", "eDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "eDamPct", "minimum"]), "max": getVal(item, ["ids", "eDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "eMdRaw", "minimum"]), "max": getVal(item, ["ids", "eMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "eMdPct", "minimum"]), "max": getVal(item, ["ids", "eMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "eSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "eSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "eSpDamPct", "minimum"]), "max": getVal(item, ["ids", "eSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "eDefRaw", "minimum"]), "max": getVal(item, ["ids", "eDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "eDefPct", "minimum"]), "max": getVal(item, ["ids", "eDefPct", "maximum"])}, ##
        },
        
        "thunder":{
            "dam": {"min": getVal(item, ["ids", "tDamRaw", "minimum"]), "max": getVal(item, ["ids", "tDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "tDamPct", "minimum"]), "max": getVal(item, ["ids", "tDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "tMdRaw", "minimum"]), "max": getVal(item, ["ids", "tMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "tMdPct", "minimum"]), "max": getVal(item, ["ids", "tMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "tSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "tSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "tSpDamPct", "minimum"]), "max": getVal(item, ["ids", "tSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "tDefRaw", "minimum"]), "max": getVal(item, ["ids", "tDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "tDefPct", "minimum"]), "max": getVal(item, ["ids", "tDefPct", "maximum"])}, ##
        },
        
        "water":{
            "dam": {"min": getVal(item, ["ids", "wDamRaw", "minimum"]), "max": getVal(item, ["ids", "wDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "wDamPct", "minimum"]), "max": getVal(item, ["ids", "wDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "wMdRaw", "minimum"]), "max": getVal(item, ["ids", "wMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "wMdPct", "minimum"]), "max": getVal(item, ["ids", "wMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "wSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "wSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "wSpDamPct", "minimum"]), "max": getVal(item, ["ids", "wSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "wDefRaw", "minimum"]), "max": getVal(item, ["ids", "wDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "wDefPct", "minimum"]), "max": getVal(item, ["ids", "wDefPct", "maximum"])}, ##
        },
        
        "fire":{
            "dam": {"min": getVal(item, ["ids", "fDamRaw", "minimum"]), "max": getVal(item, ["ids", "fDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "fDamPct", "minimum"]), "max": getVal(item, ["ids", "fDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "fMdRaw", "minimum"]), "max": getVal(item, ["ids", "fMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "fMdPct", "minimum"]), "max": getVal(item, ["ids", "fMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "fSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "fSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "fSpDamPct", "minimum"]), "max": getVal(item, ["ids", "fSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "fDefRaw", "minimum"]), "max": getVal(item, ["ids", "fDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "fDefPct", "minimum"]), "max": getVal(item, ["ids", "fDefPct", "maximum"])}, ##
        },
        
        "air":{
            "dam": {"min": getVal(item, ["ids", "aDamRaw", "minimum"]), "max": getVal(item, ["ids", "aDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "aDamPct", "minimum"]), "max": getVal(item, ["ids", "aDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "aMdRaw", "minimum"]), "max": getVal(item, ["ids", "aMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "aMdPct", "minimum"]), "max": getVal(item, ["ids", "aMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "aSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "aSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "aSpDamPct", "minimum"]), "max": getVal(item, ["ids", "aSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "aDefRaw", "minimum"]), "max": getVal(item, ["ids", "aDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "aDefPct", "minimum"]), "max": getVal(item, ["ids", "aDefPct", "maximum"])}, ##
        },
        
        "elemental":{
            "dam": {"min": getVal(item, ["ids", "rDamRaw", "minimum"]), "max": getVal(item, ["ids", "rDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "rDamPct", "minimum"]), "max": getVal(item, ["ids", "rDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "rMdRaw", "minimum"]), "max": getVal(item, ["ids", "rMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "rMdPct", "minimum"]), "max": getVal(item, ["ids", "rMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "rSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "rSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "rSpDamPct", "minimum"]), "max": getVal(item, ["ids", "rSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "rDefRaw", "minimum"]), "max": getVal(item, ["ids", "rDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "rDefPct", "minimum"]), "max": getVal(item, ["ids", "rDefPct", "maximum"])}, ##
        },
        
        "neutral":{
            "dam": {"min": getVal(item, ["ids", "nDamRaw", "minimum"]), "max": getVal(item, ["ids", "nDamRaw", "maximum"])}, ##
            "dam%": {"min": getVal(item, ["ids", "nDamPct", "minimum"]), "max": getVal(item, ["ids", "nDamPct", "maximum"])}, ##
            "meleeDam": {"min": getVal(item, ["ids", "nMdRaw", "minimum"]), "max": getVal(item, ["ids", "nMdRaw", "maximum"])}, ##
            "meleeDam%": {"min": getVal(item, ["ids", "nMdPct", "minimum"]), "max": getVal(item, ["ids", "nMdPct", "maximum"])}, ##
            "spellDam": {"min": getVal(item, ["ids", "nSpDamRaw", "minimum"]), "max": getVal(item, ["ids", "nSpDamRaw", "maximum"])}, ##
            "spellDam%": {"min": getVal(item, ["ids", "nSpDamPct", "minimum"]), "max": getVal(item, ["ids", "nSpDamPct", "maximum"])}, ##
            "def": {"min": getVal(item, ["ids", "nDefRaw", "minimum"]), "max": getVal(item, ["ids", "nDefRaw", "maximum"])}, ##
            "def%": {"min": getVal(item, ["ids", "nDefPct", "minimum"]), "max": getVal(item, ["ids", "nDefPct", "maximum"])}, ##
        },

        "poision": {"min": getVal(item, ["ids", "poison", "minimum"]), "max":getVal(item, ["ids", "poison", "maximum"])}, ##
        "spellDam": {"min": getVal(item, ["ids", "sdRaw", "minimum"]), "max":getVal(item, ["ids", "sdRaw", "maximum"])}, ##
        "spellDam%": {"min": getVal(item, ["ids", "sdPct", "minimum"]), "max":getVal(item, ["ids", "sdPct", "maximum"])}, ##
        "manaSteal": {"min": getVal(item, ["ids", "ms", "minimum"]), "max":getVal(item, ["ids", "ms", "maximum"])}, ##
        "manaReg": {"min": getVal(item, ["ids", "mr", "minimum"]), "max":getVal(item, ["ids", "mr", "maximum"])}, ##
        "healthReg": {"min": getVal(item, ["ids", "hprRaw", "minimum"]), "max":getVal(item, ["ids", "hprRaw", "maximum"])}, ##
        "helthReg%": {"min": getVal(item, ["ids", "hprPct", "minimum"]), "max":getVal(item, ["ids", "hprPct", "maximum"])}, ##
        "health": {"min": getVal(item, ["ids", "hpBonus", "minimum"]), "max":getVal(item, ["ids", "hpBonus", "maximum"])}, ##
        "LifeSteal": {"min": getVal(item, ["ids", "ls", "minimum"]), "max":getVal(item, ["ids", "ls", "maximum"])}, ##
        "walkSpd": {"min": getVal(item, ["ids", "wSdRaw", "minimum"]), "max":getVal(item, ["ids", "wSdRaw", "maximum"])}, ##
        "walkSpd%": {"min": getVal(item, ["ids", "wSdPct", "minimum"]), "max":getVal(item, ["ids", "wSdPct", "maximum"])}, ##
        "sprintReg": {"min": getVal(item, ["ids", "spritReg", "minimum"]), "max":getVal(item, ["ids", "spritReg", "maximum"])}, ##
        "jumpHight": {"min": getVal(item, ["ids", "jh", "minimum"]), "max":getVal(item, ["ids", "jh", "maximum"])}, ##
        "sprint": {"min": getVal(item, ["ids", "sprit", "minimum"]), "max":getVal(item, ["ids", "sprit", "maximum"])}, ##
        
        ##"1stSpellCost": {"min": 0, "max":0},
        ##"1stSpellCost%": {"min": 0, "max":0},
        ##"2ndSpellCost": {"min": 0, "max":0},
        ##"2ndSpellCost%": {"min": 0, "max":0},
        ##"3edSpellCost": {"min": 0, "max":0},
        ##"3edSpellCost%": {"min": 0, "max":0},
        ##"4thSpellCost": {"min": 0, "max":0},
        ##"4thSpellCost%": {"min": 0, "max":0},

        "lootBonus": {"min": getVal(item, ["ids", "lb", "minimum"]), "max":getVal(item, ["ids", "lb", "maximum"])}, ##
        "xpBonus": {"min": getVal(item, ["ids", "xpb", "minimum"]), "max":getVal(item, ["ids", "xpb", "maximum"])}, ##
        "stealing": {"min": getVal(item, ["ids", "eSteal", "minimum"]), "max":getVal(item, ["ids", "eSteal", "maximum"])}, ##
        "lootQualty": {"min": getVal(item, ["ids", "lq", "minimum"]), "max":getVal(item, ["ids", "lq", "maximum"])}, ##
        "gatherXPBonus": {"min": getVal(item, ["ids", "gXp", "minimum"]), "max":getVal(item, ["ids", "gXp", "maximum"])}, ##
        "gatherSpeed": {"min": getVal(item, ["ids", "gSpd", "minimum"]), "max":getVal(item, ["ids", "gSpd", "maximum"])}, ##

        "dam%": {"min": getVal(item, ["ids", "damPct", "minimum"]), "max":getVal(item, ["ids", "damPct", "maximum"])}, ##
        "melDam": {"min": getVal(item, ["ids", "mdRaw", "minimum"]), "max":getVal(item, ["ids", "mdRaw", "maximum"])}, ##
        "melDam%": {"min": getVal(item, ["ids", "mdPct", "minimum"]), "max":getVal(item, ["ids", "mdPct", "maximum"])}, ##
        #"critDmg": {"min": 0, "max":0},
        "exploding": {"min": getVal(item, ["ids", "expd", "minimum"]), "max":getVal(item, ["ids", "expd", "maximum"])}, ##
        "reflection": {"min": getVal(item, ["ids", "ref", "minimum"]), "max":getVal(item, ["ids", "ref", "maximum"])}, ##
        "thorns": {"min": getVal(item, ["ids", "thorns", "minimum"]), "max":getVal(item, ["ids", "thorns", "maximum"])}, ##
        "atkSpd": {"min": getVal(item, ["ids", "atkTier", "minimum"]), "max":getVal(item, ["ids", "atkTier", "maximum"])} ##
    }
    newData.append(newItem)

print(newData[0]["skills"])