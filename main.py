import random


def lottery():
    num1 = random.randrange(1, 69)
    num2 = random.randrange(1, 69)
    num3 = random.randrange(1, 69)
    num4 = random.randrange(1, 69)
    num5 = random.randrange(1, 69)
    mb = random.randrange(1, 25)
    pb = random.randrange(1, 26)
    result = (sorted([num1, num2, num3, num4, num5]))
    game = input('Are you playing Mega Millions or Powerball?: ')
    game = game.lower()
    if game.startswith('m'):
        print('Random number between 1 and 69')
        print(result)
        print('Megaball Number')
        print(mb)
    elif game.startswith('p'):
        print('Random number between 1 and 69')
        print(result)
        print('Powerball Number')
        print(pb)
    else:
        print('You did not select a valid game')


lottery()
