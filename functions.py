# arquivo com banco de funções de utilidade geral
import os

def clear_screen() -> None:
    os.system('cls')

def validador_input_s_n() -> str:
    # verifica se o usuário entoru com 's' ou 'n'

    user_input: str = input()
    validador: bool = False

    while(validador == False):
        if (user_input == '') or (user_input == None):
            print(f'Digite S ou N.')
            user_input = input()
        elif (user_input.lower() != 's') and (user_input.lower() != 'n'):
            print(f'Opção inválida. Digite S ou N.')
            user_input = input()
        else:
            validador = True
    return user_input.lower()

def validador_input_numeros() -> str:
    # verifica se o usuário entrou com um número inteiro;
    # seria bom estabelecer um limite de números possíveis

    user_input: str  = input()
    validador: bool = False

    while(validador == False):
        if (user_input == '') or (user_input == None):
            user_input = input('Digite uma opção numérica.\n')
        else:
            try:
                if isinstance(int(user_input), int) == True:
                    validador = True
            except ValueError:
                user_input = input('Digite apenas numéros.\n')
    return user_input

def converte_bool_em_str(x: bool) -> str:
    # converte um booleano em algo legível para o usuário
    if (x == True):
        return 'disponível'
    else:
        return 'ocupado'
        