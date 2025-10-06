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
         
