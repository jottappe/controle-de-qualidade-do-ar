import math


def line():
    return 30 * "-"


def title(text):
    print(line())
    print(text.center(30))
    print(line())


def menu(args):
    title("MENU")
    c = 1
    for arg in args:
        print(f"[{c}] - {arg}")
        c += 1
    print(line())
