from Dictionaries import *

def calcTypeMult(Attack, Gen, DefT1, DefT2):
    Type1Mult = 1
    Type2Mult = 1
    TotMult = ""
    Type1Dict = None
    Type2Dict = None

    if Gen == 1:
        if DefT1 == "Fire" or DefT1 == "Poison" or DefT1 == "Psychic" or DefT1 == "Bug":
            DefT1 = DefT1 + "G1"
        if DefT2 == "Fire" or DefT2 == "Poison" or DefT2 == "Psychic" or DefT2 == "Bug":
            DefT2 = DefT2 + "G1"

    if Gen == 2:
        if DefT1 == "Steel":
            DefT1 = "SteelG2"
        if DefT2 == "Steel":
            DefT2 = "SteelG2"


    Type1Dict = TypeDictList[DefT1]
    Type1Mult = Type1Dict[Attack]
    if DefT2 != "":
        Type2Dict = TypeDictList[DefT2]
        Type2Mult = Type2Dict[Attack]


    TotMult = Type1Mult * Type2Mult
    return TotMult

def calcSelfMult(SelfType1, SelfType2, Movetype, attackBoost, item, Gen):
    Stab = 1
    if SelfType1 == Movetype or SelfType2 == Movetype:
        Stab = 1.5
    atkBoost = AttackBonus[attackBoost]

    selfMult = Stab * atkBoost
    return selfMult