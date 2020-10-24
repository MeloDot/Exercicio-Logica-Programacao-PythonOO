
class Vendedor(object):

    def __init__(self, cd, nome):
        self.cd = cd
        self.nome = nome

class Produto(object):

    def __init__(self, cd, desc, vlUnitario):
        self.cd = cd
        self.desc = desc
        self.vlUnitario = vlUnitario
class Venda(object):

    def __init__(self, cdVendedor, nmVendedor, cdProduto, descProduto, quantVendida, vlUnitario):
        self.cdVendedor = cdVendedor
        self.nmVendedor = nmVendedor
        self.cdProduto = cdProduto
        self.descProduto = descProduto
        self.quantVendida = quantVendida
        self.vlUnitario = vlUnitario
