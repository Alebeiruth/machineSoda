from source import encontrar_produto, trocados, atualizar_estoque, exibir_menu, verificacao_codigo, calcular_troco, modo_administrador

if __name__ == "__main__":
    # seleção dos produtos
    produtos = [[1, "Coca-Cola", 3.75, 2],
                [2, "Pepsi", 3.67, 5],
                [3, "Monster", 9.96, 1],
                [4, "Café", 1.25, 100],
                [5, "Redbull", 13.99, 2]]

    # estoque de notas e moedas
    estoque_notas_moedas = {
        1: 10, 0.50: 10, 0.25: 10, 0.10: 10, 0.05: 10, 0.01: 10
    }

    # chamadas das funções
    while True:
        print("\nMenu Principal")
        print("1. Comprar produto")
        print("2. Modo Administrador")
        print("3. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            exibir_menu(produtos)
            cliente = int(input("Entre com o código do produto: "))

            validacao = verificacao_codigo(cliente, produtos)
            print(validacao)

            if "Código correto" in validacao:
                produto_escolhido = encontrar_produto(cliente, produtos)
                print(f"Você escolheu {produto_escolhido[1]}, que custa R$ {produto_escolhido[2]:.2f}")
                valor_a_pagar = produto_escolhido[2]

                while True:
                    valor_pago = float(input("Entre com o valor pago pelo cliente R$: ").replace(',', '.'))
                    if valor_pago >= valor_a_pagar:
                        break
                    else:
                        print("Valor pago é menor que o preço do produto. Tente novamente.")

                troco_valor = valor_pago - valor_a_pagar
                troco_notas_moedas = calcular_troco(troco_valor, estoque_notas_moedas)

                if troco_notas_moedas:
                    print(trocados(valor_a_pagar, valor_pago))
                    print("Troco a ser devolvido:")
                    for quantidade, valor in troco_notas_moedas:
                        if valor >= 1:
                            print(f"{quantidade} nota(s) de R$ {valor:.2f}")
                        else:
                            print(f"{quantidade} moeda(s) de R$ {valor:.2f}")
                    atualizar_estoque(produto_escolhido)
                else:
                    print("Não há troco suficiente disponível. Compra cancelada.")
            else:
                print("Operação encerrada devido a código incorreto ou produto fora de estoque")
        elif escolha == 2:
            modo_administrador(produtos)
        elif escolha == 3:
            print("Obrigado(a) pela preferência, até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")
