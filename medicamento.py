remedio = []
def cadrastro_remedios():

 print("\ncadrastro de remedios")
     
codigo = input("digite o codigo do remedio: ")
nome = input("digite o nome do remedio: ")
forma_farmaceutica = input("digite a forma farmaceutica: ")
preço = input("digite o preço")
    
novo_remedio = {
        "codigo": codigo,
        "nome": nome,
        "forma_farmaceutica": forma_farmaceutica,
        "preço": preço,
    }
remedios.append(novo_remedio)

print("novo remedio cadastrado")


def menu_principal():
    progrma_rodando = True
    
    white progrma_rodando:
   
    print("1-cadrasto de remedio")
   
    print("2-lista de medicamentos")
    
    print("3-busca")
    
    opcao = input("escolha uma opção")
    progrma_rodando = False
    if opcao == "1":
     cadrastro_remedios()

    elif opcao == "2":
    
    elif opcao == "3"
    