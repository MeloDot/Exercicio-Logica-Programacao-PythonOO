from Classes import Vendedor
from Classes import Produto
from Classes import Venda

vendedores = []
produtos = []
vendas = []
def pegarPorCodigo(cd, lista):
    for i in lista:
        if(i.cd == cd):
            return i
    return False
def validarCadastro(cd, lista):
    for i in lista:
        if(i.cd == cd):
            return False
    if(cd < 0):
        return False
while(True):
    opcao = int(input("Digite a opção desejada:\n"
                      "1 - Cadastrar Vendedores\n"
                      "2 - Cadastrar Produtos\n"
                      "3 - Vender Produtos\n"
                      "4 - Listar Produtos vendidos por Vendedor\n"
                      "5 - Sair\n"))
    if(opcao == 1):
        if(len(vendedores) > 0):
            print("Você ja cadastrou os vendedores. Voltando para o menu...")
            continue
        cont = 0
        while (cont < 5):
            cd = int(input(f"({cont + 1}) - Digite o codigo do Vendedor:"))
            if(validarCadastro(cd, vendedores) == False):
                print("O codigo já está cadastrado ou é menor que 0. Tente novamente.")
                continue
            nome = input(f"({cont + 1}) - Digite o nome do vendedor:")
            vendedor = Vendedor(cd, nome)
            vendedores.append(vendedor)
            cont+=1
    elif(opcao == 2):
        if(len(produtos) > 0):
            print("Você ja cadastrou os produtos. Voltando para o menu...")
            continue
        cont = 0
        while (cont < 10):
            cd = int(input(f"({cont + 1}) - Digite o codigo do Produto:"))
            if(validarCadastro(cd, produtos) == False):
                print("O codigo já está cadastrado ou é menor que 0. Tente novamente.")
                continue
            desc = input(f"({cont + 1}) - Digite a descrição do produto:")
            vlUnitario = float(input(f"({cont + 1}) - Digite o valor unitario do produto:"))
            while(vlUnitario < 0):
                print("O valor unitario não pode ser negativo. Tente novamente")
                vlUnitario = float(input(f"({cont + 1}) - Digite o valor unitario do produto:"))
            produto = Produto(cd, desc, vlUnitario)
            produtos.append(produto)
            cont+=1
    elif(opcao == 3):
        if(len(vendedores) == 0 or len(produtos) == 0):
            print("Você não cadastrou os vendedores ou os produtos. Voltando para o menu...")
            continue
        cdProduto = int(input("Digite o codigo do PRODUTO que deseja vender:"))
        while(pegarPorCodigo(cdProduto, produtos) == False):
            cdProduto = int(input("Codigo não encontrado! Tente Novamente.\nDigite o codigo do PRODUTO que deseja vender:"))
        produtoASerVendido = pegarPorCodigo(cdProduto, produtos)
        descProduto = produtoASerVendido.desc
        vlUnitario = produtoASerVendido.vlUnitario
        quantVendida = int(input("Digite a quantidade a ser vendida:"))
        while(quantVendida < 0):
            quantVendida = int(input("A quantidade a ser vendida não pode ser menor que 0! Tente Novamente.\nDigite a quantidade a ser vendida:"))
        cdVendedor = int(input("Digite o codigo do vendedor:"))
        while (pegarPorCodigo(cdVendedor, vendedores) == False):
            cdVendedor = int(input("Codigo não encontrado! Tente Novamente.\nDigite o codigo do VENDEDOR:"))
        vendedorDoProduto = pegarPorCodigo(cdVendedor, vendedores)
        nomeVendedor = vendedorDoProduto.nome
        atualizouVenda = False
        for i in vendas:
            if(cdProduto == i.cdProduto and cdVendedor == i.cdVendedor):
                i.quantVendida+=quantVendida
                atualizouVenda = True
        if(atualizouVenda == False):
            venda = Venda(cdVendedor, nomeVendedor, cdProduto, descProduto, quantVendida, vlUnitario)
            vendas.append(venda)
    elif(opcao == 5):
        print("Programa finalizado!")
        break