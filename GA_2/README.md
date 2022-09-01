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

Se minha população começar a convergir para a solução ideal, quer dizer que vou ter indivíduos mais proximos de minha solução ideia (isso pode significar que tenho diversos indivíduos iguais ou bem semelhantes, o que explica o fato de mesmo sem elitismo, o melhor indivíduo se mantem)

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
