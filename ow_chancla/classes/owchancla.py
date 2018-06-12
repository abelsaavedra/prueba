import random

import openpyxl

from ow_chancla.classes.heroe import Heroe


class OwChancla(object):

    def __init__(self):
        self.attack = []
        self.defense = []
        self.tank = []
        self.healer = []
        self.__cargar__()

    def __cargar__(self):

        wb = openpyxl.load_workbook(filename='ow.xlsx', read_only=True)
        ws = wb['Heroes']
        sw_primera_vez = False

        for row in ws.rows:
            if sw_primera_vez:
                heroe = Heroe(row[0].value,
                              row[1].value,
                              row[2].value,
                              row[3].value,
                              row[4].value)
                if heroe.tipoAnterior == 'Ataque':
                    self.attack.append(heroe)
                elif heroe.tipoAnterior == 'Defensa':
                    self.defense.append(heroe)
                elif heroe.tipoAnterior == 'Tanque':
                    self.tank.append(heroe)
                elif heroe.tipoAnterior == 'Apoyo':
                    self.healer.append(heroe)
            else:
                sw_primera_vez = True

        random.shuffle(self.attack)
        random.shuffle(self.defense)
        random.shuffle(self.tank)
        random.shuffle(self.healer)