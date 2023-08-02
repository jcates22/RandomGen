import random


def lottery():
    num1m = random.randint(1, 70)
    num2m = random.randint(1, 70)
    num3m = random.randint(1, 70)
    num4m = random.randint(1, 70)
    num5m = random.randint(1, 70)

    num1p = random.randint(1, 69)
    num2p = random.randint(1, 69)
    num3p = random.randint(1, 69)
    num4p = random.randint(1, 69)
    num5p = random.randint(1, 69)

    num1f = random.randint(1, 42)
    num2f = random.randint(1, 42)
    num3f = random.randint(1, 42)
    num4f = random.randint(1, 42)
    num5f = random.randint(1, 42)

    mb = random.randint(1, 25)
    pb = random.randint(1, 26)

    result_m = (sorted([num1m, num2m, num3m, num4m, num5m]))
    result_p = (sorted([num1p, num2p, num3p, num4p, num5p]))
    result_f = (sorted([num1f, num2f, num3f, num4f, num5f]))

    game = input('Are you playing Fantasy 5, Mega Millions, or Powerball?: ')
    print()
    game = game.lower()

    if game.startswith('f'):
        print('Random number between 1 and 42')
        print(result_f)
    elif game.startswith('m'):
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
