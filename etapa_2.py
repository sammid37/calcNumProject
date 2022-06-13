#  Arquivo principal correspondente à 2ª etapa do Projeto Bola na Rede
# Equipe 3: Abraão, Élen, Eduardo, Felipe, Gabriel e Samantha

from math import sqrt
from matplotlib.pyplot import plot
from numpy import linspace

from random import choice
import json

# Escolhe um goleiro aleatoriamente
# Talvez não seja necessário
def escolher_goleiro(data):
    goleiro = choice(data)
    return goleiro

# plotagem é um valor booleano (True ou False) referente a plotagem do gráfico
def newton_cotes(plotagem):
    pass

# Massa e altura do goleiro
def trajetoria_goleiro(m,h):
    pass

f = open("json/goleiros.json")
data_goleiros = json.load(f)

# Escolhendo um goleiro
goleiro = escolher_goleiro(data_goleiros)
print(goleiro)

# Valores sobre as dimensões da trave
h_trave = 0
l_trave = 0

# Valores padrões do goleiro, para testes
h_goleiro = 1.88
m_goleiro = 80.58

# * Desenvolvimento do projeto a seguir


# fecha o arquivo
f.close()
