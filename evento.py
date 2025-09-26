class Evento:
    def __init__(self, nome, data, local, capacidade_maxima, categoria, preco):
        self.__nome = nome
        self.__data = data
        self.__local = local
        self.__capacidade_maxima = capacidade_maxima
        self.__categoria = categoria
        self.__preco = preco
        self.__inscritos = []
    
    
    def get_nome(self):
        return self.__nome
    
    
    
    def get_detalhes(self):
        print(f'Nome: {self.__nome}\n Data: {self.__data}\n Local: {self.__local}\n Capacidade: {self.__capacidade_maxima}\n Categoria: {self.__categoria}\n Preco: {self.__preco}\n Inscritos: {self.__inscritos}') # retorna todas as informações da classe Principal.
class Workshop(Evento):
    def __init__(self, nome, data, local, capacidade_maxima, categoria, preco,material_necessario):
        super().__init__(nome, data, local, capacidade_maxima, categoria, preco) ## reutilização de alguns parametros da classe principal
        self.__material_necessario = material_necessario # criei um novo parametro dentro da classe workshop onde armazena os materiais
    def get_detalhes(self):
        super().get_detalhes() ## metodo super que reaproveita todo o print da função get detalhes da classe evento sem precisa copiar e exibir novamente
        
        print(f'Material Necessário : {self.__material_necessario}') ## Printamos o material necessario em quantidades


class Palestra(Evento):
    def __init__(self,nome,data,local,capacidade_maxima,categoria,preco,nome_palestrante,tema_especifico): 
        super().__init__(nome,data,local,capacidade_maxima,categoria,preco) # Reutilização de parametros novamente da classe principal
        self.__nome_palestrante = nome_palestrante ## criando novos parametros para a class palestra que herda de Evento
        self.__tema_especifico = tema_especifico
    def get_detalhes(self):
        super().get_detalhes() ## vai reutilizar o mesmo codigo da classe mae para exibir os detalhes
        
        print(f'Nome do Palestrante:{self.__nome_palestrante}\n Tema Da Palestra: {self.__tema_especifico}')
    
    
    
class Participante:
    def __init__(self,nome,email,evento):
        self.__nome = nome
        self.__email = email
        self.__evento = evento
    def get_nome(self):
        return self.__nome # -> retorna o nome do participante que esta no metodo privado,acessamos usando o get_nome.
    
    def exibir_detalhes(self):
        print(f'Nome do Participante: {self.__nome}\n Email: {self.__email}\n Evento: {self.__evento.get_nome()}') ## Atributos de nome , email e evento sao privados , na ultima ocasiao que passei o self.evento get nome ele ira pegar o nome exclusivamento do evento que O participante esta alocado !
        
        
class Sistema_Evento:
    def __init__(self):
       self.__lista_eventos = [] # -> Lista para armazenar todos os eventos.
       self.__lista_Participantes = [] # -> armazena todos os participantes.
       
       
    def cadastrar_evento(self,evento): ## -> metodo para cadastrar evento dentro da lista de eventos
        self.__lista_eventos.append(evento)
        
    def cadastrar_participante(self,participante): # -> metodo para adicionar participante a lista de participantes
        self.__lista_Participantes.append(participante)
        
        
    def listar_eventos(self):
        for evento in self.__lista_eventos: ## metodo para imprimir toda a lista de eventos
           pass