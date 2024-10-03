import os

aluno = [{'nome': 'Fernando', 'categoria': 'masculino', 'ativo':True},
         {'nome': 'Kaua', 'categoria': 'masculino', 'ativo':True},
         {'nome': 'Talita', 'categoria': 'femenino', 'ativo':True},
         {'nome': 'Hellen', 'categoria': 'femenino', 'ativo':True}]

def exbir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()   
    
def mostra_titulo():
    print('''
          
    GymRat

    ''')

print('GymRat')

print('1. Cadastro de Alunos')
print('2. Listar Alunos')
print('3. Ativar Aluno')
print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_alunos()
        elif opcao_escolhida == 2:
            mostrar_alunos()
        elif opcao_escolhida == 3:
            print('Ativar/desativar aluno')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_alunos():
    exbir_subtitulo('Cadastrar alunos')

def cadastrar_alunos():
    os.system('cls')
    print('cadastrando aluno... ')
    nome_aluno = input('Digite o nome do aluno: ')
    alunos.append(nome_aluno)
    print(f'(nome_aluno) foi adicionado(a) aos alunos da academia GymRat')
    
    retorna_menu_principal()

def mostrar_alunos():
    exbir_subtitulo('Listar alunos')

    for aluno in alunos:
        nome_aluno = aluno['nome']
        categoria = aluno['categoria']
        ativo = aluno['ativo']
        print(f' - {nome_aluno} | {categoria} | {ativo}')
    
    retorna_menu_principal()

def alterar_estado_aluno():
    exbir_subtitulo('Cadastrar alunos')
    nome_aluno = input('Qual aluno(a) você gostaria de mudar o status?')
    aluno_encontrado = False

    for aluno in alunos:
        if nome_aluno == aluno['nome']
            aluno_encontrado = True
            aluno['ativo'] = not aluno['ativo']
            mensagem = f'O {nome_aluno} foi ativado com sucesso' if aluno['ativo'] else f' O(A) {nome_aluno} foi desativado'

            print(mensagem)
    if not aluno_encontrado:
        print('O aluno ou aluna não existe')

def finalizar_programa():
    os.system('cls')
    print('Finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()