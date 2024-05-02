from functions import *
from reserva import Reserva

class Pousada:
    
    def __init__(self, nome:str, contato:str, quartos:list, reservas:list, produtos:list):

        self.__nome = nome
        self.__contato = contato
        self.__quartos = quartos
        self.__reservas = reservas
        self.__produtos = produtos
    
    #get e setter __nome
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome
    
    #get e setter __contato
    @property
    def contato(self) -> str:
        return self.__contato
    
    @contato.setter
    def contato(self, contato:str) -> None:
        self.__contato = contato
    
    #get e setter __quartos
    @property
    def quartos(self) -> list:
        return self.__quartos
    
    @quartos.setter
    def quartos(self, quartos:list) -> None:
        self.__quartos = quartos
        
    #get e setter __reservas    
    @property
    def reservas(self) -> list:
        return self.__reservas
    
    
    @reservas.setter
    def reservas(self, reservas:list) -> None:
        self.__reservas = reservas
    
    #get e setter __produtos
    @property
    def produtos(self) -> list:
        return self.__produtos
    
    @produtos.setter
    def produtos(self, produtos:list) -> None:
        self.__produtos = produtos
        
    def mostra_menu_principal(self) -> None:
        """
        Mostra na tela um menu formatado com as opçoes que o usuário pode escolher
        
        Returns:
        None
        """
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
        print('8.  Salvar alterações')
        print('9.  Sair')
        
    def consulta_disponibilidade(self) -> None:
        """
        Solicita ao usuário um dia e um quarto para verificar a disponibilidade.

        Esta função solicita ao usuário um dia do mês e um quarto desejado para verificar a disponibilidade.
        O dia do mês deve ser fornecido como um número.
        O quarto pode ser selecionado entre os tipos: Standard (S), Master (M) e Premium (P).

        Returns:
            None. A função imprime informações sobre a disponibilidade de quartos.
        """
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
        """
        Verifica a disponibilidade de um quarto em um determinado dia.

        Args:
            dia (str): O dia para verificar a disponibilidade, representado como uma string.
            quarto (int): O número do quarto a ser verificado.

        Returns:
            bool: True se o quarto estiver disponível, False caso contrário.

        """
        existe_na_lista_de_reservas: bool = False
        
        for reserva in self.reservas:      # Reserva(dia_inicio, dia_fim, cliente, quarto, status)        
            if int(quarto) == reserva.quarto.numero and (reserva.status.lower() == 'a' or reserva.status.lower() == 'i'):
                if int(reserva.dia_inicio) <= int(dia) <= int(reserva.dia_fim):      
                    print(f'O quarto {quarto} já está reservado (Reserva existente entre dias {reserva.dia_inicio} e {reserva.dia_fim}).')
                    existe_na_lista_de_reservas = True
                    return False
                else:
                    print(f'(INFORMAÇÃO: o dia {dia} no quarto {quarto} está vago até o dia {self.verifica_disponibilidade_ate_quando(dia,reserva.dia_inicio,reserva.dia_fim)}.)')
                    existe_na_lista_de_reservas = True
                    return True
                                        # seria bom validar input do usuário para o quarto
        
        if existe_na_lista_de_reservas == False:
            # somente no caso de não encontrar o quarto na lista de reservas:
            print(f'O dia {dia} no quarto {quarto} está definitivamente vago.')
            return True
            
    def verifica_disponibilidade_ate_quando(self, dia_de_entrada:str, dia_inicio_ja_reservado:str, dia_fim_ja_reservado:str) -> str:
        """
        Informa o último dia disponível antes de conflitar com uma reserva existente.

        Esta função informa o último dia disponível antes de um conflito com uma reserva existente.
        É útil para o usuário saber quantos dias reserváveis estão disponíveis antes de uma reserva conflitar.

        Args:
            dia_de_entrada (str): O dia escolhido pelo usuário, representado como uma string.
            dia_inicio_ja_reservado (str): O dia de início da reserva já existente, representado como uma string.
            dia_fim_ja_reservado (str): O dia de fim da reserva já existente, representado como uma string.

        Returns:
            str: O último dia disponível antes do conflito com a reserva existente, representado como uma string.

        """
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
        """
        Permite ao usuário pesquisar reservas com base em diferentes critérios.

        Esta função permite ao usuário pesquisar reservas com base em diferentes critérios, como dia do mês,
        nome do cliente ou número do quarto. Após a seleção do critério de pesquisa, o usuário fornece
        informações adicionais conforme necessário e a função exibe as reservas correspondentes, se houver.

        Returns:
            None. A função imprime as reservas correspondentes ou uma mensagem indicando que não foram encontradas reservas.

        """
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
        """
        Realiza uma reserva na pousada com base nas informações fornecidas pelo usuário.

        Este método solicita ao usuário informações sobre o dia de entrada, dia de saída e quarto desejado.
        Em seguida, verifica a disponibilidade do quarto para os dias informados.
        Se o quarto estiver disponível para os dias de entrada e saída e o nome do cliente não estiver associado a uma reserva existente,
        a reserva é realizada com sucesso e adicionada à lista de reservas da pousada.

        Returns:
            None. A função imprime informações sobre a reserva realizada ou uma mensagem indicando que a reserva não pôde ser concluída.

        """
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
        
    def cancela_reserva(self) -> None:
        """
        Cancela a reserva de um cliente na pousada.

        Esta função solicita ao usuário o nome do cliente cuja reserva deseja cancelar.
        Em seguida, percorre a lista de reservas da pousada e, se encontrar uma reserva associada ao cliente informado,
        altera o status da reserva para 'C' (cancelado) e imprime os detalhes da reserva cancelada.
        Se não encontrar nenhuma reserva associada ao cliente informado, imprime uma mensagem indicando que nenhum cliente com esse nome foi encontrado.

        Returns:
            None. A função imprime uma mensagem indicando que a reserva foi cancelada com sucesso ou uma mensagem indicando que nenhum cliente com esse nome foi encontrado.

        """
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
        
    def realiza_check_in(self) -> None:
        """
        Realiza o check-in de um cliente na pousada.

        Esta função solicita ao usuário o nome do cliente para realizar o check-in.
        Em seguida, percorre a lista de reservas da pousada e, se encontrar uma reserva associada ao cliente informado e com status 'A' (ativa),
        altera o status da reserva para 'I' (check-in realizado) e imprime os detalhes da reserva, incluindo o número de dias de hospedagem e o valor total das diárias a pagar.
        Se não encontrar nenhuma reserva associada ao cliente informado ou se a reserva não estiver ativa, imprime uma mensagem indicando que nenhum cliente com esse nome foi encontrado ou que não há uma reserva ativa para esse cliente.

        Returns:
            None. A função imprime uma mensagem indicando que o check-in foi realizado com sucesso ou uma mensagem indicando que nenhum cliente com esse nome foi encontrado ou que não há uma reserva ativa para esse cliente.
        
        """
        nome_informado = input('Informe o nome do(a) cliente:\n')
        for reserva in self.reservas:
            if (reserva.cliente.lower() == nome_informado.lower()) and (reserva.status.lower() == 'a'):
                reserva.status = 'I'
                print(f'Cliente {nome_informado} fez check-in com êxito.')
                print('INFORMAÇÃO:')
                print(f'\tDia de entrada: {reserva.dia_inicio}')
                print(f'\tDia de saída: {reserva.dia_fim}')
                print(f'\tQuarto: {reserva.quarto.numero}')
                print(f'\tNúmero de dias de hospedagem: {int(reserva.dia_fim) - int(reserva.dia_inicio) + 1}')
                print(f'\tValor das diárias a pagar: {(int(reserva.dia_fim) - int(reserva.dia_inicio) + 1) * reserva.quarto.diaria}')
                press_enter()
                return
        
        print(f'Não há nenhum cliente com nome {nome_informado}. Voltando...')
        press_enter()
        
    def realiza_check_out(self) -> None:
        """
        Realiza o check-out de um cliente na pousada.

        Esta função solicita ao usuário o nome do cliente para realizar o check-out.
        Em seguida, percorre a lista de reservas da pousada e, se encontrar uma reserva associada ao cliente informado e com status 'I' (check-in realizado),
        imprime os detalhes da reserva, incluindo o número de dias de hospedagem, o valor total das diárias a pagar e o valor total dos produtos consumidos.
        Em seguida, altera o status da reserva para 'O' (check-out realizado) e limpa a lista de consumo do quarto utilizado.
        Se não encontrar nenhuma reserva associada ao cliente informado ou se a reserva não estiver com status de check-in, imprime uma mensagem indicando que nenhum cliente com esse nome foi encontrado ou que não há um check-in para esse cliente.

        Returns:
            None. A função imprime os detalhes do check-out realizado ou uma mensagem indicando que nenhum cliente com esse nome foi encontrado ou que não há um check-in para esse cliente.

        """
        nome_informado = input('Informe o nome do(a) cliente:\n')
        for reserva in self.reservas:
            if (reserva.cliente.lower() == nome_informado.lower()) and (reserva.status.lower() == 'i'):
                print(f'Cliente {nome_informado} faz check-out agora.')
                print('INFORMAÇÃO:')
                print(f'\tDia de entrada: {reserva.dia_inicio}')
                print(f'\tDia de saída: {reserva.dia_fim}')
                print(f'\tQuarto: {reserva.quarto.numero}')
                print(f'\tNúmero de dias de hospedagem: {int(reserva.dia_fim) - int(reserva.dia_inicio) + 1}')
                print(f'\tValor das diárias a pagar: R$ {(int(reserva.dia_fim) - int(reserva.dia_inicio) + 1) * reserva.quarto.diaria}')
                
                self.mostra_lista_de_produtos_consumidos(reserva)
                
                print(f'\tValor dos produtos consumidos: R$ {self.calcula_valor_produtos_consumidos(reserva)}')
                print('---------------------------------')
                print(f'\tValor total: R$ {(int(reserva.dia_fim) - int(reserva.dia_inicio) + 1) * reserva.quarto.diaria + self.calcula_valor_produtos_consumidos(reserva)}')
                
                reserva.status = 'O'        # status da reserva para check-out
                reserva.quarto.consumo = [] # IMPORTANTE: limpar o consumo do quarto utilizado
                
                press_enter()
                return
                
        print(f'Não há nenhum cliente de nome {nome_informado} hospedado nesse momento. Voltando...')
        press_enter()
        
    def mostra_lista_de_produtos_consumidos(self, reserva_selecionada:Reserva) -> None:
        """
        Mostra a lista de produtos consumidos durante a estadia de um cliente.

        Esta função recebe como entrada uma reserva e percorre a lista de códigos de produtos consumidos associados ao quarto da reserva.
        Para cada código de produto consumido, busca o produto correspondente na lista de produtos da pousada e imprime o nome e o preço do produto consumido.
        Se não encontrar nenhum produto correspondente ao código, não imprime nada.

        Args:
            reserva_selecionada (Reserva): A reserva para a qual deseja-se mostrar a lista de produtos consumidos.

        Returns:
            None. A função imprime os produtos consumidos durante a estadia do cliente.

        """
    
        for codigo_produto_consumido in reserva_selecionada.quarto.consumo:
            for produto in self.produtos:
                if str(codigo_produto_consumido) == str(produto.codigo):
                    print(f'{codigo_produto_consumido}. {produto.nome}: R$ {produto.preco}')
                    break
                else:
                    continue
        return
        
    def calcula_valor_produtos_consumidos(self, reserva_selecionada:Reserva) -> float:
        """
        Calcula o valor total dos produtos consumidos durante a estadia de um cliente.

        Esta função recebe como entrada uma reserva e percorre a lista de códigos de produtos consumidos associados ao quarto da reserva.
        Para cada código de produto consumido, busca o produto correspondente na lista de produtos da pousada e adiciona o preço do produto ao valor total dos produtos consumidos.

        Args:
            reserva_selecionada (Reserva): A reserva para a qual deseja-se calcular o valor dos produtos consumidos.

        Returns:
            float: O valor total dos produtos consumidos durante a estadia do cliente.

        """
        valor_produtos_consumidos: float = 0
        for codigo_produto_consumido in reserva_selecionada.quarto.consumo:
            for produto in self.produtos:
                if int(codigo_produto_consumido) == int(produto.codigo):
                    valor_produtos_consumidos += produto.preco
        return valor_produtos_consumidos
    
    def registra_consumo(self):
        """
        Registra o consumo de um produto por um cliente durante sua estadia na pousada.

        Esta função solicita ao usuário o nome do cliente que deseja registrar o consumo.
        Em seguida, percorre a lista de reservas da pousada e, se encontrar uma reserva associada ao cliente informado e com status 'I' (check-in realizado),
        exibe a lista de produtos disponíveis no quarto do cliente e solicita ao usuário que escolha um produto digitando seu código numérico.
        Após a escolha do produto, registra o consumo na lista de consumo do quarto da reserva.
        Se não encontrar nenhuma reserva associada ao cliente informado ou se a reserva não estiver com status de check-in, imprime uma mensagem indicando que nenhum cliente com esse nome foi encontrado ou que não há um check-in para esse cliente.

        Returns:
            None. A função imprime uma mensagem indicando que o produto foi registrado com sucesso ou uma mensagem indicando que nenhum cliente com esse nome foi encontrado ou que não há um check-in para esse cliente.

        Raises:
            Nenhuma.
        """
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
        
    def serializar_lista_de_reservas(self) -> list:
        """
        Serializa a lista de reservas da pousada em um formato adequado para armazenamento.

        Esta função percorre a lista de reservas da pousada e para cada reserva cria uma lista auxiliar contendo o dia de início, o dia de fim,
        o nome do cliente, o número do quarto e o status da reserva.
        Em seguida, adiciona a lista auxiliar à lista principal de reservas serializadas.
        Retorna a lista serializada que pode ser usada para armazenamento em um arquivo.

        Returns:
            list: A lista serializada contendo as informações das reservas da pousada.

        """
        lista_serializada: list = []
        
        for reserva in self.reservas:
            lista_auxiliar: list = []
            
            lista_auxiliar.append(str(reserva.dia_inicio))
            lista_auxiliar.append(str(reserva.dia_fim))
            lista_auxiliar.append(str(reserva.cliente))
            lista_auxiliar.append(str(reserva.quarto.numero))
            lista_auxiliar.append(str(reserva.status))
            
            lista_serializada.append(lista_auxiliar)
        return lista_serializada
            
    def serializar_lista_de_quartos(self) -> list:
        """
        Serializa a lista de quartos da pousada em um formato adequado para armazenamento.

        Esta função percorre a lista de quartos da pousada e para cada quarto cria uma lista auxiliar contendo o número do quarto, a categoria,
        a diária e os códigos dos produtos consumidos associados ao quarto.
        Os códigos dos produtos consumidos são organizados em uma lista, podendo ser variados, inclusive uma lista vazia.
        Retorna a lista serializada que pode ser usada para armazenamento em um arquivo ou para outras operações de serialização.

        Returns:
            list: A lista serializada contendo as informações dos quartos da pousada.

        """
        lista_serializada: list = []
        
        for quarto in self.quartos:
            lista_auxiliar: list = []
            
            lista_auxiliar.append(str(quarto.numero))
            lista_auxiliar.append(str(quarto.categoria))
            lista_auxiliar.append(str(quarto.diaria))
            
            # organiza os códigos dos produtos consumidos, que podem ser variados, inclusive lista vazia
            if quarto.consumo == []:
                lista_auxiliar.append('')
            else:
                for codigo_produto_consumido in quarto.consumo:
                    lista_auxiliar.append(str(codigo_produto_consumido))
            
            lista_serializada.append(lista_auxiliar)
        return lista_serializada
    
    def limpar_reservas_c_o(self):
        """
        Remove as reservas canceladas ou concluídas da lista de reservas da pousada.

        Esta função percorre a lista de reservas da pousada e identifica as reservas que estão canceladas ('C') ou concluídas ('O').
        Armazena os índices dessas reservas em uma lista para posterior remoção.
        Em seguida, itera sobre os índices das reservas a serem deletadas e remove-as da lista de reservas.
        Retorna a lista de reservas atualizada, sem as reservas canceladas ou concluídas.

        Returns:
            None. A função imprime a lista de índices das reservas a serem deletadas e a lista de reservas atualizada após a remoção.

        """
        reservas_a_deletar: list = []   # índices das reservas a deletar
        
        for reserva in self.reservas:
            if (reserva.status.lower() == 'c') or (reserva.status.lower() == 'o'):
                reservas_a_deletar.append(self.reservas.index(reserva))
                
        
        reservas_a_deletar.reverse()
        # limpa reservas do índice maior para o índice menor; isto é necessário pois
        # vai haver mudança de índice durante o laço. começando do índice maior, isso é contornado;
        
        for index in reservas_a_deletar:
            self.reservas.pop(index)