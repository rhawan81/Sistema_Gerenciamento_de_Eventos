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
    def get_categoria(self):
        return self.__categoria # metodo para retornar a categoria do evento 
    
    def get_data(self):
        return self.__data ## retorna a data do evento
    
    def get_inscritos(self):
        return self.__inscritos
    
    def get_capacidade(self):
        return self.__capacidade_maxima
    
    def get_calculo(self):
        return len(self.__inscritos) * self.__preco
    def get_preco(self):
        return self.__preco
        
    
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
    def __init__(self,nome,email,evento,checkin_realizado = False):
        self.__nome = nome
        self.__email = email
        self.__evento = evento
        self.__checkin_realizado = False
    def get_nome(self):
        return self.__nome # -> retorna o nome do participante que esta no metodo privado,acessamos usando o get_nome.
    
    def exibir_detalhes(self):
        print(f'Nome do Participante: {self.__nome}\n Email: {self.__email}\n Evento: {self.__evento.get_nome()}') ## Atributos de nome , email e evento sao privados , na ultima ocasiao que passei o self.evento get nome ele ira pegar o nome exclusivamento do evento que O participante esta alocado !
        
    def get_email(self):
        return self.__email ## criado para fazer a verificação do email dentro do sistema e tambem para retornar o email do participante
    
    def fazer_checkin(self):
        self.__checkin_realizado = True
        print('Checkin feito com sucesso !')
        
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
            evento.get_detalhes()
            print("-" * 20)
            
    def buscar_por_categoria(self,categoria): ## busca a categoria do evento onde foi criada  na base da classe  evento
        self.categoria = categoria
        for buscar in self.__lista_eventos: ## percorre toda a lista de eventos 
            if buscar.get_categoria() == self.categoria: ## se a categoria buscada foi igual a categoria solicitada encontramos
                buscar.get_detalhes() ## retorna as informaçoes do evento
                print("-" * 20)
                
    def buscar_por_data(self,data_busca): ## metodo para buscar a data do evento 
        self.data_busca = data_busca
        print(f"--- EVENTOS ENCONTRADOS NA DATA: {data_busca} ---")
        
        for evento in self.__lista_eventos: ## se a data do evento for igual a data atual solicitada pelo usuario encotramos a data
            if evento.get_data() == self.data_busca:
                evento.get_detalhes()
                print("-" * 20)
                
    def cancelar_inscricao(self,email): # metoodo para cancelar a inscrição
        self.email = email 
        participantes_para_remover = [] # lista vazia contendo os participantes que queremos remover
        for participante in self.__lista_Participantes: ## um loop para percorrer toda a lista de participantes
            if participante.get_email() == self.email: # se o email for igual adicionaremos na lista para remover o participante
                participantes_para_remover.append(participante)
        if participantes_para_remover:    
            for participante in participantes_para_remover: ## percorre a lista de participantes
                self.__lista_Participantes.remove(participante) # remove os participantes 
            print(f"Inscrição do email {email} cancelada com sucesso.")
            
        else:
            print(f"Participante com email {email} não encontrado.")
    def realizar_chekin(self,email):
        for participante in self.__lista_Participantes:
            if participante.get_email() == email:
                participante.fazer_checkin()
                break
    def gerar_relatorio(self):
        for evento  in self.__lista_eventos:
           num = len(evento.get_inscritos())
           print(f'Nome do Evento: {evento.get_nome()} Numero de inscritos: {num}')
    def listar_eventos_com_vaga(self):
        print('-- EVENTO COM VAGAS DISPONIVEIS-----')
        for evento in self.__lista_eventos:
            if len(evento.get_inscritos()) < evento.get_capacidade():
                evento.get_detalhes()
            else:
                print('Evento Indisponivel ')
                
    def calcular_receita_evento(self,nome_evento):
        for evento in self.__lista_eventos:
            if evento.get_nome() == nome_evento:
                 receita = len(evento.get_inscritos()) * evento.get_preco()
                 print(f"A receita para o evento '{nome_evento}' é de R${receita:.2f}.")
                 return receita
        print(f'Erro: Evento {nome_evento} não encontrado')
        return 0
         