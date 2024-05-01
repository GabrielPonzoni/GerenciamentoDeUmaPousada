class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo) -> None:
        self.__codigo = codigo
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome
        
    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, preco:float) -> None:
        self.__preco = preco