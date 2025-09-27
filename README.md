💻 Sistema de Gerenciamento de Eventos
📝 Descrição
Este é um projeto de back-end para um Sistema de Gerenciamento de Eventos, desenvolvido como uma aplicação prática dos conceitos aprendidos em programação. O sistema simula o controle de eventos como workshops, palestras e meetups , funcionando como a "espinha dorsal" de uma plataforma de gestão, permitindo o cadastro de eventos, a inscrição de participantes e a emissão de relatórios detalhados. 



🚀 Funcionalidades
Gerenciamento de Eventos
Cadastro de Eventos: Permite criar novos eventos com os seguintes atributos:

Nome, data e local.

Capacidade máxima e categoria (ex: Tech, Marketing).

Preço do ingresso.

Validações:

A data do evento não pode ser anterior à data atual.

A capacidade máxima deve ser um número positivo.

Inscrição de Participantes

Cadastro de Participantes: Inscreve participantes com nome, email e o evento desejado.

Regras de Negócio:

Não permite inscrições em eventos que já atingiram a capacidade máxima.

Impede que um mesmo e-mail seja cadastrado mais de uma vez no mesmo evento.

Administração do Sistema
Listar todos os eventos e suas informações.

Buscar eventos por categoria ou por data.

Cancelar a inscrição de um participante.

Funcionalidade de check-in para marcar a presença de um participante no evento.

Relatórios e Análises
Exibir o número total de inscritos por evento.

Gerar uma lista de eventos que ainda possuem vagas disponíveis.

Calcular a receita total de um evento específico.

🛠️ Conceitos Aplicados
O desenvolvimento deste projeto foi fortemente baseado nos pilares da 

Programação Orientada a Objetos (POO): 


Herança: As classes Workshop e Palestra herdam características da superclasse Evento, adicionando atributos específicos.


Polimorfismo: O método detalhes() se comporta de maneira diferente para Workshop e Palestra, demonstrando o polimorfismo.


Encapsulamento: Os atributos das classes são mantidos como privados, e o acesso é controlado por meio de getters e setters.


Classes: O sistema é estruturado nas classes Evento (superclasse), Workshop e Palestra (subclasses), Participante e SistemaEventos como classe principal.

🔧 Tecnologias Utilizadas
Linguagem: Python


Testes: unittest 


Persistência de Dados: SQLite3 ou arquivo .json 


Controle de Versão: Git e GitHub 

⚙️ Como Executar o Projeto
Bash

# 1. Clone o repositório
git clone https://github.com/seu-usuario/Sistema_Gerenciamento_de_Eventos.git

# 2. Navegue até o diretório do projeto
cd Sistema_Gerenciamento_de_Eventos

# 3. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

# 4. (Opcional) Instale as dependências
pip install -r requirements.txt

# 5. Execute o sistema
python main.py