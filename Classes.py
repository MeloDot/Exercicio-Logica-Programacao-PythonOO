
class Vendedor(object):
    salarioFixo = 1585.00
    salarioTotal = 0

    def __init__(self, cd, nome):
        self.cd = cd
        self.nome = nome

class Produto(object):

    def __init__(self, cd, desc, vlUnitario):
        self.cd = cd
        self.desc = desc
        self.vlUnitario = vlUnitario



