# import random

# for i in range(3):
#     print(random.randint(10, 20))
#
# members = ['Eric', 'Rosa', 'Jordan']
# leader = random.choice(members)
# print(leader)

# search Python 3 Module Index for all of pythons built in modules with examples and help
import random


class Dice:
    def __init__(self, dice_type):
        self.dice_type = dice_type
        self.dice = [0, 0]

    def roll(self):
        self.dice[0] = random.randint(1, self.dice_type)
        self.dice[1] = random.randint(1, self.dice_type)
        return self.dice[0], self.dice[1]


print('Starting dice role...')
my_dice = Dice(6)
for i in range(3):
    print(my_dice.roll())
