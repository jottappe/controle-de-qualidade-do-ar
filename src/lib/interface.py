from lib.progress_bar import *
import math


def line():
    return 30 * '-'


def title(text):
    print(line())
    print(text.center(30))
    print(line())


def menu(args):
    title('MENU')
    c = 1
    for arg in args:
        print(f'[{c}] - {arg}')
        c += 1
    print(line())


def progress():
    numbers = [x * 5 for x in range(1000, 2000)]
    result = []

    progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        result.append(math.factorial(x))
        progress_bar(i + 1, len(numbers))
