print('GymRat')

print('1. Cadastro de Alunos')
print('2. Listar Alunos')
print('3. Ativar Aluno')
print('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção: ') )
print('você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar Aluno')
elif opcao_escolhida == 2:
    print('Listar Aluno')
elif opcao_escolhida ==3:
    print('Ativar/desativar Aluno')
else:
    print('Saindo da apicação')
