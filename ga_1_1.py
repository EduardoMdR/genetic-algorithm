# Inicio do algoritmo genético

# ideia de implementação
# Passo 1: Crio uma população inicial randômica (100)
# Passo 2: verifico o fitness de cada indivíduo
# Passo 3: Seleciono dois pais (roleta) e gero dois filhos
# Passo 4: Aplico crossover (se taxa_cro = verdade)
# Passo 5: Aplico mutação (se taxa_mut = verdade)
#          Faço isso 50 vezes para completar minha população
# Passo 6: Repito esse processo até completar todas as gerações
# Passo 7: Passar o resultado para um arquivo .txt (e imprimir mais coisas lá par facilitar o debug)
# Fim: vou ter o indivíduo melhor qualificado (da última geração) como minha resposta


# bibliotecas
import numpy as np
# import math


# Variáveis globais estáticas
cromossomos = 44
populacao = 4       # 100
geracoes = 4        # 40
taxa_mut = 0.008
taxa_cro = 0.65
verbose = 0         # variavel utizada para debugar (funciona em escala pequena)
constante_normalizacao = 0.0000476837278899989


# Funções
# Recebo um valor (min=1, max=roleta), e retorno qual o pai (e seu id) referente à essa número
def escolheFilho(pai, populacao, fitness):
  # print("Fitness do pai escolhido: ", pai)
  aux_roleta = 0
  for index in range(populacao):
    aux_roleta += int(fitness[index])
    if(pai <= aux_roleta):
      pai = geracao_atual[index]
      break
  
  return pai, index

def mutacaoGene(pai, taxa_mut, cromossomos):
  for index in range(cromossomos):
    mutacao = np.random.randint(1000)
    if(mutacao <= (taxa_mut*1000)):
      pai[index] = (np.random.randint(2))
      if(verbose): print('Aconteceu mutação em pai('') : ', index+1)
  return pai

# def main(args):
print("Algoritmo genético 1-1")
arquivoTxt = open('resposta.txt', 'w', encoding='utf-8')
arquivoTxt.write('Algoritmo genético 1-1 \n')
arquivoTxt.write('Inicio do algoritmo \n\n')

# Passo 1:
geracao_atual = []
for filho in range(populacao):
  geracao_atual.append(np.random.randint(2, size=cromossomos))


arquivoTxt.write('População inicial:\n')
index = 0
for x in geracao_atual:
  # repr() transforma variável em string
  index += 1
  arquivoTxt.write('filho '+ repr(index) + ':' + repr(x) + '\n')
arquivoTxt.write('\n')

# Montando as gerações
for i1 in range(geracoes):
  arquivoTxt.write(repr(i1+1) + 'º Geração\n')
  nova_geracao = []

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

  arquivoTxt.write('Fitness de cada filho: ' + repr(fitness) + '\n')
  arquivoTxt.write('Roleta: ' + repr(roleta) + '\n')

  arquivoTxt.write('\nInicio da reprodução: \n')
  # Percorrendo uma geração população/2 vezes
  for i2 in range(int(populacao/2)):
    arquivoTxt.write('\n' + repr(i2+1) + 'º pais a serem escolhidos: \n')

    # Passo 3:
    pai_x, pai_x_id = escolheFilho(np.random.randint(low=1, high=roleta), populacao, fitness)
    pai_y, pai_y_id = escolheFilho(np.random.randint(low=1, high=roleta), populacao, fitness)

    arquivoTxt.write('PaiX ('+ repr(pai_x_id+1) +') escolhido: ' + repr(pai_x) + '\n')
    arquivoTxt.write('PaiY ('+ repr(pai_y_id+1) +') escolhido: ' + repr(pai_y) + '\n')


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

  geracao_atual = nova_geracao
  if(verbose): print('Nova geração: ', nova_geracao)
  if(verbose): print('Nova geração: ', geracao_atual)

# Realizar o procedimento anterior len(populacao) vezes

arquivoTxt.close