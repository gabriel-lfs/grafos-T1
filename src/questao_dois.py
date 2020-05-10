import sys
from collections import OrderedDict, deque
from copy import deepcopy
from datetime import datetime
from enum import Enum
from typing import List, Tuple

from src.milanceous import get_memory_usage, create_file_audit


class COLOR(Enum):
    BLACK = 'black'
    GREY = 'grey'
    WHITE = 'white'


class Vertex:
    def __init__(self, title: int):
        self.title = title
        self.dfs_color = COLOR.WHITE
        self.dfs_discovery_time = -1
        self.dfs_closing_time = -1
        self.dfs_parent = None
        self.dfs_level = 0
        self.__relation_titles = set()

    @property
    def relation_titles(self):
        return self.__relation_titles

    @relation_titles.setter
    def relation_titles(self, relation):
        self.__relation_titles.add(relation.title)


class Graph:
    def __init__(self, vertexes):
        self.__vertexes = OrderedDict({vertex.title: vertex for vertex in vertexes})
        self.time = 0
        self.dfs_start_time = None
        self.dfs_end_time = None
        self.dfs_queue = []

    def report(self):
        sequences = {title: len(item.relation_titles) for title, item in self.__vertexes.items()}
        edges_amount = int(sum(sequences.values()) / 2)
        vertexes_amount = len(self.__vertexes)

        filename = create_file_audit('report')
        with open(filename, 'w+') as f:
            f.write(f'O grafo contém: {vertexes_amount} vértices com {edges_amount} arestas.\n\n')
            f.write('Sequências:\n')
            for name, amount in sequences.items():
                f.write(f'O vértice {name} contém um grau de {amount}.\n')

        print(f'\n\narquivo {filename} criado.')

    def __adjacency_matrix(self) -> Tuple[int, List[List[int]]]:
        matrix = []
        start_time = datetime.now().time()
        for vertex in self.__vertexes.values():
            line = [0 for _ in range(len(self.__vertexes))]
            relations = vertex.relation_titles

            for index in relations:
                line[index - 1] = 1

            matrix.append(line)

        end_time = datetime.now()

        print(f'\nComeçou às: {start_time} e terminou às: {end_time}')
        return get_memory_usage(), matrix

    def __adjacency_list(self):
        pass

    def adjacency_matrix(self):
        memory_usage, matrix = self.__adjacency_matrix()
        filename = create_file_audit('adjacency-matrix')

        with open(filename, 'w+') as f:
            f.write('matriz de adjacência:\n\n')
            [f.write(f'{line}\n') for line in matrix]
            f.write(f'\n\no uso de memória foi de: {memory_usage /1024 / 1024} MB')

        print(f'arquivo {filename} criado.')

    def dfs(self, start_vertex_title=1):
        start_vertex = self.__vertexes.get(start_vertex_title)

        if not start_vertex:
            print("\n\nVértice inexistente.")
            return

        self.dfs_start_time = datetime.now()

        self.__dfs(deque([*self.__vertexes.keys(), start_vertex_title]))

        self.dfs_end_time = datetime.now()

        filename = create_file_audit('dfs')

        with open(filename, 'w+') as f:
            f.write(f'Começou às: {self.dfs_start_time} e terminou às: {self.dfs_end_time}\n\n')
            char_quantity = len(str(len(self.__vertexes)))
            for vertex in sorted(self.__vertexes.values(), key=lambda x: x.dfs_discovery_time):
                f.write(
                    f'vértice {str(vertex.title).zfill(char_quantity)} -> '
                    f'nível: {vertex.dfs_level} pai: {vertex.dfs_parent} '
                    f'tempo de descoberta: {vertex.dfs_discovery_time}\n'
                )

    def __dfs(self, stack):
        self.time = 0
        while len(stack) > 0:

            title = stack.pop()
            self.time = self.time + 1

            if self.__vertexes[title].dfs_color == COLOR.WHITE:

                self.__vertexes[title].dfs_color = COLOR.GREY
                self.__vertexes[title].dfs_discovery_time = self.time

                for adjacency in self.__vertexes[title].relation_titles:
                    if self.__vertexes[adjacency].dfs_color == COLOR.WHITE:

                        self.__vertexes[adjacency].dfs_parent = title
                        self.__vertexes[adjacency].dfs_level = self.__vertexes[title].dfs_level + 1

                        stack.append(adjacency)

            if not next(iter(
                    child for child in self.__vertexes[title].relation_titles
                    if self.__vertexes[child].dfs_color == COLOR.WHITE
            ), None):
                self.__vertexes[title].dfs_color = COLOR.BLACK
                self.__vertexes[title].dfs_closing_time = self.time

    def bfs(self):
        pass


def read_input_file():
    with open(input('Nome do arquivo de input: ')) as f:
        graph_size = int(f.readline())
        vertexes = {}
        for index in range(1, graph_size + 1):
            vertexes[index] = Vertex(title=index)

        for line in f:
            vertex, relation = line.strip('\n').split(' ')
            vertexes[int(vertex)].relation_titles = vertexes[int(relation)]
            vertexes[int(relation)].relation_titles = vertexes[int(vertex)]

    return Graph(vertexes.values())


def input_dfs():
    imputed_vertex = input('\n\nDe qual vértice que você quer inciar a busca?')
    current_graph.dfs(int(imputed_vertex))


if __name__ == '__main__':
    graph = read_input_file()
    while True:
        current_graph = deepcopy(graph)
        options = {
            '1': ('Relatório', current_graph.report),
            '2': ('Matriz de adjacência', current_graph.adjacency_matrix),
            '3': ('DFS', input_dfs),
            '4': ('BFS', current_graph.bfs),
            '9': ('Sair', sys.exit)
        }

        prompt = "\n".join(f'{key} - {value[0]}' for key, value in options.items())

        imputed_option = input(
            f"\n\nSelecione o número da opção desejada:\n{prompt}"
        )

        selected_option = options.get(imputed_option)

        if selected_option:
            selected_option[1]()
            continue

        print("\n\nOpção invalida... Tente novamente!")

    print('Shall it never reach here!!!')
