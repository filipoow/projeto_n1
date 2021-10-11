from time import sleep


print("-=" *30)
sleep(2)
print('Bem-vindo ao sistema de cadastro, desenvolvido pelos alunos: ')
print("-=" *30)
# Funções
def projeton1():
    print("-=" *30)
    user = input("Digite seu login de administrador: ")
    password = input("Digite sua senha: ")
    if user and password == "AaDdMm":
        sleep(2)
        print("Entrando no sistema...")
    
    
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

cadastroUsuarios = []

while True:
    cadastroUsuarios.append(input("Digite o nome completo do usuário: "))
    cadastroUsuarios.append(input("Digite o e-mail do usuário: "))
    continuar = input("Deseja continuar cadastrando mais usuários? S/N: ")
    while continuar not in 'SsNn':
        continuar = input('Resposta inválida, deseja continuar? S/N: ')
    if continuar in 'Nn':
        break

projeton1()
usuariosCadastrados()
usuariosPorOrdemAlfabetica()
print("-=" *30)
buscandoUsuario(input("Digite o nome que você deseja encontrar na lista: "))
