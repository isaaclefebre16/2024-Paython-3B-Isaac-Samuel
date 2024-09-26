import os

aluno = [{'nome': 'Fernando', 'categoria': 'masculino', 'ativo':True},
         {'nome': 'Kaua', 'categoria': 'masculino', 'ativo':True},
         {'nome': 'Talita', 'categoria': 'femenino', 'ativo':True},
         {'nome': 'Hellen', 'categoria': 'femenino', 'ativo':True}]

def cadastrar_alunos():
    exibir_subtitulo()
    
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
        opcao_escolhida = int(input('Escolha uma opção: ') )
        print('você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            print('Cadastrar Aluno')
        elif opcao_escolhida == 2:
            print('Listar Aluno')
        elif opcao_escolhida == 3:
            print('Ativar/desativar Aluno')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()

except:
    opcao_invalida()

def cadastrar_alunos():
    os.system('cls')
    print('cadastrando aluno... ')
    nome_nadador = input('Digite o nome do aluno: ')
    alunos.append(nome_aluno)
    print(f'(nome_aluno) foi adicionado(a) aos alunos de Foz do Iguaçu')
    input('Digite qualquer tecla para voltar')
    main()


def main():
    mostra_titulo()
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()