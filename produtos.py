import operator

def cadastrarProd():
    print('')
    nome = input("Por favor entre com o nome do produto: ")
    desc = input("Por favor entre com a descrição do produto: ")
    while True:
        try: #Garante que o valor inserido no preço será um número
            val = float(input("Diga o preço do produto: "))
            break
        except ValueError: #Caso não seja inserido um numéro o erro será mostrado
            print("Valor inválido digitado para o tipo de consulta")
            continue
    venda_aux  = input("O produto está a venda? ")
    if(venda_aux == "Sim" or venda_aux == "sim" or venda_aux == "SIM")
        venda = 'Sim'
    elif (venda_aux == "Não" or venda_aux == "não" or venda_aux == "Não" or venda_aux == "NAO" or venda_aux == "Nao" or venda_aux == "nao"):
        venda = 'Não'
    else:
        print("Código não reconhecido.")
    
    dicionario = {'Nome': nome, 'Descricção': desc, 'Preço': val, 'Vendendo': venda} #Cria um dicionário que irá guardar todas as informações do produto
    return dicionario #Retorna o dicionario para o main

def listarcadastro(produtos):
    print('')
    novalista = []
    novalista = sorted(produtos, key=operator.itemgetter('Preço'))
    print("Nome   |   Valor   |   A venda")
    for d in novalista:
        print (d['Nome'], '|', d['Preço'], '|', d['Vendendo'])

def listar(produtos):
    print('')
    while True:
        print("Escolha a opção de consulta desejada\n1-Consultar todos os produtos\n2-Consultar apenas produtos a venda\n3-Retornar")
        try: #Garante que a opção de consulta será um número 
            opcao = int(input("Diga o que deseja fazer: "))
            break
        except ValueError: #Caso não seja inserido um número o erro será mostrado
            print("Valor inválido digitado para o tipo de consulta")
            continue

    if opcao == 1:
        novalista = []
        novalista = sorted(produtos, key=operator.itemgetter('Preço'))
        print("Nome   |   Valor   |   A venda")
        for d in novalista:
            print (d['Nome'], '|', d['Preço'], '|', d['Vendendo'])
    elif opcao == 2:
        novalista = []
        novalista = sorted(produtos, key=operator.itemgetter('Preço'))
        print("Nome   |   Valor")
        for d in novalista:
            if(d['Vendendo'] == 'Sim'):
                print (d['Nome'], '|', d['Preço'])
    elif opcao == 3:
        print("Retornando.")
    else:
        print("Opcao invalida.")

#main
produtos = []
em = int(0)
while em != 3: #Inicia loop para checagem caso seja escolhida opção do fim do menu
    print("\nEssas são as opções do menu\n1-Cadastrar produto\n2-Consultar produtos\n3-Encerrar programa")
    try:
        em = int(input("Diga a sua escolha do menu: "))
    except ValueError:
        print("Entrada inválida, tente valor numérico.")
        continue
    if em == 1:
        pd = cadastrarProd()
        produtos.append(pd) #Adiciona na lista de produtos o produto recem cadastrado
        listarcadastro(produtos)
    elif em == 2:
        listar(produtos)
    elif em == 3:
        exit()
    else:
        print("Opção não existente no menu.")