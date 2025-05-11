print('Python na Escola de Programação da Alura.')
nome = input('digite seu nome ')
idade = input('sua idade ')
print ( f'seu nome é {nome} e vc tem {idade} anos')
print ('''
A
L
U
R
A
''')

numero = int(input('escolha um numero '))

if numero % 2 == 0 :
    print('o numero que voce escolheu é par')
else:
    print('o numero que voce escolheu é impar')

idade_2 = int(input('quantos anos voce tem?'))

if 12 >= idade_2 >= 1 :
    print(f'você é uma criança de {idade_2} anos')
elif 18>= idade_2 >=13 :
    print(f'você é um adolescente de {idade_2} anos')  
else :
    print(f'parabéns!!!você ja é um adulto de {idade_2} anos')

usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")
