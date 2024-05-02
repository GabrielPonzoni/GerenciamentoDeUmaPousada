from functions import *
from pousada import Pousada
from quarto import Quarto
from produto import Produto
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

def serializar(pousada:Pousada) -> None:   
    # Acessa arquivos da pousada informada;
    # (sobre)escreve o conteúdo dos arquivos com o conteúdo atualizado
    # das listas da pousada. Reaproveita a primeira linha (cabeçalho);
    # Escreve separadamente a última linha para não sobrar linha em branco
        
    # lista de reservas:
    with open('reserva.txt', 'r', encoding='utf-8') as arquivo:
        primeira_linha = arquivo.readline()

    with open('reserva.txt', 'w', encoding='utf-8', newline='') as arquivo:  # newline='' impede que haja linas em branco (chatgpt)
        arquivo.write(primeira_linha)     # escreve cabeçalho
        
        lista_de_listas: list = pousada.serializar_lista_de_reservas()
        for i in range(len(lista_de_listas) - 1):                              # índice não-inclusivo; sugestão do chatgpt: lista_de_linhas[:-1]
            arquivo.write(','.join(lista_de_listas[i]) + '\n')                 # escreve cada linhas com \n ao final, exceto a última
        arquivo.write(','.join(lista_de_listas[len(lista_de_listas) - 1]))     # escreve a última linha sem \n; índice inclusivo; sugestão do chatgpt: lista_de_linhas[-1]
        
    # lista de quartos:
    with open('quarto.txt', 'r', encoding='utf-8') as arquivo:
        primeira_linha = arquivo.readline()

    with open('quarto.txt', 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write(primeira_linha) 
        
        lista_de_listas: list = pousada.serializar_lista_de_quartos()
        for i in range(len(lista_de_listas) - 1):                   
            arquivo.write(','.join(lista_de_listas[i]) + '\n')      
        arquivo.write(','.join(lista_de_listas[len(lista_de_listas) - 1]))

def carrega_pousada(pousada:Pousada, lista_das_linhas:list) -> None:
    
    for i in range(len(lista_das_linhas)):
        # só pode haver uma pousada; assim, não há risco de sobreescrever; consulte arquivo pousada.txt
        pousada.nome = str(lista_das_linhas[i][0])
        pousada.contato = str(lista_das_linhas[i][1])
        pousada.quartos = []
        pousada.reservas = []
        pousada.produtos = []

def carrega_quartos(pousada:Pousada, lista_das_linhas:list) -> None:
    for linha in lista_das_linhas:      # varre cada linha da lista de linhas; cada linha possui os atributos dum QUARTO
        pousada.quartos.append(Quarto(int(linha[0]), linha[1], float(linha[2]), []))
                                        # com isso, geramos instâncias da classe Quarto (objetos 'Quarto')            
    
    # ATENÇÃO: linha[3] deve ser uma lista, mas quarto.txt pode ter um número arbitrário de elementos a partir de linha[3].
    # exemplo: 101,S,500.00,3,3,4,5,7,2
    # essa lista contém os códigos dos produtos (3,3,4,5,7,2), e esses dados devem ser organizados em uma lista.
    # para corrigir isso, é preciso um tratamento diferente.
    
    for i in range(len(lista_das_linhas)): # passa por todas as linhas / quartos 
        numero_de_elementos_de_codigo_de_produto: int = len(lista_das_linhas[i]) - 3   # no mínimo haverá 1, mesmo que seja = ''
        #pousada.quartos[i].consumo = []
        for j in range(3, len(lista_das_linhas[i])):   # verifica a partir do elemento 3
            if lista_das_linhas[i][j] == '':
                continue
            else:
                pousada.quartos[i].consumo.append(lista_das_linhas[i][j])
        
def carrega_reservas(pousada:Pousada, lista_das_linhas:list) -> None:
    for linha in lista_das_linhas:      # varre cada linha da lista de linhas; cada linha possui os atributos duma RESERVA
        pousada.reservas.append(Reserva(int(linha[0]), int(linha[1]), linha[2], linha[3], linha[4]))
                                        # com isso, geramos instâncias da classe Reserva (objetos 'Reserva')
    # ATENÇÃO: linha[3] não é um objeto da classe Quarto, como solicitado pela classe Reserva.
    # Para resolver isso, usar o valor de linha[3] recém importado (uma string) para localizar
    # o respectivo quarto em 'pousada.quartos' e atribuir o objeto Quarto no seu lugar:
    for reserva in pousada.reservas:
        for quarto in pousada.quartos:
            if (int(quarto.numero) == int(reserva.quarto)):
                reserva.quarto = quarto     # atribui a reserva.quarto um objeto Quarto
                break
    
def carrega_produtos(pousada:Pousada, lista_das_linhas:list) -> None:
    for linha in lista_das_linhas:
        pousada.produtos.append(Produto(int(linha[0]), linha[1], float(linha[2])))

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
                clear_screen()
                minha_pousada.cancela_reserva()
            case '5':
                clear_screen()
                minha_pousada.realiza_check_in()
            case '6':
                clear_screen()
                minha_pousada.realiza_check_out()
            case '7':
                clear_screen()
                minha_pousada.registra_consumo()
            case '8':
                clear_screen()
                print('Salvando alterações...')
                minha_pousada.limpar_reservas_c_o()
                serializar(minha_pousada)
                press_enter()
            case '9':
                clear_screen()
                print('Salvando alterações...')
                minha_pousada.limpar_reservas_c_o()
                serializar(minha_pousada)
                print('Até logo!')
                return True
            case _:
                print('Opção inexistente. Tente novamente...')
main()