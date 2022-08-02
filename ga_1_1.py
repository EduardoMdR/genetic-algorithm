# Inicio do algoritmo genético

# ideia de implementação
# Passo 1: Crio uma população inicial randômica (100)
# Passo 2: verifico o fitness de cada indivíduo
# Passo 3: Seleciono dois pais (roleta) e gero dois filhos
# Passo 4: Aplico crossover (se taxa_cro = verdade)
# Passo 5: Aplico mutação (se taxa_mut = verdade)
#          Faço isso 50 vezes para completar minha população
# Passo 6: Repito esse processo até completar todas as gerações
# Passo 7: Passar o resultado para um arquivo .txt
# Fim: vou ter o indivíduo melhor qualificado (da última geração) como minha resposta


# bibliotecas
import numpy as np
# import math


# Variáveis globais estáticas
cromossomos = 44
populacao = 6       # 100
geracoes = 4        # 40
taxa_mut = 0.008
taxa_cro = 0.65
verbose = 0         # variavel utizada para debugar (funciona em escala pequena)
constante_normalizacao = 0.0000476837278899989


# Funções
def escolheFilho(pai, populacao, fitness):
  # print("Fitness do pai escolhido: ", pai)
  aux_roleta = 0
  for index in range(populacao):
    aux_roleta += int(fitness[index])
    if(pai <= aux_roleta):
      pai = geracao_atual[index]
      break
  
  return pai

def mutacaoGene(pai, taxa_mut, cromossomos):
  for index in range(cromossomos):
    mutacao = np.random.randint(1000)
    if(mutacao <= (taxa_mut*1000)):
      pai[index] = (np.random.randint(2))
      if(verbose): print('Aconteceu mutação em pai('') : ', index+1)
  return pai

# def main(args):
print("Algoritmo genético 1-1")


# Passo 1:
geracao_atual = []
nova_geracao = []
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


for i in range(int(populacao/2)):
  if(verbose): print(i+1,'º pais a serem escolhidos')
  # pai_x = []
  # Passo 3:
  pai_x = escolheFilho(np.random.randint(low=1, high=roleta), populacao, fitness)
  pai_y = escolheFilho(np.random.randint(low=1, high=roleta), populacao, fitness)

  if(verbose):
    print('Pai X escolhido: ', pai_x)
    print('Pai Y escolhido: ', pai_y)


  # Passo 4 (Preciso melhorar)
  # posso utilizar um randomizador para determinar o ponto de crossover
  crossover = np.random.randint(100)
  copia_pai_x, copia_pai_y = [], []

  if(crossover <= (taxa_cro*100)):
    # print('Aconteceu crossover')
    copia_pai_x = np.array_split(pai_x,2)
    copia_pai_y = np.array_split(pai_y,2)

    pai_x = np.concatenate((copia_pai_x[0], copia_pai_y[1]), axis=None)
    pai_y = np.concatenate((copia_pai_x[1], copia_pai_y[0]), axis=None)

  if(verbose):
    if(crossover < (taxa_cro*100)): print('Houve crossover')
    print('Pai X pós crossover: ', pai_x)
    print('Pai Y pós crossover: ', pai_y)


  # Passo 5
  pai_x = mutacaoGene(pai_x, taxa_mut, cromossomos)
  pai_y = mutacaoGene(pai_y, taxa_mut, cromossomos)


  if(verbose):
    print('pai_x final: ', pai_x)
    print('pai_y final: ', pai_y)

  nova_geracao.append(pai_x)
  nova_geracao.append(pai_y)

if(verbose): print(nova_geracao)

# Realizar o procedimento anterior len(populacao) vezes