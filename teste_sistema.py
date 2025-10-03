import unittest
from evento import Evento

class TestSistema(unittest.TestCase):
    def test_criar_evento(self):
        evento = Evento('Festival de Verão','27/04/2027', 'pernambuco', 8, 'luta',87)
        self.assertEqual('Festival de Verão', evento.get_nome())
        
    def test_2_cadastrar_participante_com_sucesso(self):
        """Verifica se um participante é cadastrado corretamente no sistema e no evento."""
        participante = participante("Ana Souza", "ana@email.com", self.evento_tech)
        self.sistema.cadastrar_participante(participante, self.evento_tech)
        
        # Verifica se o participante está na lista de inscritos do evento
        inscritos_evento = self.evento_tech.get_inscritos()
        self.assertIn(participante, inscritos_evento)
        
    def test_10_encontrar_eventos_com_vagas(self):
        """Verifica se o sistema identifica corretamente eventos com vagas disponíveis[cite: 25]."""
        # Lotando o workshop
        p1 = participante("Carlos", "carlos@email.com", self.workshop_dados)
        p2 = participante("Bia", "bia@email.com", self.workshop_dados)
        self.sistema.cadastrar_participante(p1, self.workshop_dados)
        self.sistema.cadastrar_participante(p2, self.workshop_dados)

        eventos_com_vagas = self.sistema.listar_eventos_com_vagas()
        
        # Apenas o evento_tech (100 vagas) deve ser retornado, já que o workshop (2 vagas) está lotado
        self.assertEqual(1, len(eventos_com_vagas))
        self.assertEqual("Python Conf", eventos_com_vagas[0].get_nome())

        
        
  