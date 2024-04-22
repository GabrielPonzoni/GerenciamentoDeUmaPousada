from functions import *
from random import randrange
from pousada import Pousada

# inicializa uma tabela de dias e disponibilidades aleatoriamente;
# a disponibilidade é um booleano
# talvez seja interessante criar uma classe para essa tabela
# ao invés de deixá-la solta no programa.
datas_disponiveis: list = [[] for i in range(31)]
for row in datas_disponiveis:
    row.append(None)
    row.append(None)

for i in range(31):
    datas_disponiveis[i][0] = i+1
    if randrange(2) == 0:
        datas_disponiveis[i][1] = True
    else:
        datas_disponiveis[i][1] = False

##################################################################
##################################################################

def menu_principal() -> None:
    print('BEM-VINDO AO RECANTO DO SOSSEGO!')
    print('================================')
    print('Digite a opção desejada.\n')
    print('1.  Consultar disponibilidade') 
    print('2.  Consultar reserva')
    print('3.  Realizar reserva')
    print('4.  Cancelar reserva')
    print('5.  Realizar check-in')
    print('6.  Realizar check-out')
    print('7.  Registrar consumo')
    print('8.  Salvar')
    print('9.  Sair')

def consulta_disponibilidade() -> None:
    print('DATAS DISPONÍVEIS P/ MAIO')
    print('=========================')
    mostra_disponibilidade()
    input('(Pressione Enter)')

def mostra_disponibilidade():
    for dia in range(31):
        print(f'{datas_disponiveis[dia][0]}\t\t{converte_bool_em_str(datas_disponiveis[dia][1])}')

def realiza_reserva():
    # mostra o calendário e permite usuário fazer reservas;
    # uma vez satisfeito, mostra as reservas do usuário

    mostra_disponibilidade()
    print('Escolha o dia que deseja reservar:')
    user_input = validador_input_numeros()
    
    if (datas_disponiveis[int(user_input) - 1][1] == False):
        print('Este dia já está reservado. Escolha outro dia.')
        user_input = validador_input_numeros()
    else:
        print(f'Você reservou o dia {datas_disponiveis[int(user_input) -1][0]}.')
        datas_disponiveis[int(user_input) - 1][1] = False

        print('Deseja reservar outro dia? (S/N)')
        user_input = validador_input_s_n()
        if (user_input == 's'):        # user_input já foi covertido para letras minúsculas no validador.
            realiza_reserva()
        else:
            consulta_reserva()
            main()

def consulta_reserva():
    pass

def main():
    clear_screen()
    menu_principal()
    user_input = validador_input_numeros()

    match user_input:
        case '1':
            clear_screen()
            consulta_disponibilidade()
            main()                      # usando aqui recursividade
        case '2':
            clear_screen()
            consulta_reserva()
        case '3':
            clear_screen()
            realiza_reserva()
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            pass
        case '9':
            print('Até logo!')
        case _:
            print('Opção inexistente. Saindo do programa...')
main()