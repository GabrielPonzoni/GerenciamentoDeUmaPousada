from functions import *
from random import randrange
from pousada import Pousada
from quarto import Quarto
from reserva import Reserva
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
    for linha in lista_das_linhas:      # varre cada linha da lista de linhas; cada linha possui os atributos dum QUARTO
        pousada.quartos.append(Quarto(int(linha[0]), linha[1], float(linha[2]), linha[3]))
                                        # com isso, geramos instâncias da classe Quarto (objetos 'Quarto')            
    
    # verificando abaixo de que os quartos foram corretamente importados (deletar quando não precisar mais)
    '''for quarto in pousada.quartos:
        print(f'{quarto.numero} = {quarto}')
    press_enter()'''
        
def carrega_reservas(pousada:Pousada, lista_das_linhas:list) -> None:
    for linha in lista_das_linhas:      # varre cada linha da lista de linhas; cada linha possui os atributos duma RESERVA
        pousada.reservas.append(Reserva(int(linha[0]), int(linha[1]), linha[2], linha[3], linha[4]))
                                        # com isso, geramos instâncias da classe Reserva (objetos 'Reserva')
    # ATENÇÃO: linha[3] não é um objeto da classe Quarto, como solicitado pela classe Reserva.
    # Para resolver isso, usar o valor de linha[3] recém importado (uma string) para localizar
    # o respectivo quarto em pousada.quartos e usar o objeto Quarto no seu lugar:
    for reserva in pousada.reservas:
        for quarto in pousada.quartos:
            if (int(quarto.numero) == int(reserva.quarto)):
                reserva.quarto = quarto     # atribui a reserva.quarto um objeto Quarto
                break
            
    # verificando abaixo de que os quartos foram corretamente importados (deletar quando não precisar mais)
    for reserva in pousada.reservas:
        print(f'{reserva.quarto.numero}')
    press_enter()
    
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
            case _:
                print('Opção inexistente. Tente novamente...')
main()