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

### Operadores Independentes: 
A ideia dos operadores independentes, é evitar que uma boa combinação feita por crossover se perca com a mutação, e vise-versa, os resultados são bem parecidos com o GA2-5 (Algumas vezes com n_ultimos, os resultados proximos de 1 não são obtidos, as vezes ficam muitos proximos, e outras um pouco mais longe, isso ocorre tanto no GA2-5, como nesse GA3-1, os resultados mostrados são uma amostra do obtidos, mas é IMPORTANTE deixar esse aviso).

Teoricamente não saberia dizer se era pra ser melhor que o GA2-5, ele propõe resolver uma problematica, mas acaba encobrindo ourta (que seria o fato de que um crossover junto com a mutação, poderia geral um indivíduo melhor, e selecionar um dos dois pode encobrir isso), na pratica os resultados obtidos são na maioria das vezes muitos semelhantes.

> População: 100, Gerações: 120 e 220, n_eliminados: 6
![image](https://user-images.githubusercontent.com/54919290/188049806-cf3874ec-03bf-4147-aa51-92e8c1307d23.png)
![image](https://user-images.githubusercontent.com/54919290/188049886-fca98291-6f00-490f-8176-2a2fd6cf3388.png)

> População: 100, gerações 120, n_eliminados: 20, 60, 90, 90 e 98
![image](https://user-images.githubusercontent.com/54919290/188050136-f385bc76-f6fb-406e-b966-0fa87818b2e6.png)
![image](https://user-images.githubusercontent.com/54919290/188050998-8c4f5d60-898c-4728-ad91-42126d09c25a.png)
![image](https://user-images.githubusercontent.com/54919290/188051092-bc00bfe9-8783-4af0-af72-101867bb8f7d.png)
![image](https://user-images.githubusercontent.com/54919290/188051297-40e14739-70e9-4c16-b3b5-f257bbe54f98.png)
![image](https://user-images.githubusercontent.com/54919290/188051477-4a299a90-f01d-4873-9bca-0ee1c32447a8.png)

<hr />

