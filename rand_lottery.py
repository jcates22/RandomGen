import random


def rand_lottery():
    """
    Selects game based on user input, then iterates over a range of 5 numbers. The underscore (_) is a placeholder
    variable that is used to store the current value of the range. However, in this case, the underscore is not used
    to store the value of the range, so it is essentially ignored.

    The for loop will iterate X times, and at each iteration, the value of _ will be incremented by 1. The code
    inside the for loop will be executed 5 times, once for each value of _.

    """

    game = input('Are you playing Cash4Life, Fantasy 5, Mega Millions, or Powerball?: ')
    print()
    game = game.lower()

    if game.startswith('c'):
        for _ in range(49):
            print(f'Random number {_} between 1 and 60')
            num1c = random.randrange(1, 61)
            num2c = random.randrange(1, 61)
            num3c = random.randrange(1, 61)
            num4c = random.randrange(1, 61)
            num5c = random.randrange(1, 61)
            result_c = sorted([num1c, num2c, num3c, num4c, num5c])
            print(result_c)
            print()
            print('Cash Ball')
            cb = random.randrange(1, 5)
            print(cb)
            print('-' * 30)
    elif game.startswith('f'):
        for _ in range(49):
            print(f'Random number {_} between 1 and 42')
            num1f = random.randrange(1, 43)
            num2f = random.randrange(1, 43)
            num3f = random.randrange(1, 43)
            num4f = random.randrange(1, 43)
            num5f = random.randrange(1, 43)
            result_f = sorted([num1f, num2f, num3f, num4f, num5f])
            print(result_f)
            print('-' * 30)
    elif game.startswith('m'):
        for _ in range(49):
            print(f'Random number {_} between 1 and 70')
            num1m = random.randrange(1, 71)
            num2m = random.randrange(1, 71)
            num3m = random.randrange(1, 71)
            num4m = random.randrange(1, 71)
            num5m = random.randrange(1, 71)
            result_m = sorted([num1m, num2m, num3m, num4m, num5m])
            print(result_m)
            print()
            print('Megaball Number')
            mb = random.randrange(1, 26)
            print(mb)
            print('-' * 30)
    elif game.startswith('p'):
        for _ in range(49):
            print(f'Random number {_+1} between 1 and 69')
            num1p = random.randrange(1, 70)
            num2p = random.randrange(1, 70)
            num3p = random.randrange(1, 70)
            num4p = random.randrange(1, 70)
            num5p = random.randrange(1, 70)
            result_p = sorted([num1p, num2p, num3p, num4p, num5p])
            print(result_p)
            print()
            print('Powerball Number')
            pb = random.randrange(1, 27)
            print(pb)
            print('-' * 30)
    else:
        print('You did not select a valid game')


rand_lottery()
