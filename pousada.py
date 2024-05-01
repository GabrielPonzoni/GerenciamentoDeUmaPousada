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
        
        self.verifica_disponibilidade(input_de_dia, int(input_de_quarto))
        press_enter()
        
    def verifica_disponibilidade(self, dia:str, quarto:int) -> bool:
    # procura o quarto desejado na lista de reservas e, caso encontrado, verifica se não há colisão de dias com outras reservas;
    # caso o quarto desejado não for encontrado na lista de reservas, significa que está livre.
        
        existe_na_lista_de_reservas: bool = False
        
        for reserva in self.reservas:      # Reserva(dia_inicio, dia_fim, cliente, quarto, status)
            
            if int(quarto) == reserva.quarto.numero:
                if int(reserva.dia_inicio) <= int(dia) <= int(reserva.dia_fim):      
                    print(f'O quarto {quarto} já está reservado (Reserva existente entre dias {reserva.dia_inicio} e {reserva.dia_fim}).')
                    existe_na_lista_de_reservas = True
                    #break
                    return False
                else:
                    print(f'(INFORMAÇÃO: o dia {dia} no quarto {quarto} está vago até o dia {self.verifica_disponibilidade_ate_quando(dia,reserva.dia_inicio,reserva.dia_fim)}.)')
                    existe_na_lista_de_reservas = True
                    #break
                    return True
            # seria bom validar input do usuário para o quarto
        
        if existe_na_lista_de_reservas == False:
            # somente no caso de não encontrar o quarto na lista de reservas:
            print(f'O dia {dia} no quarto {quarto} está definitivamente vago.')
            return True
            
    def verifica_disponibilidade_ate_quando(self, dia_de_entrada:str, dia_inicio_ja_reservado:str, dia_fim_ja_reservado:str) -> str:
    # informa o dia (str) a partir do qual uma reserva existente conflitará com o dia escolhido pelo usuário;
    # útil para o usuário saber quantos dias reserváveis estão disponíveis;
    # ex: escolhe dia 5; há reserva entre dia 10 e 12; retorna dia 10;
    # IMPORTANTE:
    # este método ainda pode ser aprimorado para casos com mais reservas no mês. mas aumenta muito complexidade;
    
        # caso 1: dia de entrada antes do período reservado
        if int(dia_de_entrada) < int(dia_inicio_ja_reservado):
            for i in range(int(dia_de_entrada), 30):
                if i < int(dia_inicio_ja_reservado):
                    continue
                else:
                    return str(i)
                             
        # caso 2: dia de entrada depois do período reservado
        elif int(dia_de_entrada) > int(dia_fim_ja_reservado):
            return str(30)
            
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
                
                for reserva in self.reservas:           # Reserva(dia_inicio, dia_fim, cliente, quarto, status)
                    if int(reserva.dia_inicio) <= dia_informado <= int(reserva.dia_fim) and (reserva.status.lower() == 'a'):
                        existe_dia_informado = True
                        print(f'RESERVADO: Cliente {reserva.cliente} entre dias {reserva.dia_inicio} e {reserva.dia_fim} no quarto {reserva.quarto.numero}')
                if existe_dia_informado == False:
                    print(f'Não há nenhuma reserva em nenhum quarto no dia {dia_informado}.')
                press_enter()
                
            case '2':
                print('Digite o nome do(a) cliente:')
                input_do_usuario: str = input()
                
                cliente_informado: str = input_do_usuario
                existe_cliente_informado: bool = False
                
                for reserva in self.reservas:
                    if cliente_informado.lower() == reserva.cliente.lower() and (reserva.status.lower() == 'a'):
                        existe_cliente_informado = True
                        print(f'RESERVADO: Cliente {reserva.cliente} entre dias {reserva.dia_inicio} e {reserva.dia_fim} no quarto {reserva.quarto.numero}')
                if existe_cliente_informado == False:
                    print(f'Não há nenhum(a) cliente de nome {cliente_informado} com reserva ATIVA.')
                press_enter()
                
            case '3':
                print('Digite o número do quarto:')
                input_do_usuario: str = validador_input_numeros()
                
                quarto_informado = int(input_do_usuario)
                existe_quarto_informado: bool = False
                
                for reserva in self.reservas:
                    if quarto_informado == reserva.quarto.numero and (reserva.status.lower() == 'a'):
                        existe_quarto_informado = True
                        print(f'RESERVADO: O quarto {reserva.quarto.numero} está reservado para cliente {reserva.cliente} entre dia {reserva.dia_inicio} e {reserva.dia_fim}.')
                if existe_quarto_informado == False:
                    print(f'O quarto {quarto_informado} não possui nenhuma reserva.')
                press_enter()
                
    def realiza_reserva(self) -> None:
        print('Informe o dia de entrada:')
        dia_de_entrada_informado: str = validador_input_numeros()
        
        print('Informe o dia de saída:')
        dia_de_saida_informado: str = validador_input_numeros()
        
        print('Informe o quarto desejado:')
        quarto_informado: str = validador_input_numeros()
        
        if (self.verifica_disponibilidade(dia_de_entrada_informado, quarto_informado) == True) and (
            (self.verifica_disponibilidade(dia_de_saida_informado, quarto_informado) == True)):
            
            print('Informe seu nome:')
            nome_informado: str = input()
            
            # verifica se nome informado já possui alguma reserva
            for reserva in self.reservas:
                if nome_informado.lower() == reserva.cliente.lower():
                    print(f'{nome_informado} já possui uma reserva na pousada.')
                    print('Reserva não realizada!')
                    break
            
            self.reservas.append(Reserva(int(dia_de_entrada_informado), int(dia_de_saida_informado), nome_informado, int(quarto_informado), 'A'))
            
            # localiza o quarto da reserva recém realizada (último item da lista que recebeu append);
            # é a mesma ideia do que foi feito no método carrega_reservas() na main()
            for quarto in self.quartos:
                if (int(quarto.numero) == int(self.reservas[-1].quarto)):
                    self.reservas[-1].quarto = quarto 
                    break
                
            print('Sua reserva foi realizada com êxito!')
            print('Dados da sua reserva:')
            print(f'\tCliente: {self.reservas[-1].cliente}')
            print(f'\tCheck-in: {self.reservas[-1].dia_inicio}')
            print(f'\tCheck-out: {self.reservas[-1].dia_fim}')
            print(f'\tQuarto: {self.reservas[-1].quarto.numero}')
            press_enter()            
        else:
            print('Datas informadas colidem com reserva existente.')
            press_enter()
            return
        
    def cancela_reserva(self):
        nome_informado = input('Informe o nome do cliente para cancelar sua reserva:\n')
        for reserva in self.reservas:
            if (reserva.cliente == nome_informado):
                reserva.status = 'C'
                print(f'A reserva de {nome_informado} foi cancelada com êxito.')
                print('INFORMAÇÃO: dados da reserva cancelada:')
                print(f'\tDia de entrada: {reserva.dia_inicio}; Dia de saída: {reserva.dia_fim}; Quarto: {reserva.quarto.numero}')
                press_enter()
                return
        print(f'Não há nenhum cliente com nome {nome_informado}. Voltando...')
        press_enter()
        
    def realiza_check_in(self):
        nome_informado = input('Informe o nome do(a) cliente:\n')
        for reserva in self.reservas:
            if (reserva.cliente.lower() == nome_informado.lower()) and (reserva.status.lower() == 'a'):
                reserva.status = 'I'
                print(f'Cliente {nome_informado} fez check-in com êxito.')
                print('INFORMAÇÃO:')
                print(f'\tDia de entrada: {reserva.dia_inicio}')
                print(f'\tDia de saída: {reserva.dia_fim}')
                print(f'\tQuarto: {reserva.quarto.numero}')
                print(f'\tNúmero de dias de hospedagem: {int(reserva.dia_fim) - int(reserva.dia_inicio)}')
                print(f'\tValor das diárias a pagar: {(int(reserva.dia_fim) - int(reserva.dia_inicio)) * reserva.quarto.diaria}')
                press_enter()
                return
        print(f'Não há nenhum cliente com nome {nome_informado}. Voltando...')
        press_enter()
        
    def realiza_check_out(self):
        nome_informado = input('Informe o nome do(a) cliente:\n')
        for reserva in self.reservas:
            if (reserva.cliente.lower() == nome_informado.lower()) and (reserva.status.lower() == 'i'):
                reserva.status = 'O'
                print(f'Cliente {nome_informado} faz check-out agora.')
                print('INFORMAÇÃO:')
                print(f'\tDia de entrada: {reserva.dia_inicio}')
                print(f'\tDia de saída: {reserva.dia_fim}')
                print(f'\tQuarto: {reserva.quarto.numero}')
                print(f'\tNúmero de dias de hospedagem: {int(reserva.dia_fim) - int(reserva.dia_inicio)}')
                print(f'\tValor das diárias a pagar: R$ {(int(reserva.dia_fim) - int(reserva.dia_inicio) + 1) * reserva.quarto.diaria}')
                print(f'\tValor dos produtos consumidos: R$ {self.calcula_valor_produtos_consumidos(reserva)}')
                print('---------------------------------')
                print(f'\tValor total: {(int(reserva.dia_fim) - int(reserva.dia_inicio)) * reserva.quarto.diaria + self.calcula_valor_produtos_consumidos(reserva)}')
                press_enter()
                return
                
        print(f'Não há nenhum cliente de nome {nome_informado} hospedado nesse momento. Voltando...')
        press_enter()
        
    def calcula_valor_produtos_consumidos(self, reserva_selecionada:Reserva) -> float:
        # calcula o valor dos produtos consumidos
        valor_produtos_consumidos: float = 0
        for codigo_produto_consumido in reserva_selecionada.quarto.consumo:
            for produto in self.produtos:
                if int(codigo_produto_consumido) == int(produto.codigo):
                    valor_produtos_consumidos += produto.preco
        return valor_produtos_consumidos
            
                
    def registra_consumo(self):
        nome_informado = input('Informe o nome do(a) cliente:\n')
        for reserva in self.reservas:
            if (reserva.cliente.lower() == nome_informado.lower()) and (reserva.status.lower() == 'i'):
                print(f'LISTA DE PRODUTOS DISPONÍVEIS NO QUARTO de {nome_informado}:')
                print('=============================================================')

                for produto in self.produtos:
                    print(f'{produto.codigo}\t{produto.nome}\t\t{produto.preco}')
                    
                print('Escolha um produto digitando o seu código numérico:')
                input_do_usuario = validador_input_numeros()
                
                # registra o consumo na lista de consumo do respectivo quarto.
                # à lista de consumo do quarto será adicionado um objeto Produto.
                # ATENÇÃO: no arquivo 'quarto.txt', o consumo será traduzido apenas no código do produto
                for produto in self.produtos:
                    if int(input_do_usuario) == produto.codigo:
                        reserva.quarto.consumo.append(str(input_do_usuario))
                
                print(f'Produto de código \"{reserva.quarto.consumo[-1]}\" registrado com êxito.')
                press_enter()
                return
                
        print(f'Não há nenhum cliente de nome {nome_informado} hospedado nesse momento. Voltando...')
        press_enter()