remedios = []


def cadastro_remedios():
    print("===CADASTRO DE REMÉDIO===")

    nome = input("Digite o nome do remédio: ")
    codigo = input("Digite o código do remédio: ")
    forma_farmaceutica = input("Digite a forma farmacêutica: ")
    preco = input("Digite o preço: ")

    novo_remedio = {
        "codigo": codigo,
        "nome": nome,
        "form_farmaceutica": forma_farmaceutica,
        "preco": preco
    }

    remedios.append(novo_remedio)

    print("Remédio cadastrado com sucesso!")


def busca_medicamentos():
    print("===BUSCA DE REMÉDIO===")

    if len(remedios) == 0:
        print("Nenhum remédio cadastrado.")
        return

    termo_busca = input("Digite o código do remédio: ")

    encontrado = False

    for remedio in remedios:
        if termo_busca.lower() == remedio["codigo"].lower():
            print("Remédio encontrado!")
            print(f"Nome: {remedio['nome']}")
            print(f"Código: {remedio['codigo']}")
            print(f"Forma farmacêutica: {remedio['form_farmaceutica']}")
            print(f"Preço: R$ {remedio['preco']}")

            encontrado = True

    if encontrado == False:
        print("Remédio não encontrado.")


def lista_medicamentos():
    print("===LISTA DE MEDICAMENTOS===")

    if len(remedios) == 0:
        print("Nenhum remédio cadastrado.")
        return

    for indice, remedio in enumerate(remedios, start=1):
        print(f"Remédio {indice}")
        print(f"Nome: {remedio['nome']}")
        print(f"Código: {remedio['codigo']}")
        print(f"Forma farmacêutica: {remedio['form_farmaceutica']}")
        print(f"Preço: R$ {remedio['preco']}")


def menu_principal():
    programa_rodando = True

    while programa_rodando:

        print("===MENU PRINCIPAL===")
        print("1 - Cadastro de remédio")
        print("2 - Lista de medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_remedios()

        elif opcao == "2":
            lista_medicamentos()

        elif opcao == "3":
            busca_medicamentos()

        elif opcao == "4":
            print("Fim do programa. Valeu!")
            programa_rodando = False

        else:
            print("Opção inválida.")


menu_principal()
