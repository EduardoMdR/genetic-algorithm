# Inicio do algoritmo genético

# ideia de implementação
# Passo 1: Crio uma população inicial randômica (100)
# Passo 2: verifico o fitness de cada indivíduo
# Passo 3: Seleciono dois pais (roleta) e gero dois filhos
# Passo 4: Aplico crossover (se taxa_cro = verdade)
# Passo 5: Aplico mutação (se taxa_mut = verdade)
#          Faço isso 50 vezes para completar minha população
# Passo 6: Repito esse processo até completar todas as gerações
# Fim: vou ter o indivíduo melhor qualificado (da última geração) como minha resposta

# bibliotecas
import numpy as np
import math

# Variáveis globais estáticas
cromossomos = 44
populacao = 10      # 100
geracoes = 4        # 40
taxa_mut = 0.008
taxa_cro = 0.65
verbose = 0         # variavel utizada para debugar
constante_normalizacao = 0.0000476837278899989

# def main(args):
print("Algoritmo genético 1-1")

# Passo 1:
geracao_atual = []
for filho in range(populacao):
  geracao_atual.append(np.random.randint(2, size=cromossomos))

if(verbose):
  print("Geração incial da população: \n", geracao_atual)

# Passo 2:
roleta = 0
fitness = []
for filho in range(populacao):
  x = (geracao_atual[filho][:int(cromossomos/2)] * constante_normalizacao) - 100
  y = (geracao_atual[filho][int(cromossomos/2):] * constante_normalizacao) - 100
  # aux = math.pow(math.sin(math.pow(math.pow(x,2)+math.pow(y,2),0.5)),2)
  # aux2 = 1.0 + 0.001 * (math.pow(math.pow(x,2)+math.pow(y,2),2))
  # fitness.append(aux/aux2)
  aux = np.random.randint(low=1, high=5)
  fitness.append(aux)
  roleta += aux
  # Preciso arrimar a equação de fitness

if(verbose):
  print("Fitness de cada filho: \n", fitness)
  print("Roleta: ", roleta)

# Passo 3:
pai_x = np.random.randint(low=1, high=roleta)
pai_y = np.random.randint(low=1, high=roleta)
pai_atual = 0
while(pai_atual):
  

for index in range(populacao):
  # Realizar o procedimento anterior len(populacao) vezes