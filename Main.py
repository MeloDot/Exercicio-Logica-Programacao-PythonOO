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
        cont = 0
        while cont < 5:
            cd = int(input(f"({cont + 1}) - Digite o codigo do Vendedor:"))
            if(validarCadastro(cd, vendedores) == False):
                print("O codigo já está cadastrado ou é menor que 0. Tente novamente.")
                continue
            nome = input("Digite o nome do vendedor:")
            vendedor = Vendedor(cd, nome)
            vendedores.append(vendedor)
            cont+=1
    elif(opcao == 5):
        print("Programa finalizado!")
        break


