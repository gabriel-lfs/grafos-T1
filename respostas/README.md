## Questao 1

- **Busca em profundidade:** Percorre todos os filhos de um vertice antes de ir para um vértice do mesmo nível, empilha todos os vértices, logo consegue descobrir até mesmo os que estão desconexos.

- **Busca em largura (ou extensão):** Busca em todos os vértices no mesmo nível que o dele, antes de se aprofundar no grafo, um uso comum comentado em aula foi o de uma arvore de inteligencia de uma IA.

- **Busca por custo uniforme (menor primeiro):** Sempre vai para o vertice de menor custo independente de aquele ser o menor caminho, é mais performático do que uma busca heuristica porém menos precisa, pois não necessáriamente vai encontrar o menor caminho
- **Busca em aprofundamento iterativo:** Junta a busca em largura e em profundidade tenta varios caminhos, sempre deixando um "custo" a ser batido para chegar até o destino
- **Busca heurística gulosa (pelo melhor primeiro):** Parecida com o custo uniforme porém com uma função heuristica baseada no destino como por exemplo a distância em linha reta entre os dois vertices para definir um caminho mais preciso.
- **Busca A\*:** A melhor estratégia dentre todas as citadas para enccontrar um destino, ela vai, de certeza encontrar o menor caminho, porém isso tem um custo. Ela vai expandindo sempre o menor custo da soma da distancia atual e da heuristica e o algoritimo só termina quando for achado o vertice destino e o mesmo tenha o menor custo na arvore de expansão inteira.


## Questão 2

Foi utilizado o arquivo `teste1.txt` dentro da pasta `../arquivos-teste` e os arquivos de resultado estão dentro do zip `tests.zip`

|Arquivo   |Memória matriz	|Memoria Lista |Busca|T1 - Vertice 5|T2 -Vértice 665|T3 -Vértice 667|T4 - Vertice 8|T5 -Vértice 9986|T6 - Vértice 12321|T7 - vértice 9899|T8 - vértice 32212|T9 - vértice 999|T10 - vértice 666|
|----------|----------------|--------------|-----|--------------|---------------|---------------|--------------|----------------|------------------|-----------------|------------------|----------------|-----------------|
|teste1.txt|8223.6015625 MB |76.12109375 MB|DFS  |333182 ms	    |665126 ms      |350085 ms      |326430 ms     |342735 ms       |341512 ms         |348966 ms        |340620 ms         |336310 ms       |340616 ms        |
|teste1.txt|8244.39453125 MB|129.0234375 MB|BFS  |855187 ms     |833843 ms      |867696 ms      |850797 ms     |837225 ms       |839881 ms         |846293 ms        |861421 ms         |839024 ms       |842870 ms        |


## Questão 3
        Arvore de busca:
        
          `-  A -> custo = 0 + (0 + 0) = 0
            |-  B -> custo = 182 + (0 + 73) = 255
           |   `-  K -> custo = 113 + (255 + 83) = 451
            |-  C -> custo = 179 + (0 + 64) = 243
           |   `-  I -> custo = 117 + (243 + 64) = 424
           |      |-  L -> custo = 100 + (424 + 28) = 552
           |     |   `-  P -> custo = 61 + (552 + 63) = 676
           |      `-  M -> custo = 97 + (424 + 20) = 541
           |         `-  O -> custo = 70 + (541 + 50) = 661
            |-  D -> custo = 165 + (0 + 89) = 254
           |   `-  N -> custo = 73 + (254 + 89) = 416
            `-  E -> custo = 166 + (0 + 104) = 270
               `-  J -> custo = 115 + (270 + 40) = 425
                  |-  N -> custo = 73 + (425 + 53) = 551
                  `-  Q -> custo = 61 + (425 + 80) = 566
                     `-  R -> custo = 0 + (566 + 65) = 631
         
        
         caminho percorrido:
         
        A -> custo = 0 + (0 + 0) = 0 
        E -> custo = 166 + (0 + 104) = 270 
        J -> custo = 115 + (270 + 40) = 425 
        Q -> custo = 61 + (425 + 80) = 566 
        R -> custo = 0 + (566 + 65) = 631  