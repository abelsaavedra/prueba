import random

from ow_chancla.classes.owchancla import OwChancla


def main():
    owchancla = OwChancla()

    meta_list = [
        'aatthh',
        'attthh',
        'aattth',
    ]

    meta = meta_list[random.randint(0, len(meta_list))]

    equipo1 = []
    equipo2 = []

    for m in meta:
        if m == 'a' or m == 'd':
            equipo1.append(owchancla.attack.pop())
            equipo2.append(owchancla.attack.pop())
        elif m == 't':
            equipo1.append(owchancla.tank.pop())
            equipo2.append(owchancla.tank.pop())
        elif m == 'h':
            equipo1.append(owchancla.healer.pop())
            equipo2.append(owchancla.healer.pop())

    random.shuffle(equipo1)
    print("\nEquipo 1 con {}".format(meta))
    for p in equipo1:
        print(p)

    random.shuffle(equipo2)
    print('\nEquipo 2 con {}'.format(meta))
    for p in equipo2:
        print(p)


if __name__ == "__main__":
    main()
