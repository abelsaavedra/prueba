class Pokemon:
    nombre = ""
    vida_base = 0
    ataques = {}

    def __init__(self, nombre="", vida_base=0, ataques={}):
        self.nombre = nombre
        self.vida_base = vida_base
        self.ataques = ataques

    def atacar(self, enemigo, tipo="Básico"):
        enemigo.recibir_ataque(self.ataques[tipo])
        print("{} recibe ataque {} {} de {}".format(enemigo.nombre, tipo, self.ataques[tipo], self.get_nombre()))
        print("{} tiene {} puntos de vida \n".format(enemigo.get_nombre(), enemigo.get_puntos_vida()))

    def get_ataques(self):
        return self.ataques

    def recibir_ataque(self, puntos):
        self.vida_base -= puntos

    def get_puntos_vida(self):
        return self.vida_base

    def get_nombre(self):
        return self.nombre


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 90, {"Básico": 8})


class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 80, {"Básico": 7})


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 100, {"Básico": 10})


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 100, {"Básico": 8, "Chispazo": 10, "Bola voltio": 12})
