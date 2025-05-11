import os

restaurantes = [{'nome':'Açaí do japa', 'categoria':'gelados', 'ativo':False}, 
                {'nome':'Pizzaiolo maluco', 'categoria':'Pizza', 'ativo':True},
                {'nome':'rei do camarao', 'categoria':'frutos do mar', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair do app\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')
    exit()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '~' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        status = 'Ativo' if ativo else 'Inativo'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}')

def alterar_status_restaurante():
    exibir_subtitulo('Alterar status do restaurante')
    listar_restaurantes()
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_do_restaurante.lower():
            novo_status = input('Deseja ativar ou desativar o restaurante? (a/d): ').lower()
            if novo_status == 'a':
                restaurante['ativo'] = True
                print(f'O restaurante {nome_do_restaurante} foi ativado com sucesso!')
            elif novo_status == 'd':
                restaurante['ativo'] = False
                print(f'O restaurante {nome_do_restaurante} foi desativado ')
            else:
                print('Opção inválida para status!')
            break
    else:
        print(f'Não foi encontrado nenhum restaurante com o nome {nome_do_restaurante}.')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
            voltar_ao_menu_principal()
        elif opcao_escolhida == 3: 
            alterar_status_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
