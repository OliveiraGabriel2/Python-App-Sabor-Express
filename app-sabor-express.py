import os


restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Sushi Japa Chan', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'bristo', 'categoria': 'Francêsa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True}]


def exibir_nome_do_programa():
    ''' Essa função serve para exibir o nome do programa '''
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')


def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair \n')


def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal  '''
    input('\nDigite uma tecla para voltar para o menu principal: ')
    main()


def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal'''
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar para o menu: ')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Lista os restaurantes presentes na lista'''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status do restaurante'}')
    # para cada restaurante na lista em restaurantes exibi o nome
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')  
    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    '''Altera o estado ativo/desativado de um restaurante'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']  # muda o valor
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)


    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    voltar_ao_menu_principal()


def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))


        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif (opcao_escolhida == 2):
            listar_restaurantes()
        elif (opcao_escolhida == 3):
            alternar_estado_do_restaurante()
        elif (opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()