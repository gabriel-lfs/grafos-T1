from datetime import datetime
from enum import Enum
from milanceous import get_memory_usage


class COLOR(Enum):
    BLACK = 'black'
    GREY = 'grey'
    WHITE = 'white'


class Vertex:
    def __init__(self, title: str):
        self.title = title.upper()
        self.dfs_color = COLOR.WHITE
        self.dfs_discovery_time = -1
        self.dfs_closing_time = -1
        self.relations = []


class Graph:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.time = 0
        self.dfs_start_time = None
        self.dfs_end_time = None
        self.dfs_memory_usage = []
        self.dfs_current_level = 0

    def report(self):
        sequences = {int(i.title): len(i.relations) for i in self.vertexes}
        edges_amount = int(sum(sequences.values()) / 2)
        vertexes_amount = len(self.vertexes)

        with open(f'./report_{datetime.now().isoformat("_").replace(":", "").replace(".", "")}.txt', 'w+') as f:
            f.write(f'O grafo contém: {vertexes_amount} vértices com {edges_amount} arestas.\n\n')
            f.write('Sequências:\n')
            for name, amount in sequences.items():
                f.write(f'O vértice {name} contém um grau de {amount}.\n')

    def adjacency_matrix(self):
        for vertex in self.vertexes:
            pass

    def dfs(self):
        self.dfs_start_time = datetime.now()
        self.__dfs(self.vertexes)
        self.dfs_end_time = datetime.now()

    def __dfs(self, vertexes=None):
        dfs_memory_usage = []
        for vertex in vertexes or self.vertexes:
            self.time += 1

            if vertex.dfs_color == COLOR.WHITE:
                self.__dfs_visit(vertex)

            dfs_memory_usage.append(get_memory_usage())

    def __dfs_visit(self, vertex):
        vertex.dfs_color = COLOR.GREY
        self.time = self.time + 1
        vertex.dfs_discovery_time = self.time

        for adjacency in vertex.relations:
            if adjacency.dfs_color == COLOR.WHITE:
                self.__dfs(vertex.relations)

        vertex.dfs_color = COLOR.BLACK
        self.time = self.time + 1
        vertex.dfs_closing_time = self.time


def read_input_file():
    with open(input('Nome do arquivo de input: ')) as f:
        graph_size = int(f.readline())
        vertexes = {}
        for index in range(1, graph_size + 1):
            vertexes[index] = Vertex(title=str(index))

        for line in f:
            vertex, relation = line.strip('\n').split(' ')

            print(index)
            print(vertex)
            vertexes[int(vertex)].relations.append(vertexes[int(relation)])
            print(vertexes[int(vertex)].relations)
    return Graph(vertexes.values())


if __name__ == '__main__':
    graph = read_input_file()

    graph.report()
    graph.dfs()

    print('done')
