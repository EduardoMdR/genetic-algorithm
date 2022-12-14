import numpy as np
import math
import random

populacao = 4
cromossomos = 44
constante_normalizacao = 0.0000476837278899989
# constante_normalizacao = (200 / (math.pow(2,22) - 1))
geracao_atual = []

geracao_atual.append(np.random.randint(2, size=cromossomos))
x, y = '', ''

print(geracao_atual)
idx = 0

for i in (geracao_atual[0]):
  if(idx < int(cromossomos/2)): x += str(i)
  else: y += str(i)
  idx += 1

print('Valor de X: ', x)
print('Valor de Y: ', y)

x = (int(x, 2) * constante_normalizacao) - 100
y = (int(y, 2) * constante_normalizacao) - 100

print('Valor de X normalizado: ', x)
print('Valor de Y normalizado: ', y)

eq_aux, eq_aux2 = 0, 0
eq_aux = math.pow((math.pow(x,2) + math.pow(y,2)), 0.5)
eq_aux = (math.pow(math.sin(eq_aux),2) - 0.5)
eq_aux2 = 1.0 + (0.001 * (math.pow((math.pow(x,2) + math.pow(y,2)),2)))
fitness = (0.5 - (eq_aux/eq_aux2))
print('Fitness final', fitness)
print('Roleta: ',random.uniform(0.01,fitness))