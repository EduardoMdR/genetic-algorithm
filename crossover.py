import numpy as np
# import math

cromossomos = 44
geracao_atual = []

geracao_atual.append(np.random.randint(2, size=cromossomos))

print(geracao_atual)
aux = np.random.randint(low=1, high=cromossomos)
print(aux)
print(geracao_atual[0][:aux])
print(geracao_atual[0][aux:])