import random

class Hero:

    #constructor for hero
    def __init__(self, name, style, lvl, xp, win, draw, loss, strength, accuracy, speed, body, heart, soul):
        self.name = name
        self.style = style

        if self.style == 'Balanced':
            modStrength = 0
            modAccuracy = 0
            modSpeed = 0
            modBody = 0
            modHeart = 0
            modSoul = 0
            blockDodge = 5
        elif self.style == 'Brawler':
            modStrength = 2
            modAccuracy = -2
            modSpeed = 0
            modBody = 2
            modHeart = 1
            modSoul = -3
            blockDodge = 7
        elif self.style == 'Mage':
            modStrength = -3
            modAccuracy = 2
            modSpeed = 0
            modBody = -2
            modHeart = 0
            modSoul = 3
            blockDodge = 4
        elif self.style == 'Grappler':
            modStrength = 2
            modAccuracy = 1
            modSpeed = -1
            modBody = 0
            modHeart = 0
            modSoul = -2
            blockDodge = 5
        elif self.style == 'Boxer':
            modStrength = 1
            modAccuracy = 1
            modSpeed = 0
            modBody = 0
            modHeart = 0
            modSoul = -2
            blockDodge = 5
        elif self.style == 'MMA':
            modStrength = 1
            modAccuracy = 0
            modSpeed = 1
            modBody = 0
            modHeart = 1
            modSoul = -3
            blockDodge = 5
        elif self.style == 'BattleMage':
            modStrength = 1
            modAccuracy = 0
            modSpeed = -2
            modBody = 1
            modHeart = -2
            modSoul = 2
            blockDodge = 6
        elif self.style == 'Rogue':
            modStrength = -1
            modAccuracy = 3
            modSpeed = 3
            modBody = -3
            modHeart = -1
            modSoul = -1
            blockDodge = 3
        else:
            modStrength = 0
            modAccuracy = 0
            modSpeed = 0
            modBody = 0
            modHeart = 0
            modSoul = 0

        self.level = lvl
        self.experience = xp
        self.win = win
        self.draw = draw
        self.loss = loss

        self.strength = strength + modStrength
        self.accuracy = accuracy + modAccuracy
        self.speed = speed + modSpeed
        self.body = body + modBody
        self.heart = heart + modHeart
        self.soul = soul + modSoul

        self.health = 5 * (10 + int(self.body) + int(self.heart))
        self.tempHealth = self.health
        self.stamina = 3 * (10 + int(self.body) + int(self.soul))
        self.tempStamina = self.stamina
        self.mana = 3 * (10 + int(self.heart) + int(self.soul))
        self.tempMana = self.mana

    #to string for hero
    def __str__(self):
        return 'Name: ' + self.name + '\nStyle: ' + self.style + \
               '\nLevel: ' + str(self.level) + '\tExperience: ' + str(self.experience) + \
               '\nW/D/L: ' + str(self.win) + '/' + str(self.draw) + '/' + str(self.loss) + \
               '\nHealth: ' + str(self.health) + '\tStamina: ' + str(self.stamina) + '\tMana: ' \
               + str(self.mana) + '\nStrength: ' + str(self.strength) + '\nAccuracy: '+ str(self.accuracy)\
               + '\nSpeed: ' + str(self.speed) + '\nBody: ' + str(self.body) + '\nHeart: '\
               + str(self.heart) + '\nSoul: ' + str(self.soul)

class Commands:

    #command used for generating a number between roll & int
    def roll(int):
        return random.randint(1, int)

    #command used for printing
    def printMatchUp(player1, player2):
        print('====================================')
        print(player1)
        print('=================VS=================')
        print(player2)
        print('====================================')

    #command used for resetting health, stamina, and mana
    def matchBegin(player1, player2):
        player1.tempHealth = player1.health
        player1.tempStamina = player1.stamina
        player1.tempMana = player1.mana
        player2.tempHealth = player2.health
        player2.tempStamina = player2.stamina
        player2.tempMana = player2.mana
        Commands.printMatchUp(player1, player2)

    def blockDodge(self):
        ceiling = self.blockDodge
        roll = Commands.roll(10)

        if roll <= ceiling:
            return 'Block'
        else:
            return 'Dodge'

    def isCrit(roll):
        if roll == 20:
            return True
        else:
            return False

    def attackHit(player1, player2):
        roll1 = Commands.roll(20)
        roll2 = Commands.roll(20)

        blockDodge = Commands.blockDodge(player2)
        crit = Commands.isCrit(roll1)
        if blockDodge == 'Block':
            if (player1.strength + player1.accuracy + roll1) >= (player2.body + player2.heart + roll2) and crit:
                print(player2.name, ' tries to block.')
                print('It fails!', player1.name, 'lands critical blow!')
                return 2
            elif (player1.strength + player1.accuracy + roll1) >= (player2.body + player2.heart + roll2) and not crit:
                print(player2.name, ' tries to block.')
                print('It fails!', player1.name, 'lands a strike!')
                return 1
            else:
                print(player2.name, 'is able to block it')
                return 0
        else:
            if (player1.strength + player1.accuracy + roll1) >= (player2.speed + player2.soul + roll2) and crit:
                print(player2.name, ' tries to dodge.')
                print('It fails!', player1.name, 'lands a critical blow!')
                return 2
            elif (player1.strength + player1.accuracy + roll1) >= (player2.speed + player2.soul + roll2) and not crit:
                print(player2.name, ' tries to dodge.')
                print('It fails!', player1.name, 'lands a strike!')
                return 1
            else:
                print(player2.name, 'is dodges out of the way!')
                return 0


    #command used to determine the attack type of the attacker based on fight style
#main to essentially test
x = Hero('Jeff', 'Grappler', 1, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3)
y = Hero('Steve', 'Rogue', 1, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3)
x.tempHealth = 1
print(x.tempHealth)
Commands.matchBegin(x, y)
print(x.tempHealth, 'test')

