from functions import *
from quarto import Quarto
from reserva import Reserva

class Pousada:
    
    def __init__(self, nome:str, contato:str, quartos:list, reservas:list, produtos:list):

        self.__nome = nome
        self.__contato = contato
        self.__quartos = quartos
        self.__reservas = reservas
        self.__produtos = produtos
        
        self.__clientes: list = []
        # precisa setter/getter? ou pode remover?
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome
        
    @property
    def contato(self) -> str:
        return self.__contato
    
    @contato.setter
    def contato(self, contato:str) -> None:
        self.__contato = contato
        
    @property
    def quartos(self) -> list:
        return self.__quartos
    
    @quartos.setter
    def quartos(self, quartos:list) -> None:
        self.__quartos = quartos
        
    @property
    def reservas(self) -> list:
        return self.__reservas
    
    @reservas.setter
    def reservas(self, reservas:list) -> None:
        self.__reservas = reservas
        
    @property
    def produtos(self) -> list:
        return self.__produtos
    
    @produtos.setter
    def produtos(self, produtos:list) -> None:
        self.__produtos = produtos
        
    def mostra_menu_principal(self) -> None:
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
        print('10. teste')
        
    def consulta_disponibilidade(self) -> None:
        print('\nPara procurar por quartos vagos, é preciso informar o dia de início e o quarto desejado.')
        print('Por favor, digite um dia do mês:')
        input_de_dia: str = validador_input_numeros()
        
        print('\nNossos quartos são do tipo (S)tandard, (M)aster e (P)remium.')
        print('Digite o número de um quarto:')
        print('S: 101, 102, 103, 104, 105,\nM: 201, 202, 203, 204\nP: 301, 302, 303')
        input_de_quarto: str = validador_input_numeros()
        
        self.verifica_disponibilidade(input_de_dia, input_de_quarto)
        press_enter()
        
    def verifica_disponibilidade(self, dia:str, quarto:str)-> bool:
    # procura o quarto desejado na lista de reservas e, caso encontrado, verifica se não há colisão de dias com outras reservas;
    # caso o quarto desejado não for encontrado na lista de reservas, significa que está livre.
        
        existe_na_lista_de_reservas: bool = False
        
        for reserva in self.reservas:      # dia_inicio[0], dia_fim[1], cliente[2], quarto[3], status[4]
            
            if quarto == reserva[3]:
                if int(reserva[0]) <= int(dia) <= int(reserva[1]):      
                    print(f'O quarto {quarto} já está reservado (Reserva existente entre dias {reserva[0]} e {reserva[1]}).')
                    existe_na_lista_de_reservas = True
                    #break
                    return False
                else:
                    print(f'(INFORMAÇÃO: o dia {dia} no quarto {quarto} está vago até o dia {self.verifica_disponibilidade_ate_quando(dia,reserva[0])}.)')
                    existe_na_lista_de_reservas = True
                    #break
                    return True
            # seria bom validar input do usuário para o quarto
        
        if existe_na_lista_de_reservas == False:
            # somente no caso de não encontrar o quarto na lista de reservas:
            print(f'O dia {dia} no quarto {quarto} está definitivamente vago.')
            return True
            
    def verifica_disponibilidade_ate_quando(self, dia_de_entrada:str, dia_ja_reservado:str) -> str:
    # informa o dia (str) a partir do qual uma reserva existente conflitará com o dia escolhido pelo usuário;
    # útil para o usuário saber quantos dias reserváveis estão disponíveis;
    # ex: escolhe dia 5; há reserva entre dia 10 e 12; retorna dia 10
        for i in range(int(dia_de_entrada), 31):
            if i < int(dia_ja_reservado):
                continue
            else:
                return str(i)
            
    def consulta_reserva(self) -> None:
        print('\nEscolha uma das opções de filtro para pesquisa:')
        print('1.  Pesquisa por dia do mês')
        print('2.  Pesquisa por nome do(a) cliente')
        print('3.  Pesquisa por número do quarto')
        input_do_usuario: str = validador_input_numeros()
        
        match input_do_usuario:
            case '1':
                print('Digite o dia do mês:')
                input_do_usuario: str = validador_input_numeros()
                                
                dia_informado: int = int(input_do_usuario)
                existe_dia_informado: bool = False
                
                for reserva in self.reservas:   # dia_inicio[0], dia_fim[1], cliente[2], quarto[3], status[4]
                    if int(reserva[0]) <= dia_informado <= int(reserva[1]) and (reserva[4].lower() == 'a'):
                        existe_dia_informado = True
                        print(f'RESERVADO: Cliente {reserva[2]} entre dias {reserva[0]} e {reserva[1]} no quarto {reserva[3]}')
                if existe_dia_informado == False:
                    print(f'Não há nenhuma reserva em nenhum quarto no dia {dia_informado}.')
                press_enter()
                
            case '2':
                print('Digite o nome do(a) cliente:')
                input_do_usuario: str = input()
                
                cliente_informado: str = input_do_usuario
                existe_cliente_informado: bool = False
                
                for reserva in self.reservas:
                    if cliente_informado.lower() == reserva[2].lower():
                        existe_cliente_informado = True
                        print(f'RESERVADO: Cliente {reserva[2]} entre dias {reserva[0]} e {reserva[1]} no quarto {reserva[3]}')
                if existe_cliente_informado == False:
                    print(f'Não há nenhum(a) cliente de nome {cliente_informado} com alguma reserva.')
                press_enter()
                
            case '3':
                print('Digite o número do quarto:')
                input_do_usuario: str = validador_input_numeros()
                
                quarto_informado: str = input_do_usuario
                existe_quarto_informado: bool = False
                
                for reserva in self.reservas:
                    if quarto_informado == reserva[3]:
                        existe_quarto_informado = True
                        print(f'RESERVADO: O quarto {reserva[3]} está reservado para cliente {reserva[2]} entre dia {reserva[0]} e {reserva[1]}.')
                if existe_quarto_informado == False:
                    print(f'O quarto {quarto_informado} não possui nenhuma reserva.')
                press_enter()
                
    def realiza_reserva(self) -> None:
        print('Informe o dia de entrada:')
        dia_de_entrada_informado: str = validador_input_numeros()
        
        print('Informe o dia de saída:')
        die_de_saida_informado: str = validador_input_numeros()
        
        print('Informe o quarto desejado:')
        quarto_informado: str = validador_input_numeros()
        
        if self.verifica_disponibilidade(dia_de_entrada_informado, quarto_informado) == True:
            print('Informe seu nome:')
            nome_informado: str = input()
        else:
            print('Retornando ao menu principal...')
            press_enter()
            return
        
        for reserva in self.reservas:
            pass