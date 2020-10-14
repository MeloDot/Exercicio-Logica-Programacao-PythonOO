from Classes import Vendedor
from Classes import Produto
from Classes import Venda

vendedores = []
produtos = []
vendas = []

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
    elif(opcao == 5):
        print("Programa finalizado!")
        break


