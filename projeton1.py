from time import sleep

#Sistema de login
ver = False
while ver == False:
    print("-=" *30)
    office = input("Digite seu cargo: ")
    user = input("Digite seu login: ")
    password = input("Digite sua senha: ")

   
    if office == "Gestor":
        if user and password == "Adm":
            sleep(2)
            print("Entrando no sistema...")
            print("-=" *30)
            ver = True
    else:
        print("-=" *30)
        print("Seu usuário não tem acesso as funções de gestor.")
        ver = False

# Funções

    print("-=" *30)
    office = input("Digite seu cargo: ")
    user = input("Digite seu login: ")
    password = input("Digite sua senha: ")
    if office == "Gestor":
        if user and password == "Adm":
            sleep(2)
            print("Entrando no sistema...")
    else:
        print("-=" *30)
        print("Seu usuário não tem acesso as funções de gestor.")
    
def usuariosCadastrados():
    print("-=" *30)
    print("Os usuários cadastrados são: ")
    sleep(0.5)
    print(cadastroUsuarios)

def usuariosPorOrdemAlfabetica():
    print("-=" *30)
    print("Os usuários em ordem alfabética são: ")
    sleep(0.5)
    cadastroUsuarios.sort()
    for usuariosAlfabetico in cadastroUsuarios:
        print(usuariosAlfabetico)

def buscandoUsuario(nome):
    print("-=" *30)
    print("Buscando um usuário pelo seu nome...")
    sleep(1)
    if nome in cadastroUsuarios:
        print(f"Foi encontrado na lista o nome {nome}")
    else:
        print(f"Não foi encontrado na lista o nome {nome}")

def removerUsuario(nome):
    print("-=" *30)
    print("Buscando um usuário pelo seu email...")
    sleep(1)
    if nome in cadastroUsuarios:
        cadastroUsuarios.remove(nome)
        print(f"Foi encontrado o email: {nome} e foi deletado.")
    else:
        print(f"Não foi encontrado na lista o email {nome}")

def alterarusúario(nome):
    print("-=" *30)
    print("buscando um usúario pelo nome:...")
    sleep(1)
    if nome in cadastroUsuarios:
        cadastroUsuarios.remove(nome)      
    
# Programa principal
cadastroUsuarios = []

def menu(): 
    i = 0
    while i < 100:
        i = i + 1
        if ver == True:
            sleep(2)
            print("Bem-vindo ao sistema de cadastro")
            print("1 - Cadastro de Usuário")
            print("2 - Mostrar usuários cadastrados")
            print("3 - Usuários cadastrados por ordem alfabética")
            print("4 - Buscando usuário na lista")
            print("5 - Remover usuário da lista")
            print("6 - Alterar nome do usuário")
            print("7 - Sair do sistema")
            print("-=" *30)
            op = int(input("Digite o número da operação: "))

            if op == 1:
                while True:
                    cadastroUsuarios.append(input("Digite o nome completo do usuário: "))
                    cadastroUsuarios.append(input("Digite o e-mail do usuário: "))
                    continuar = input("Deseja continuar cadastrando mais usuários? S/N: ")
                    while continuar not in 'SsNn':
                        continuar = input('Resposta inválida, deseja continuar? S/N: ')
                    if continuar in 'Nn':
                        break
            if op == 2:
                usuariosCadastrados()
            if op == 3:
                usuariosPorOrdemAlfabetica()
            if op == 4:
                print("-=" *30)
                buscandoUsuario(input("Digite o nome que você deseja encontrar na lista: "))
            if op == 5:
                removerUsuario(input("Digite o email do usuário que deseja remover: "))
            if op == 6:
                alterarusúario(input("Digite o e-mail do usúario que deseja alterar:"))
                nome=str(input("Digite o novo nome:"))
                cadastroUsuarios.append(nome)
            if op == 7:
                i = 100
menu()