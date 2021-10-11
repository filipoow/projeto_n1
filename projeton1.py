from time import sleep


print("-=" *30)
sleep(2)
print('Bem-vindo ao sistema de cadastro, desenvolvido pelos alunos: ')

#Sistema de login
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

def projeton1():
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

# Programa principal

if ver == True:
    cadastroUsuarios = []

    while True:
        cadastroUsuarios.append(input("Digite o nome completo do usuário: "))
        cadastroUsuarios.append(input("Digite o e-mail do usuário: "))
        continuar = input("Deseja continuar cadastrando mais usuários? S/N: ")
        while continuar not in 'SsNn':
            continuar = input('Resposta inválida, deseja continuar? S/N: ')
        if continuar in 'Nn':
            break
    usuariosCadastrados()
    usuariosPorOrdemAlfabetica()
    print("-=" *30)
    buscandoUsuario(input("Digite o nome que você deseja encontrar na lista: "))
else:
    projeton1()





