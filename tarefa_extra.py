'''
Precisamos criar uma agenda para armazenar o nome e o telefone das pessoas.
Algoritmo:
1- Definir o dicionário para armazenar os dados
2- Inserir os dados no dicionário
    - digitar nome 
    - digitar telefone
    - guardar nome e telefone na agenda
3- Aleterar o telefone de alguém
    - ler um nome
    - localiza na agenda
    - le o novo número
4- Apagar o telefone de alguém
    - ler o nome
    - localizar na agenda
    - deletar da agenda
5- Imprimir a agenda
'''

agenda = {'ivonei':['1111'], 'maria':['2222'], 'pedro': ['3333'],'aaa':['999991111','999992222','999993333']}

def ler_telefone(telefones = []):
    def entrar_outro_numero():
        resposta = input('Entrar outro número? s/n: ')
        if resposta.upper() == 'S':
            return True
        return False
"""
Na função acima é criado a lista 'telefones', e pergunta se
o usuário quer adicionar outro numero de telefone, se a resposta
for sim ele executa o código abaixo:
"""
telefone = input('   Entre o Telefone: ')
if len(telefone) == 9:
        if telefone.isnumeric():
            telefones.append(telefone)
            if entrar_outro_numero():
                return ler_telefone(telefones)
            else: 
                return telefones
        else:
            input('   Número deve conter apenas dígitos numéricos. [Enter] ')
else:
        input('   Número deve ter 9 dígitos. [Enter] ')
return ler_telefone()

"""
No código acima pede-se para digitar o numero de telefone,
se houver 9 digitos, verifica se é numérico e adiciona o numero
em 'telefone', perguntar se deseja adicionar outro numero, se sim 
retorna para a função 'ler_telefone', se não, mostra os telefones.
Se não for numerico e nao tiver 9 digitos sai da função.
"""



def insere():
#    print('- - - Insere nome na Agenda - - -')
    print('Insere nome na Agenda'.center(35,'-'))

    while True:
        print('[Enter] finaliza o cadastro')
        nome = input('Nome: ')
        if nome: 
            if nome not in agenda:
                agenda[nome] = ler_telefone()
            else: input('   Nome Já cadastrado na Agenda. [Enter] ')
        else:
            break

"""
Na função acima pede-se para adicionar nome na agenda,
se o nome ainda nao estiver na agenda, executa 'ler_telefone'
caso ja tenha o nome na agenda aparece mensagem que já está cadastrado.
"""


def alterar_nome_telefone():
    resposta = input(''' 
            --------------------------
            O que você deseja alterar:
            --------------------------
            1 - Nome
            2 - Telefone
            Escolha: ''')
    if resposta not in ('1','2'):
        return alterar_nome_telefone
    return resposta

"""
Função para alterar o nome ou telefone
"""


def alterar_nome(nome):
    novo_nome = input('...[Enter] - Retorna\n...Digite o nome correto: ')
    if novo_nome:
        if novo_nome in agenda:
            input('...Este nome já consta na agenda! ')
        else:
            agenda[novo_nome] = agenda[nome]
            del(agenda[nome])

"""
Para alterar o nome, digitar o novo nome
se já estiver na agenda aparece mensagem que já consta na agenda
se não adiciona o novo nome na agenda
"""


def alterar_telefone(nome):
    print('...Escolha o telefone: ')
    telefones = agenda[nome]
    for ind,fone in enumerate(telefones):
        print(f'...{ind} - {fone}')
    escolha = int(input('   Escolha pelo indice: '))
    if escolha >= 0 and escolha <= len(telefones):
        telefones.pop(escolha)
        agenda[nome] = ler_telefone(telefones)
print(agenda)

"""
Para alterar o telefone, verifica o numero na agenda
escolhe o telefone pelo indice, se a escolha for maior ou igual a zero 
e a quantidade(telefones) executa a alteração abaixo
"""


def alterar():
    print('Altera Agenda'.center(35,'-'))
    while True:
        print('[Enter] finaliza a alteração')
        nome = input('Nome para alterar: ')  # se for digitado enter. o conteúdo é nulo
        if nome:  # nome é válido
            if nome in agenda: # nome está na agenda?
                if alterar_nome_telefone() == '1': # Alterar Nome
                    alterar_nome(nome)
                else: 
                    alterar_telefone(nome)
                print(agenda)
            else:
                input('Nome não consta na agenda. [Enter]')
        else:   # nome NÃO válido
            break





def excluir():
        print('Excluir'.center(35,'-'))
        nome = input('Nome para excluir: ')  
        if nome in agenda:
            confirma = input(f'...Confirma a exclusão {nome}? s/n: ')
            if confirma.upper() == 'S':
                del(agenda[nome])
                input('...Nome Excluido...[Enter]')
        else:
            input('Nome não consta na agenda. [Enter]')
        print(agenda)
"""
Na função acima, digitar o nome para excluir,
verifica se o nome consta na agenda, confirma a exclusão com sim ou não
se S, excluir o nome.
Se o nome nao consta na agenda, aparece mensagem e mostra agenda
"""

def menu():
    resposta = input('''

+---------------------------------+
| Menu Principal                  |
+---------------------------------+
| 0 - Finalizar                   |
| 1 - Inserir Dados na Agenda     |
| 2 - Alterar Telefone            |
| 3 - Excluir Pessoa na Agenda    |
| 4 - Mostrar Agenda              |
+---------------------------------+
Escolha: ''')

    if resposta in ('0','1','2','3','4'):
        return resposta
    input('Escolha incorreta. [Enter] - Tente Novamente.')
    return menu()



def imprime_agenda():
    print('Agenda'.center(35,'-'))
    for nome,fones in agenda.items():
        telefones = str(fones).strip("[]").replace("'","")
        print(f'  {nome.ljust(15,".")} - {telefones}')




#####################################
# Programa Principal
#     
while True:
    escolha = menu()
    if escolha   == '1':
        insere()
    elif escolha == '2':    
        alterar()
    elif escolha == '3':
        excluir()
    elif escolha == '4':
        imprime_agenda()
    else: break

print('Fim')
