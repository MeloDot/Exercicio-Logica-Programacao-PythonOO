# Exercicio-Logica-Programacao-PythonOO

1) Uma loja de artesanato possui 5 vendedores e comercializa 10 (dez) tipos de produtos. Os
vendedores recebem, mensalmente, salário fixo (líquido) de R$ 1585,00, acrescido de 5% do valor total
de suas vendas.
Crie um programa em Python que apresente o seguinte menu de opções:
1 - Cadastrar Vendedores
2 - Cadastrar Produtos
3 - Vender Produtos
4 - Listar Produtos vendidos por Vendedor
5 - Sair

Opção 1 - Cadastrar Vendedores
Receber do usuário o código e nome dos 5 (cinco) vendedores. Voltar para o Menu.
Importante:
- Não permitir: código de vendedor duplicado e código <=0.
- Após cadastrar não permitir entrar novamente nessa opção.

Opção 2 - Cadastrar Produtos
Receber do usuário o código, a descrição e o valor unitário dos 10 (dez) produtos. Voltar para o Menu.
Importante:
- Não permitir: código de produto duplicado.e código <=0.
- Após cadastrar não permitir entrar novamente nessa opção.

Opção 3 - Vender Produtos
Receber do usuário o código do produto que deseja vender, quantidade vendida e código do vendedor
que vendeu o produto. Voltar para o Menu.
Importante:
- Validar se o código do produto e o código do vendedor existem;
- Validar a quantidade vendida que precisa ser > 0;
- O usuário não pode acessar essa opção sem antes ter cadastrado os produtos e os vendedores.
Disciplina: Computational Thinking using Python
- O usuário poderá vender o mesmo produto em diferentes momentos.

Opção 5 – Sair
- Somente poderá sair do programa nessa opção.

Opção 4 - Listar produtos Vendidos por vendedor
- Ordem de Impressão: Código do vendedor + Código do produto. (1.0 ponto)
O relatório deve conter código de vendedor, nome do vendedor, código do produto,
descrição de produto, quantidade vendida, valor unitário e valor total de cada produto
(quantidade vendida * valor unitário).

Importante:
- No relatório, a quantidade vendida do produto precisa ser a quantidade total vendida pelo
vendedor do produto. Por exemplo: Se o vendedor vendeu 6 unidades do produto 100 (Produto
2) e depois vendeu 4 unidades do mesmo produto, no relatório deve aparecer Quantidade
Vendida = 10.
- Nem sempre o vendedor irá vender todos os produtos existentes no cadastro, portanto, deve
aparecer no relatório apenas os produtos vendidos pelo vendedor.
- O usuário somente pode acessar essa opção se tiver pelo menos um produto vendido.
Ao final, deverá mostrar o valor total das vendas e o valor da comissão que o vendedor irá
receber. Voltar para o Menu.

