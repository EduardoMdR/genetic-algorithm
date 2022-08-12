# genetic-algorithm

### Rodar o programa

> Preciso ter instalado a biblioteca Matplotlib
``` pip install matplotlib ```

> Preciso do python
``` py .\ga_1_1.py ```

<br />

## ideia do algoritmo 1.1 (John Holland)

- Técnica de representação: Representação binária 44bits
- Tecnica de inicialização: randômica
- Eliminação: elimina todos
- Reprodução: Substitui a geração
- Seleção de pais: Roleta
- Fitness (grau de adaptação): ajuste é avaliação

> Populaçao inicial: 100 elementos; Total de gerações: 40

Módulo de reprodução:
- Seleção do operador: Primeiro operador
- Operadores: Crossover de um ponto com mutação
- Taxa de mutação: 0,008
- taxa de crossover: 0,65

<br />

## ideia do algoritmo 2.2

- Técnica de representação: Representação binária 44bits
- Tecnica de inicialização: randômica
- Eliminação: elimina todos
- Reprodução: Substitui a geração ><b>com elitismo</b><
- Seleção de pais: Roleta
- Fitness (grau de adaptação): ajuste é avaliação ><b>Normalização linear 100 a 1 de 1 em 1</b><

> Populaçao inicial: 100 elementos; Total de gerações: 40

Módulo de reprodução:
- Seleção do operador: Primeiro operador
- Operadores: Crossover de um ponto com mutação
- Taxa de mutação: 0,008
- taxa de crossover: 0,65

