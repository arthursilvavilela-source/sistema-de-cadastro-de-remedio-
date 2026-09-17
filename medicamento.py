remedio = []
def cadrastro_remedios():

 print("\ncadrastro de remedios")
     
nome = input("digite o nome do remedio: ")
codigo = input("digite o codigo do remedio: ")
forma_farmaceutica = input("digite a forma farmaceutica: ")
preço = input("digite o preço")
    
novo_remedio = {
        "codigo": codigo,
        "nome": nome,
        "form_farmaceutica": forma_farmaceutica,
        "preço": preço,
    }
remedio.append(novo_remedio)

print("novo remedio cadastrado")



def lista_medicamentos():
    print("lista de livros")
if len == 0:
    print("nem um remedio no estoque")
    
    
    termo_busca = input("digite o codigo do remedio: ")
    encontrado = False
    
    for remedios in remedio:
        if termo_busca in remedio ["codigo"]. lower():
            print("Remedio encontrado")
            print(f"nome: {nome['nome']}")
            print(f"codigo: {codigo ['codigo']}")
            print(f"form_farmaceutica: {forma_farmaceutica ['form_farmaceutica']}")
            print(f"preço: {preço ['preço']}")
            
            
        
    
    
    

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
    