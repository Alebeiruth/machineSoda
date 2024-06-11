def main():
    pass

# função itera sobre matriz produtos, apresentando ID e o produto
def exibir_menu(produtos):
    print("Escolha seu produto abaixo:")
    for produto in produtos:
        print(f"{produto[0]} - {produto[1]}")

# função verifica se o código do produto é válido e se há estoque
def verificacao_codigo(cliente, produtos):
    produto = encontrar_produto(cliente, produtos)
    if produto is None:
        return "Código incorreto"
    elif produto[3] <= 0:
        return f"{produto[1]} está fora de estoque"
    else:
        return f"Código correto. {produto[1]} está disponível."

# função encontra o produto pelo código
def encontrar_produto(codigo, produtos):
    for produto in produtos:
        if produto[0] == codigo:
            return produto
    return None

# função que demostra o troco do cliente
def trocados(valor_a_pagar, valor_pago):
    return f"Seu troco é R$ {valor_pago - valor_a_pagar:.2f}"

# função que subtrai e atualiza ou não a quantidade de moedas
def calcular_troco(troco, estoque_notas_moedas):
    notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = []
    for valor in notas_moedas:
        quantidade = int(troco // valor)
        if quantidade > 0:
            if quantidade <= estoque_notas_moedas[valor]:
                resultado.append((quantidade, valor))
                troco = round(troco - quantidade * valor, 2)
            else:
                return None  # Não há notas/moedas suficientes no estoque
    if troco > 0:
        return None  # Não foi possível fornecer o troco exato
    else:
        return resultado

# função que atualiza o estoque ou falta do produto
def atualizar_estoque(produto):
    if produto[3] > 0:
        produto[3] -= 1
        print(f"Estoque atualizado. Restam {produto[3]} unidades de {produto[1]}.")
    else:
        print(f"{produto[1]} está fora de estoque.")

# função criadas para erros de digitação de numero inteiros
def input_int(mensagem):
    while True:
        try:
            valor = int(float(input(mensagem).replace(',', '.')))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# função criadas para erros de digitação de numero fluantes
def input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# função que cradastra novos produtos
def cadastrar_produto(produtos):
    id_novo = len(produtos) + 1
    nome = input("Digite o nome do produto: ")
    preco = input_float("Digite o preço do produto: ")

    while True:
        estoque = input_int("Digite a quantidade em estoque (maior ou igual a 1): ")
        if estoque >= 1:
            break
        else:
            print("A quantidade em estoque deve ser maior que 1. Tente novamente.")

    produtos.append([id_novo, nome, preco, estoque])
    print(f"Produto {nome} cadastrado com sucesso!")

# função que edita de novos e antigos produtos
def editar_produto(produtos):
    id_produto = input_int("Digite o ID do produto a ser editado: ")
    produto = encontrar_produto(id_produto, produtos)
    if produto:
        nome = input(f"Digite o novo nome do produto (atual: {produto[1]}): ")
        preco = input_float(f"Digite o novo preço do produto (atual: R$ {produto[2]:.2f}): ")
        estoque = input_int(f"Digite a nova quantidade em estoque (atual: {produto[3]}): ")
        produto[1] = nome
        produto[2] = preco
        produto[3] = estoque
        print(f"Produto {nome} editado com sucesso!")
    else:
        print("Produto não encontrado.")

# função que remove os produtos
def remover_produto(produtos):
    id_produto = input_int("Digite o ID do produto a ser removido: ")
    produto = encontrar_produto(id_produto, produtos)
    if produto:
        produtos.remove(produto)
        print(f"Produto {produto[1]} removido com sucesso!")
    else:
        print("Produto não encontrado.")

# função menu que demostra o usuario as opções existentes
def modo_administrador(produtos):
    while True:
        print("\nModo Administrador")
        print("1. Cadastrar produto")
        print("2. Editar produto")
        print("3. Remover produto")
        print("4. Sair do modo administrador")
        escolha = input_int("Escolha uma opção: ")
        if escolha == 1:
            cadastrar_produto(produtos)
        elif escolha == 2:
            editar_produto(produtos)
        elif escolha == 3:
            remover_produto(produtos)
        elif escolha == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")
