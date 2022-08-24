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


### bibliotecas ###
import numpy as np
import random
import math
import matplotlib.pyplot as plt


# Variáveis globais estáticas
cromossomos = 44            # tamanho dos cromossomos de cada indivíduo
populacao = 100             # Total de indívidios de uma geração
geracoes = 40               # Total de gerações
taxa_mut = 0.008            # Taxa que uma mutação acontece em algum gene (bit)
taxa_cro = 0.65             # Taxa que o crossover acontece na reprodução
constante_normalizacao = 0.0000476837278899989
# constante_normalizacao = (200 / (math.pow(2,22) - 1))


### Funções ###
# Recebo um valor (min=0, max=roleta), e retorno qual o pai (e seu id) referente à essa número
def escolheFilho(pai, populacao, fitness):
  aux_roleta = 0.0
  for index in range(populacao):
    aux_roleta += float(fitness[index])
    if(pai <= aux_roleta):
      pai = geracao_atual[index]
      break
  return pai, index

# Verifica para cada bit, se vai ou não aconecer uma mutação
def mutacaoGene(pai, qualPai, taxa_mut, cromossomos):
  aux_pai = []
  for index in range(cromossomos):
    mutacao = np.random.randint(1000)
    if(mutacao <= (taxa_mut*1000)):
      if str(pai[index]) == '0': aux_pai.append(np.int32(1))
      else: aux_pai.append(np.int32(1))
      arquivoTxt.write('Aconteceu mutação em pai(' + repr(qualPai) + ') : '+ repr(index+1) + '\n')
    else:
      aux_pai.append(pai[index])

  return np.int32(aux_pai)

# Salva valores para plotar no gráfico
def imprimirGrafico(fitness):
  melhor = fitness[0]
  for index in range(len(fitness)):
    if(melhor < fitness[index]): melhor = fitness[index]

  return melhor

# Recebe os fitness da gerações e retorna o pior e o melhor elemento
def encontrarMelhorEPior(geracoes, melhor_filho):
  melhor_geracao, pior_geracao = melhor_filho[0], melhor_filho[0]
  melhor, pior = 0, 0

  for index in range(geracoes):
    if melhor_geracao <= melhor_filho[index]: 
      melhor_geracao = melhor_filho[index]
      melhor = index
    if pior_geracao >= melhor_filho[index]:
      pior_geracao = melhor_filho[index]
      pior = index

  return melhor, pior

# Recebe uma geração e retorna o fitness de cada individuo
def funcaoAptidao(populacao, cromossomos, geracao_atual):
  roleta = 0
  fitness = []
  filho = 0

  for filho in range(populacao):
    x, y = 0.0, 0.0
    aux_x, aux_y = '', ''
    aux_idx = 0
    for i in (geracao_atual[filho]):
      if(aux_idx < int(cromossomos/2)): aux_x += str(i)
      else: aux_y += str(i)
      aux_idx += 1

    x = (int(aux_x, 2) * constante_normalizacao) - 100.0
    y = (int(aux_y, 2) * constante_normalizacao) - 100.0

    eq_aux, eq_aux2 = 0.0, 0.0
    eq_aux = math.pow((math.pow(x,2) + math.pow(y,2)), 0.5)
    eq_aux = math.pow(math.sin(eq_aux),2) - 0.5
    eq_aux2 = math.pow(1.0 + (0.001 * (math.pow(x,2) + math.pow(y,2))),2)
    fitness.append((0.5 - (eq_aux/eq_aux2)))
    roleta += (0.5 - (eq_aux/eq_aux2))
  
  return fitness, roleta

### def main(args): ###
print("Algoritmo genético 1-1")
arquivoTxt = open('resposta.txt', 'w', encoding='utf-8')
arquivoTxt.write('Algoritmo genético 1-1 \n')
arquivoTxt.write('Inicio do algoritmo \n\n')


# Passo 1:
geracao_atual = []
melhor_filho = []
media = []
for filho in range(populacao):
  geracao_atual.append(np.random.randint(2, size=cromossomos))

arquivoTxt.write('População inicial:\n')
index = 0
for x in geracao_atual:
  # repr() transforma variável em string
  index += 1
  arquivoTxt.write('filho '+ repr(index) + ': ' + repr(x) + '\n')
arquivoTxt.write('\n')

# Montando as gerações
for i1 in range(geracoes):
  arquivoTxt.write('\n\n\n#################### ' + repr(i1+1) + 'º Geração ####################\n')
  nova_geracao = []


  # Passo 2:
  fitness, roleta = funcaoAptidao(populacao, cromossomos, geracao_atual)
  
  media.append(roleta / populacao)
  arquivoTxt.write('Fitness de cada filho: ' + repr(fitness) + '\n')
  melhor_filho.append(imprimirGrafico(fitness))
  arquivoTxt.write('Média da população:' + str(media[i1]) + '\n')
  arquivoTxt.write('Melhor filho da população:' + str(melhor_filho[i1]) + '\n\n\n')

  arquivoTxt.write('Roleta: ' + repr(roleta) + '\n')
  arquivoTxt.write('Inicio da reprodução: \n')
  # Percorrendo uma geração população/2 vezes
  for i2 in range(int(populacao/2)):
    arquivoTxt.write('\n' + repr(i2+1) + 'º pais a serem escolhidos: \n')


    # Passo 3:
    pai_x, pai_x_id = escolheFilho(random.uniform(0.01,roleta), populacao, fitness)
    pai_y, pai_y_id = escolheFilho(random.uniform(0.01,roleta), populacao, fitness)

    arquivoTxt.write('PaiX ('+ repr(pai_x_id+1) +') escolhido: ' + repr(pai_x) + '\n')
    arquivoTxt.write('PaiY ('+ repr(pai_y_id+1) +') escolhido: ' + repr(pai_y) + '\n')


    # Passo 4
    crossover = np.random.randint(100)
    if(crossover <= (taxa_cro*100)):
      qtd_cro = np.random.randint(low=1, high=cromossomos)      # O local que vai acontecer o crossover
      
      pai_x = np.concatenate((pai_x[:qtd_cro], pai_y[qtd_cro:]), axis=None)
      pai_y = np.concatenate((pai_x[qtd_cro:], pai_y[:qtd_cro]), axis=None)

      arquivoTxt.write('Houve crossover (no cormossomo ' + str(qtd_cro) + ')\n')
    else:
      arquivoTxt.write('Não houve crossover\n')


    # Passo 5
    pai_x = mutacaoGene(pai_x, 'X', taxa_mut, cromossomos)
    pai_y = mutacaoGene(pai_y, 'Y', taxa_mut, cromossomos)
    arquivoTxt.write('\n')
    arquivoTxt.write('Filho 1 final: '+ repr(pai_x) + '\n')
    arquivoTxt.write('Filho 2 final: '+ repr(pai_y) + '\n')

    nova_geracao.append(pai_x)
    nova_geracao.append(pai_y)

  geracao_atual = nova_geracao

# Verificando qual é o melhor filho da última geração
escolhido_id = fitness[0]
for index in range(populacao):
  if(escolhido_id < fitness[index]): escolhido_id = fitness[index]

arquivoTxt.write('\n\n\nMelhores individuos de cada geração:' + str(melhor_filho) + '\n\n')
escolhido = escolheFilho(escolhido_id, populacao, fitness)
arquivoTxt.write('Individuo mais qualificado (última geração): '+ repr(escolhido) + '\n')

# Verificando qual é o melhor e o pior fitness de todas as gerações
melhor, pior = 0, 0
melhor, pior = encontrarMelhorEPior(geracoes, melhor_filho)

melhor_media, pior_media = 0, 0
melhor_media, pior_media = encontrarMelhorEPior(geracoes, media)


arquivoTxt.write('Melhor geração: '+ repr(melhor + 1) + '\n')
arquivoTxt.write('Pior geração: '+ repr(pior + 1) + '\n')
arquivoTxt.close


# Mostrando resultado em grafico
qtdGeracoes = []
for index in range(geracoes):
  qtdGeracoes.append(str(index+1))

plt.figure(figsize=(12,6))
# - 1º Melhor indivíduo de cada geração
# Plotar todas as gerações, seu melhor e pior indivídio
plt.plot(qtdGeracoes, melhor_filho, label='Melhor indivíduo da população')         
plt.plot(qtdGeracoes[melhor], melhor_filho[melhor], 'bo', label='Melhor/Pior indivíduo')
plt.plot(qtdGeracoes[pior], melhor_filho[pior], 'bo')

# - 2º Média de todos os indivíduos de cada geração
# Plotar média de todas as gerações, melhor e pior geração
plt.plot(qtdGeracoes, media, color='#f4d03f', label='Média da população')                 
plt.plot(qtdGeracoes[melhor_media], media[melhor_media], 'ro', label='Melhor/Pior população')
plt.plot(qtdGeracoes[pior_media], media[pior_media], 'ro')

plt.ylabel("Fitness", size = 16)
plt.xlabel("Gerações", size = 16)
plt.title("Melhores individuos de cada geração", fontdict={'weight': 'bold','size': 18})
plt.legend()
plt.grid(True)
plt.savefig('ga_1_1.png')

# - 3º Média dos N melhores indivíduos da geração
# - 4º Média dos N Piores indivíduos da geração