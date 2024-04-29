from functions import *
from random import randrange
from pousada import Pousada
from quarto import Quarto
import csv
     
def deserializar(nome_de_arquivo:str) -> list:
    # retorna uma matriz (lista de listas). cada elemento é uma linha do arquivo lido;
    # estando o arquivo está no formato CSV, as linhas serão interpretadas como listas de elementos separados por vírgula;
    # a primeira linha é desprezada usando o método next(), pois contém apenas o cabeçalho com os rótulos informativos;
    with open(nome_de_arquivo, 'r', encoding='utf-8') as arquivo:
        next(arquivo)
        lista_das_linhas = list(csv.reader(arquivo))
    return lista_das_linhas

def carrega_pousada(pousada:Pousada, lista_das_linhas:list) -> None:
    for i in range(len(lista_das_linhas)):
        # só pode haver uma pousada; assim, não há risco de sobreescrever
        pousada.nome = str(lista_das_linhas[i][0])
        pousada.contato = str(lista_das_linhas[i][1])
        pousada.quartos = []
        pousada.reservas = []
        pousada.produtos = []
     #   print(f'{pousada.nome}\t{pousada.contato}\t{pousada.quartos}\t{pousada.reservas}\t{pousada.produtos}\t')

def carrega_quartos(pousada:Pousada, lista_das_linhas:list) -> None:
    numero_de_quartos: int = len(lista_das_linhas)
    
    for i in range(numero_de_quartos):
        pousada.quartos.append([]) # cria uma lista vazia para cada quarto, a ser preenchida a seguir
        for dados in lista_das_linhas[i]: # são 4 dados no caso dos QUARTOS, por definição (int, str, float, list)
            pousada.quartos[i].append(dados)
            
    #for i in range(numero_de_quartos):
     #   print(f'{pousada.quartos[i][0]}\t{pousada.quartos[i][1]}\t{pousada.quartos[i][2]}\t{pousada.quartos[i][3]}')
        
def carrega_reservas(pousada:Pousada, lista_das_linhas:list) -> None:
    numero_de_reservas: int = len(lista_das_linhas)
    
    for i in range(numero_de_reservas):
        pousada.reservas.append([]) # cria uma lista vazia para cada reserva, a ser preenchida a seguir
        for dados in lista_das_linhas[i]: # são 5 dados no caso das RESERVAS, por definição
            pousada.reservas[i].append(dados)
            
    for i in range(numero_de_reservas):
        print(f'{pousada.reservas[i][0]}\t{pousada.reservas[i][1]}\t{pousada.reservas[i][2]}\t{pousada.reservas[i][3]}\t{pousada.reservas[i][4]}')

def carrega_produtos(pousada:Pousada, lista_das_linhas:list) -> None:
    pass

def main():
    minha_pousada = Pousada('','',[],[],[])
    
    clear_screen()
    carrega_pousada(minha_pousada, deserializar('pousada.txt'))
    carrega_quartos(minha_pousada, deserializar('quarto.txt'))
    carrega_reservas(minha_pousada, deserializar('reserva.txt'))
    carrega_produtos(minha_pousada, deserializar('produto.txt'))

    
    
    while True:
        clear_screen()
        minha_pousada.mostra_menu_principal()
        user_input = validador_input_numeros()
        match user_input:
            case '1':
                clear_screen()
                minha_pousada.consulta_disponibilidade()
            case '2':
                clear_screen()
                minha_pousada.consulta_reserva()
            case '3':
                clear_screen()
                minha_pousada.realiza_reserva()
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
                clear_screen()
                print('Até logo!')
                return True
            case '10':
                clear_screen()
                carrega_pousada(minha_pousada, deserializar('pousada.txt'))
                carrega_quartos(minha_pousada, deserializar('quarto.txt'))
                carrega_reservas(minha_pousada, deserializar('reserva.txt'))
                carrega_produtos(minha_pousada, deserializar('produto.txt'))
                #minha_pousada.consulta_disponibilidade()
                #minha_pousada.consulta_reserva()
                minha_pousada.realiza_reserva()
            case _:
                print('Opção inexistente. Tente novamente...')
main()