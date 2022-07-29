# Inicio do algoritmo genético

# ideia de implementação
# Passo 1: Crio uma população inicial randômica (100)
# Passo 2: verifico o fitness de cada indivíduo
# Passo 3: Seleciono dois pais (roleta) e gero dois filhos
# Passo 4: Aplico crossover (se taxa_cro = verdade)
# Passo 5: Aplico mutação (se taxa_mut = verdade)
# Passo 6: Repito esse processo até completar todas as gerações
# Fim: vou ter o indivíduo melhor qualificado como minha resposta

# bibliotecas
import numpy as np

# Variáveis globais estáticas
cromossomos = 44
populacao = 100
geracoes = 40
taxa_mut = 0.008
taxa_cro = 0.65

# def main(args):
print("Algoritmo genético 1-1")

# Passo 1:
geracao_atual = [populacao]

for filho in range(populacao):
  # geracao_atual[filho] = np.random.randint(2, size=cromossomos)
  # print(geracao_atual[filho])
