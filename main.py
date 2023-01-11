import random


def lottery():
    num1m = random.randrange(1, 70)
    num2m = random.randrange(1, 70)
    num3m = random.randrange(1, 70)
    num4m = random.randrange(1, 70)
    num5m = random.randrange(1, 70)

    num1p = random.randrange(1, 69)
    num2p = random.randrange(1, 69)
    num3p = random.randrange(1, 69)
    num4p = random.randrange(1, 69)
    num5p = random.randrange(1, 69)

    mb = random.randrange(1, 25)
    pb = random.randrange(1, 26)

    result_m = (sorted([num1m, num2m, num3m, num4m, num5m]))
    result_p = (sorted([num1p, num2p, num3p, num4p, num5p]))

    game = input('Are you playing Mega Millions or Powerball?: ')
    print()
    game = game.lower()

    if game.startswith('m'):
        print('Random number between 1 and 70')
        print(result_m)
        print()
        print('Megaball Number')
        print(mb)
    elif game.startswith('p'):
        print('Random number between 1 and 69')
        print(result_p)
        print()
        print('Powerball Number')
        print(pb)
    else:
        print('You did not select a valid game')


lottery()
