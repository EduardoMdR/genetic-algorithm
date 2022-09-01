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

### N últimos sem duplicatas:
Tenho um resultado melhor que o GA2-3, porém demora muito para chegar em uma máximo local, e quando chego não saio dele.

Ao aumentar os n eliminados, não tenho um bom aproveitamento do algoritmo, pois suas taxas de mutação e crossover não estão adaptadas para as novas funcionalidades

> População: 100, Gerações: 260 e 300, n_eliminados: 6
![image](https://user-images.githubusercontent.com/54919290/187825121-aeaf556a-f42d-4f0b-9f26-43e0cab7f5f2.png)
![image](https://user-images.githubusercontent.com/54919290/187825213-16fb793d-1034-4868-8fd5-b7ed6ac209a6.png)

> População: 100, gerações 120, n_eliminados: 40 e 90
![image](https://user-images.githubusercontent.com/54919290/187825507-ec9c7eac-a8a4-4397-a5f0-93fa08261332.png)
![image](https://user-images.githubusercontent.com/54919290/187825566-79539910-8c50-45b8-a007-5017d56cf0a3.png)

<hr />

### Arrumando taxas de mutação e crossover:
Como a reprodução acontece em uma taxa menor, precisamos aumentar a taxa de mutação e crossover para conseguirmos aconpanhar o algoritmo sem ter que passar muitas gerações.

Aumentando os n_ultimos é possivel encontrar o melhor resultado obtido mais cedo

> População: 100, Gerações: 120 e 220, n_eliminados: 6
![image](https://user-images.githubusercontent.com/54919290/187826163-6fce2fd2-1524-4d42-b0a8-ce3067e4801d.png)
![image](https://user-images.githubusercontent.com/54919290/187826254-b1d4a7b3-0e05-431e-af8e-109c5f967391.png)

> População: 100, gerações 120, n_eliminados: 20, 60, 60 e 90
![image](https://user-images.githubusercontent.com/54919290/187826468-68ad7d86-1fc4-4e2d-a4e1-8571c9d78ccb.png)
![image](https://user-images.githubusercontent.com/54919290/187826559-2b066bf6-8583-416b-bcf0-c201f65fe135.png)
![image](https://user-images.githubusercontent.com/54919290/187826653-15077092-89bc-4cb5-af77-71534bf5115b.png)
![image](https://user-images.githubusercontent.com/54919290/187826705-77d71ccc-6863-410c-8e5a-82e8cf09d8c3.png)

