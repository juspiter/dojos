import math

def truncate(valor):
	return math.trunc(valor * 100) / 100

def calcular_comissao(valor):
	if valor < 10000:
		return truncate(valor * 0.05)
	return truncate(valor * 0.06)



# Venda < 10000: comissão 5%
# Venda >= 10000: comissão 6%