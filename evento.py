class Evento:
    def __init__(self, nome, data, local, capacidade_maxima, categoria, preco):
        self.__nome = nome
        self.__data = data
        self.__local = local
        self.__capacidade_maxima = capacidade_maxima
        self.__categoria = categoria
        self.__preco = preco
        self.__inscritos = []
    def get_detalhes(self):
        print(f'Nome: {self.__nome}\n Data: {self.__data}\n Local: {self.__local}\n Capacidade: {self.__capacidade_maxima}\n Categoria: {self.__categoria}\n Preco: {self.__preco}\n Inscritos: {self.__inscritos}')
class Workshop(Evento):
    def __init__(self, nome, data, local, capacidade_maxima, categoria, preco,material_necessario):
        super().__init__(nome, data, local, capacidade_maxima, categoria, preco)
        self.__material_necessario = material_necessario


class Palestra(Evento):
    pass
    
    
    
class Participante:
    pass