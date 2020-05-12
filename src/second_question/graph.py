from collections import OrderedDict, deque
from datetime import datetime
from queue import Queue
from typing import Tuple, List

from src.milanceous import create_file_audit, get_memory_usage
from src.second_question import COLOR


class Graph:
    def __init__(self, vertexes):
        self.__vertexes = OrderedDict({vertex.title: vertex for vertex in vertexes})
        self.time = 0

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

    def adjacency_matrix(self):
        memory_usage, matrix = self.__adjacency_matrix()
        filename = create_file_audit('adjacency_matrix')

        with open(filename, 'w+') as f:
            f.write(f'Uso de memória: {memory_usage /1024 / 1024} MB\n\n')
            f.write('Matriz de adjacência:\n\n')
            [f.write(f'{line}\n') for line in matrix]

        print(f'\n\narquivo {filename} criado.')

    def adjacency_list(self):
        memory_usage, adjacency_list = self.__adjacency_list()

        filename = create_file_audit('adjacency_list')

        with open(filename, 'w+') as f:
            f.write(f'Uso de memória: {memory_usage / 1024 / 1024} MB\n\n')
            f.write('Lista de adjacência:\n\n')
            [f.write(f'{key} -> {value}') for key, value in adjacency_list.items()]

    def bfs(self, start_vertex=1):

        if not self.__vertexes.get(start_vertex):
            print("\n\nVértice inexistente.")
            return

        search_queue = Queue()

        self.__vertexes[start_vertex].discovery_time = 0

        search_queue.put(start_vertex)

        start_time = datetime.now()
        self.__bfs(search_queue)
        end_time = datetime.now()

        filename = create_file_audit('bfs')

        self.__create_search_file(start_time, end_time, filename)

    def dfs(self, start_vertex_title=1):
        start_vertex = self.__vertexes.get(start_vertex_title)

        if not start_vertex:
            print("\n\nVértice inexistente.")
            return

        start_time = datetime.now()

        self.__dfs(deque([*self.__vertexes.keys(), start_vertex_title]))

        end_time = datetime.now()

        filename = create_file_audit('dfs')

        self.__create_search_file(start_time, end_time, filename)

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
        return get_memory_usage(), {key: value.relation_titles for key, value in self.__vertexes.items()}

    def __create_search_file(self, start_time, end_time, filename):
        with open(filename, 'w+') as f:
            f.write(f'Começou às: {start_time} e terminou às: {end_time}\n\n')
            char_quantity = len(str(len(self.__vertexes)))
            for vertex in sorted(self.__vertexes.values(), key=lambda x: x.discovery_time):
                f.write(
                    f'vértice {str(vertex.title).zfill(char_quantity)} -> '
                    f'nível: {vertex.level} pai: {vertex.parent} '
                    f'tempo de descoberta: {vertex.discovery_time}\n'
                )

    def __bfs(self, search_queue):
        while not search_queue.empty():
            self.time = self.time + 1

            current_vertex = search_queue.get()

            if self.__vertexes[current_vertex].color == COLOR.WHITE:
                self.__vertexes[current_vertex].color = COLOR.GREY

                for relation in self.__vertexes[current_vertex].relation_titles:
                    if self.__vertexes[relation].color == COLOR.WHITE:
                        self.__vertexes[relation].discovery_time = self.time
                        self.__vertexes[relation].parent = self.__vertexes[current_vertex].title
                        self.__vertexes[relation].level = self.__vertexes[current_vertex].level + 1

                        search_queue.put(relation)

                self.__vertexes[current_vertex].color = COLOR.BLACK
                self.__vertexes[current_vertex].closing_time = self.time

    def __dfs(self, stack):
        self.time = 0
        while len(stack) > 0:

            title = stack.pop()
            self.time = self.time + 1

            if self.__vertexes[title].color == COLOR.WHITE:

                self.__vertexes[title].color = COLOR.GREY
                self.__vertexes[title].discovery_time = self.time

                for adjacency in self.__vertexes[title].relation_titles:
                    if self.__vertexes[adjacency].color == COLOR.WHITE:

                        self.__vertexes[adjacency].parent = title
                        self.__vertexes[adjacency].level = self.__vertexes[title].level + 1

                        stack.append(adjacency)

            if not next(iter(
                    child for child in self.__vertexes[title].relation_titles
                    if self.__vertexes[child].color == COLOR.WHITE
            ), None):
                self.__vertexes[title].color = COLOR.BLACK
                self.__vertexes[title].closing_time = self.time