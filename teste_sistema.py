import unittest
from evento import Evento

class TestSistema(unittest.TestCase):
    def test_criar_evento(self):
        evento = Evento('jose','27/04/2027', 'pernambuco', 8, 'luta',87)
        self.assertEqual('jose', evento.get__nome())