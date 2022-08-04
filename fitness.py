import numpy as np

populacao = 4
cromossomos = 44
constante_normalizacao = 0.0000476837278899989
geracao_atual = []

geracao_atual.append(np.random.randint(2, size=cromossomos))

roleta = 0
fitness = []
aux = ''
x, y = '', ''

print(geracao_atual)
idx = 0

for i in (geracao_atual[0]):
  if(idx < int(cromossomos/2)): x += str(i)
  else: y += str(i)
  idx += 1

print('Valor ed X: ', x)
print('Valor ed Y: ',y)

# print(aux)
x = (int(x, 2) * constante_normalizacao) - 100
y = (int(y, 2) * constante_normalizacao) - 100

print('Valor ed X: ', x)
print('Valor ed Y: ',y)