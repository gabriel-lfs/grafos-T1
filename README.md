# Trabalho 01 Teoria dos Grafos

### Passos para rodar o projeto:

São necessários para rodar o projeto, os seguintes pacotes:

[Python na versão 3.8](https://www.python.org/downloads/)

[pip3](https://pip.pypa.io/en/stable/installing/)

[make](https://www.gnu.org/software/make/)

para rodar o projeto basta executar o seguinte comando:

`make run`

### QUESTÃO 1
Explique rapidamente cada uma das estratégias abaixo, destacando a escolha do vértice da fronteira, como ela se comporta e qual é o desempenho do algoritmo ao realizar a busca por um objetivo:
- Busca em profundidade
- Busca em largura (ou extensão)
- Busca por custo uniforme (menor primeiro)
- Busca em aprofundamento iterativo 
- Busca heurística gulosa (pelo melhor primeiro)
- Busca A*


### QUESTÃO 2
Segue  abaixo  as  funcionalidades  que  precisam  ser  implementadas  neste trabalho.  Ele  trabalhará apenas com grafos não-dirigidos
![imagem-questao2](https://raw.githubusercontent.com/gabriel-lfs/grafos-T1/master/resources/img-q1.png)

#### Entrada:
Sua  implementação  deve  ser  capaz  de  ler  um  grafo  de  um  arquivo  texto.  O  formato  do  grafo  no arquivo  será  o  seguinte.  A  primeira  linha  informa  o  número  de  vértices  do  grafo.  Cada  linha subsequente  informa  as  arestas.  Um  exemplo  de  um  grafo  e  seu  respectivo arquivo  texto pode  ser visto acima.

#### Saida
- Sua implementação deve ser capaz de gerar um arquivo texto com as seguintes informações sobre o grafo: número de vértices, número de arestas e sequência de grau.

- Representação  de  grafos.  Sua implementação  deve  ser  capaz  de  representar  grafos  utilizando tanto  uma  matriz  de  adjacência,  quanto  uma  lista  ou  vetor  de  adjacência.  O  usuário  poderá escolher a representação a ser utilizada.

- Busca em grafos: largura e profundidade. Sua implementação deve ser capaz de percorrer o grafo utilizando busca em largura e busca em profundidade. O vértice inicial será dado pelo usuário. A respectiva árvore de busca deve ser gerada assim como o nível de cada vértice na árvore (nível da  raiz  é  zero).  Estas  informações  devem  ser  armazenadas  em  um  arquivo.  Para  descrever  a árvore gerada, basta informar o pai de cada vértice e seu nível no arquivo de saída.

Considerando cada um dos grafos de entrada, responda às perguntas abaixo:

- Compare o desempenho em termos de memória utilizada pelas duas representações do grafo. Ou seja,  determine  a  quantidade  de  memória  (em  MB)  utilizada  pelo  seu  programa  quando  você representa o grafo utilizando uma matriz e lista de adjacência.

- Compare o desempenho em termos de tempo de execução das duas representações do grafo. Ou seja, determine o tempo necessário para executar dez buscas em largura em cada um dos casos (utilize diferentes vértices como ponto de partida da busca). Dica: obtenhao tempo do relógio da máquina no seu código antes de iniciar e depois de terminar a BFS.

- Você deve preparar uma (ou duas) tabela com os resultados obtidos onde as colunas representam as características e as linhas representam os diferentes grafos analisados.

![imagem-questao2-2](https://raw.githubusercontent.com/gabriel-lfs/grafos-T1/master/resources/img-q2.png)


### QUESTÃO 3

Considere o seguinte mapa.

![imagem-questao3](https://raw.githubusercontent.com/gabriel-lfs/grafos-T1/master/resources/img-q3.png)

Usando o algoritmo A* determine uma rota de A até R, usando as seguintes funções de custo g(n) = adistância entre cada cidade e h(n) = a distância em linha reta entre duas Cidades.

Implemente um programa que forneça o seguinte:

- Mostre a ordem em que os vértices serão expandidos/explorados.

- Mostre a árvore de busca que será produzida, mostrando a função de custo em cada vértice.

- Mostre o caminho/rota que será tomada e o custo total.