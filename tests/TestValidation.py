import unittest
from validation.validation import validation

class TestValidation(unittest.TestCase):
    def test_valid_input(self):
        """
        Testa um conjunto válido.
        """
        erros = validation("Carlos da Costa", "123.456.789-00", "carlos@email.com")
        self.assertEqual(erros, {})

    def test_nome_vazio(self):
        """
        Testa entrada nome em branco.
        """
        erros = validation("", "123.456.789-00", "carlos@email.com")
        self.assertIn("nome", erros)

    def test_nome_invalido_caracteres(self):
        """
        Testa entrada nome com números.
        """
        erros = validation("Carlos123", "123.456.789-00", "carlos@email.com")
        self.assertIn("nome", erros)

    def test_nome_curto(self):
        """
        Teste entrada nome com menos de 3 letras.
        """
        erros = validation("Ca", "123.456.789-00", "carlos@email.com")
        self.assertIn("nome", erros)

    def test_cpf_vazio(self):
        """
        Testa entrada cpf em branco.
        """
        erros = validation("carlos da Costa", "", "carlos@email.com")
        self.assertIn("cpf", erros)

    def test_cpf_invalido(self):
        """
        Testa entrada cpf com formato inválido.
        """
        erros = validation("Carlos da Costa", "123456", "carlos@email.com")
        self.assertIn("cpf", erros)

    def test_email_vazio(self):
        """
        Teste entrada email em branco.
        """
        erros = validation("Carlos da Costa", "123.456.789-00", "")
        self.assertIn("email", erros)

    def test_email_invalido(self):
        """
        Testa entrada email com formato inválido.
        """
        erros = validation("Carlos da Costa", "123.456.789-00", "carlos#email")
        self.assertIn("email", erros)

    def test_multiplos_erros(self):
        """
        Testa com todos os campos inválidos.
        """
        erros = validation("", "abc", "email@")
        self.assertIn("nome", erros)
        self.assertIn("cpf", erros)
        self.assertIn("email", erros)

if __name__ == '__main__':
    unittest.main()
