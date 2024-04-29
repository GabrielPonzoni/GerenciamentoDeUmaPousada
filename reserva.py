from quarto import Quarto
class Reserva:
    
    # Reservas: (A)tiva, (C)ancelada, check-(I)n, check-(o)ut
    # (A) = reserva funcionando, não pode reservar aqui
    # (C) = pode reservar aqui
    # (I) = tem alguém já com quarto e com dia
    # (O) = quarto e dia vago, pode reservar aqui
    
    def __init__(self, dia_inicio:int, dia_fim:int, cliente:str, quarto:Quarto, status:str) -> None:
        
        self.__dia_inicio = dia_inicio
        self.__dia_fim = dia_fim
        self.__cliente = cliente
        self.__quarto = quarto
        self.__status = status
        
    @property
    def dia_inicio(self) -> int:
        return self.__dia_inicio
    
    @dia_inicio.setter
    def dia_inicio(self, dia_inicio:int) -> int:
        self.__dia_inicio = dia_inicio
        
    @property
    def dia_fim(self) -> int:
        return self.__dia_fim
    
    @dia_fim.setter
    def dia_fim(self, dia_fim:int) -> int:
        self.__dia_fim = dia_fim
        
    @property
    def cliente(self) -> str:
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente:str) -> str:
        self.__cliente = cliente
        
    @property
    def quarto(self) -> Quarto:
        return self.__quarto
    
    @quarto.setter
    def quarto(self, quarto:Quarto) -> Quarto:
        self.__quarto = quarto
        
    @property
    def status(self) -> str:
        return self.__status
    
    @status.setter
    def status(self, status:str) -> str:
        self.__status = status