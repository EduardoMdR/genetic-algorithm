# genetic-algorithm 3-1 até 3-3


#### ideia do algoritmo 3.1 (Operadores Independentes)

> Peso(probabilidade) dos operadores: 0,7 crossover de um ponto; 0,3 de mutação

#### ideia do algoritmo 3.2 (Crossover Uniforme)

> Operadores: <b>crossover uniforme</b>

#### ideia do algoritmo 2.3 (Interpolação de Peso de Operador)

> Técnica de parametrização: interpola peso do operador de 0,7 e 0,3 (crossover e mutação respectivamente), até 0,5 e 0,5 (a cada rodada ocorre variação de 0,005 em cada operador)


## implementação final

#### Módulo de avaliação: F6 Binária
#### Módulo de população:
- Técnica de representação: Representação binária 44bits
- Técnica de inicialização: Randômica
- Técnica de eliminação: Elimina os <b>N últimos</b>
- Reprodução: Substitui a geração <b>sem duplicatas</b>
- Seleção de pais: Roleta
- Fitness (grau de adaptação): ajuste é avaliação <b>Normalização linear 100 a 1 de 1 em 1</b>

> Populaçao inicial: 100 elementos; Total de gerações: 40

#### Módulo de reprodução:
- Seleção do operador: Roleta
- Operadores: Crossover Uniforme e mutação
- Taxa de mutação: 0,04
- Técnica de parametrização: 0,7 e 0,3 (até 0,5 e 0,5)
- Peso dos operadores: crossover = 0,7 e mutação = 0,3


## Resultados obtidos
