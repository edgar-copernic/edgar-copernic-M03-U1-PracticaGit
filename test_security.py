import unittest
from security import validar_password

class TestValidarPassword(unittest.TestCase):
	def test_password_curta(self):
		self.assertFalse(validar_password("abc"))


	def test_password_correcta(self):
		self.assertTrue(validar_password("contrasenyallarga"))

if __name__ == "__main__":
	unittest.main()
