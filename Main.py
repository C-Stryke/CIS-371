from Functions import *

attackBoost = None
item = None

def main():
    while True:
        SelfType1 = input("What is the First type of the Attacking Pokemon ")
        if SelfType1 in Types:
            break
        print("Please enter a valid type ")
    while True:
        SelfType2 = input("What is the Second type of the Attacking Pokemon ")
        if SelfType2 in Types:
            break
        print("Please enter a valid type ")
    while True:
        MoveType = input("What Type of Move are you using ")
        if MoveType in Types:
            break
        print("Please enter a valid type ")
    while True:
        Gen = int(input("What Generation Game are you Playing "))
        if Gen > 0 and Gen <= 9:
            break
        print("Please enter a valid Gen ")
    while True:
        EnemyType1 = input("What is the First type of the Defending Pokemon ")
        if EnemyType1 in Types:
            break
        print("Please enter a valid type ")
    while True:
        EnemyType2 = input("What is the Second type of the Defending Pokemon ")
        if EnemyType2 in Types:
            break
        print("Please enter a valid type ")
    while True:
        attackBoost = input("What is the Attack Boost of your Pokemon ")
        if attackBoost in AttackBonus:
            break
        print("Please enter a valid number ")
    TypeTotal = calcTypeMult(MoveType, Gen, EnemyType1, EnemyType2)
    SelfTotal = calcSelfMult(SelfType1, SelfType2, MoveType, attackBoost, item, Gen)
    Total = TypeTotal * SelfTotal
    print("Total Damage Multiplier " + str(Total))
    return


if __name__ == '__main__':
    main()