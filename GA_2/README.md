# genetic-algorithm 2-1 até 2-5


#### ideia do algoritmo 2.1

> Técnica de Aptidão: Normalização Linear

#### ideia do algoritmo 2.2

> Técnica de Reprodução: substituição de todos <b>com elitismo</b>

#### ideia do algoritmo 2.3

> Técnica de Reprodução: elimina os N últimos

#### ideia do algoritmo 2.4

> Técnica de Reprodução: elimina os N últimos <b>sem duplicatas</b>

#### ideia do algoritmo 2.5

> Atualização das probabilidade dos operadores

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
- Seleção do operador: Primeiro operador
- Operadores: Crossover de um ponto com mutação
- Taxa de mutação: 0,04
- taxa de crossover: 0,80


## Resultados obtidos

Normalização Linear: 
Com a normalização linear, a média da população tende a subir, o melhor indivíduo tende a ser menos inconstante que o GA1-1, já que os melhores indivíduos tem maiores chance de reproduzir que no GA1-1

> população 100, Gerações 40
![image](https://user-images.githubusercontent.com/54919290/187817322-67b21af4-e996-4907-ad11-3f3a6b3155b3.png)
![image](https://user-images.githubusercontent.com/54919290/187817596-361b1762-94ab-49e0-8075-5f5089918d10.png)


<hr />
