class Heroe(object):

    def __init__(self, id, nombre, nombreAlternativo, tipo, tipoAnterior):
        self.id = id
        self.nombre = nombre
        self.nombreAlternativo = nombreAlternativo
        self.tipo = tipo
        self.tipoAnterior = tipoAnterior

    def __str__(self):
        return "{} de {}".format(self.nombre, self.tipoAnterior)
