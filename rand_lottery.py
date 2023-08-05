import random


def rand_lottery(start, stop, step):
    """
  Prints multiple random values on the same line.

  Args:
    start: The starting number of the range.
    stop: The end number of the range.
    step: The step size of the range.

  Returns:
    Nothing.
  """

    for i in range(start, stop, step):
        print(random.randrange(i, i + step), end=" ")


game = input('Are you playing Cash4Life, Fantasy 5, Mega Millions, or Powerball?: ')
print()
game = game.lower()

if game.startswith('c'):
    for _ in range(5):
        print('Random number between 1 and 60')
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
        print("-" * 30)
elif game.startswith('f'):
    for _ in range(5):
        print('Random number between 1 and 42')
        num1f = random.randrange(1, 43)
        num2f = random.randrange(1, 43)
        num3f = random.randrange(1, 43)
        num4f = random.randrange(1, 43)
        num5f = random.randrange(1, 43)
        result_f = sorted([num1f, num2f, num3f, num4f, num5f])
        print(result_f)
        print("-" * 30)
elif game.startswith('m'):
    for _ in range(5):
        print('Random number between 1 and 70')
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
        print("-" * 30)
elif game.startswith('p'):
    for _ in range(5):
        print('Random number between 1 and 69')
        num1p = random.randrange(1, 70)
        num2p = random.randrange(1, 70)
        num3p = random.randrange(1, 70)
        num4p = random.randrange(1, 70)
        num5p = random.randrange(1, 70)
        result_p = sorted([num1p, num2p, num3p, num4p, num5p])
        print(result_p)
        print()
        print('Megaball Number')
        pb = random.randrange(1, 27)
        print(pb)
        print("-" * 30)
else:
    print('You did not select a valid game')
