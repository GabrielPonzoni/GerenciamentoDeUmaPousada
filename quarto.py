class Quarto:
    
    def __init__(self, numero: int, categoria: str, diaria: float, consumo: list[int]):
        
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.__consumo = consumo
        
    @property
    def numero(self) -> int:
        return self.__numero
    
    @numero.setter
    def numero(self, numero:int) -> None:
        self.__numero = numero
        
    @property
    def categoria(self) -> str:
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria:str) -> None:
        self.__categoria = categoria
        
    @property
    def diaria(self) -> float:
        return self.__diaria
    
    @diaria.setter
    def diaria(self, diaria:float) -> None:
        self.__diaria = diaria
        
    @property
    def consumo(self) -> list[int]:
        return self.__consumo
    
    @consumo.setter
    def consumo(self, consumo:list[int]) -> None:
        self.__consumo = consumo