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

### Normalização Linear: 
Com a normalização linear, a média da população tende a subir, o melhor indivíduo tende a ser menos inconstante que o GA1-1, já que os melhores indivíduos tem maiores chance de reproduzir que no GA1-1.

Se minha população começar a convergir para a solução ideal, quer dizer que vou ter indivíduos mais próximos de minha solução ideia (isso pode significar que tenho diversos indivíduos iguais ou bem semelhantes, o que explica o fato de mesmo sem elitismo, o melhor indivíduo se mantem)

Se eu tenho uma quantidade de indivíduos grande, a curva de melhor indivíduo acaba ficando mais constante (isso não é uma regra, mas normalmente ocorre) quanto maior esse número, menos variações ocorrem, mas elas ocorrem.

Se fizer a normalização menos significante (ex. de 999 até 900 de 1 em 1), o GA2-2 fica semelhante ao GA1-1

> população: 100, Gerações: 40
![image](https://user-images.githubusercontent.com/54919290/187817322-67b21af4-e996-4907-ad11-3f3a6b3155b3.png)
![image](https://user-images.githubusercontent.com/54919290/187817596-361b1762-94ab-49e0-8075-5f5089918d10.png)

> População: 100, Gerações: 80
![image](https://user-images.githubusercontent.com/54919290/187818191-7aae3ae2-3308-44d6-996e-586e3a1f1db5.png)
![image](https://user-images.githubusercontent.com/54919290/187818244-11899de7-0682-42a0-94cd-5203797d0810.png)

> População: 200, gerações: 40 e População: 500, gerações: 160
![image](https://user-images.githubusercontent.com/54919290/187819416-2d2ec14e-1e04-408a-a908-adf621286602.png)
![image](https://user-images.githubusercontent.com/54919290/187820033-c0edbdff-8fdc-4bcd-a971-c53b9dd0285c.png)

<hr />

### Elitismo:
Com o Elitismo a média da população aparenta estar subindo um pouco mais (em quase todos os casos rodados, as médias aparentam estar subindo um pouco mais, porém estabilizando em algum ponto)

Ao aumentar a quantidade de indivíduos, a média se assemelha do GA2-2
> População: 100, Gerações: 40
![image](https://user-images.githubusercontent.com/54919290/187820964-42fd6b9f-7c7a-4c69-ad53-6bfa86e3684a.png)

> População: 100, Gerações: 80 e 120
![image](https://user-images.githubusercontent.com/54919290/187821227-7812bd0a-3d26-4b7c-b34e-5fcadb9424c1.png)
![image](https://user-images.githubusercontent.com/54919290/187821325-8d311061-d357-488d-8032-76f282cc1610.png)

> População: 200, gerações: 40 e População: 500, gerações: 160
![image](https://user-images.githubusercontent.com/54919290/187821694-7e7cdcee-7dba-4a58-8da2-4755e3884573.png)
![image](https://user-images.githubusercontent.com/54919290/187822109-76de8ab3-b620-4e02-97be-692c66f7eeee.png)

<hr />

### N últimos:
Eliminando os N últimos, a média da população cresce em uma proporção quase constante, porém acabo ficando preso em um máximo local.

Quanto maior são os N_últimos_eliminados, mais rapido minha média vai convergir, porém agora em um máximo local, mais próximo do máximo global

> População: 100, gerações 40, e 120 e 180, n_eliminados: 6
![image](https://user-images.githubusercontent.com/54919290/187823791-2a231ce5-cbe6-4c70-96fe-e250b8eb5268.png)
![image](https://user-images.githubusercontent.com/54919290/187823982-afb10f90-3fa2-4cf9-8f81-388f10b21abc.png)
![image](https://user-images.githubusercontent.com/54919290/187824091-9b485152-1281-42d1-a354-364b01d25458.png)

> População: 100, gerações 120, n_eliminados: 20 e 40 e 60 e 90
![image](https://user-images.githubusercontent.com/54919290/187824379-0741a5fb-5301-4d3c-b79b-5f0480f77f76.png)
![image](https://user-images.githubusercontent.com/54919290/187824467-c22bfda4-fcbf-424e-8beb-3056708a357c.png)
![image](https://user-images.githubusercontent.com/54919290/187824507-ae7d4f7e-cced-442e-a08a-5629d15377e4.png)
![image](https://user-images.githubusercontent.com/54919290/187824606-3e9ef913-3a20-4ac4-abbb-033e2df360a4.png)

<hr />

