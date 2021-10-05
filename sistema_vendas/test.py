import unittest
from calc_comissao import calcular_comissao

class test_calc_comissao(unittest.TestCase):
	def teste_venda_500_comissao_25(self):
		#Arrange
		venda = 500
		esperado = 25
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)


	def teste_venda_9999_comissao_499_95(self):
		#Arrange
		venda = 9999
		esperado = 499.95
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)


	def teste_venda_1_comissao_0_05(self):
		#Arrange
		venda = 1
		esperado = 0.05
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)


	def teste_venda_10000_comissao_600(self):
		#Arrange
		venda = 10000
		esperado = 600
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)


	def teste_venda_99952_25_comissao_600(self):
		#Arrange
		venda = 99952.25
		esperado = 5997.13
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)


	def teste_venda_101_16_comissao_5_05(self):
		#Arrange
		venda = 101.16
		esperado = 5.05
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)

	def teste_venda_3_99_comissao_5_05(self):
		#Arrange
		venda = 3.99
		esperado = 0.19
		#Act
		resultado = calcular_comissao(venda)
		#Assert
		self.assertEqual(esperado, resultado)


# python -m unittest discover . test.py
