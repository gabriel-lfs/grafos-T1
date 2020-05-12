## Questao 1

- **Busca em profundidade:** Percorre todos os filhos de um vertice antes de ir para um vértice do mesmo nível, empilha todos os vértices, logo consegue descobrir até mesmo os que estão desconexos.

- **Busca em largura (ou extensão):** Busca em todos os vértices no mesmo nível que o dele, antes de se aprofundar no grafo, um uso comum comentado em aula foi o de uma arvore de inteligencia de uma IA.

- **Busca por custo uniforme (menor primeiro):** Sempre vai para o vertice de menor custo independente de aquele ser o menor caminho, é mais performático do que uma busca heuristica porém menos precisa, pois não necessáriamente vai encontrar o menor caminho
- **Busca em aprofundamento iterativo:** Junta a busca em largura e em profundidade tenta varios caminhos, sempre deixando um "custo" a ser batido para chegar até o destino
- **Busca heurística gulosa (pelo melhor primeiro):** Parecida com o custo uniforme porém com uma função heuristica baseada no destino como por exemplo a distância em linha reta entre os dois vertices para definir um caminho mais preciso.
- **Busca A\*:** A melhor estratégia dentre todas as citadas para enccontrar um destino, ela vai, de certeza encontrar o menor caminho, porém isso tem um custo. Ela vai expandindo sempre o menor custo da soma da distancia atual e da heuristica e o algoritimo só termina quando for achado o vertice destino e o mesmo tenha o menor custo na arvore de expansão inteira.


## Questão 2

Foi utilizado o arquivo `teste1.txt` dentro da pasta `../arquivos-teste` e os arquivos de resultado estão dentro do zip `tests.zip`

|**Tópicos/Execuções** |**Primeira**   |**Segunda**     |
|----------------------|---------------|----------------|
|**Arquivo**           |teste1.txt     |teste1.txt      |
|**Memória matriz**    |8223.6015625 MB|8244.39453125 MB|
|**Memoria Lista**     |76.12109375 MB |129.0234375 MB  |
|**Busca**             |DFS            |BFS             |
|**T1 - Vertice 5**    |333182 ms      |855187 ms       |
|**T2 -Vértice 665**   |665126 ms      |833843 ms       |
|**T3 -Vértice 667**   |350085 ms      |867696 ms       |
|**T4 - Vertice 8**    |326430 ms      |850797 ms       |
|**T5 -Vértice 9986**  |342735 ms      |837225 ms       |
|**T6 - Vértice 12321**|341512 ms      |839881 ms       |
|**T7 - vértice 9899** |348966 ms      |846293 ms       |
|**T8 - vértice 32212**|340620 ms      |861421 ms       |
|**T9 - vértice 999**  |336310 ms      |839024 ms       |
|**T10 - vértice 666** |340616 ms      |842870 ms       |
