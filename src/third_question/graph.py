"""
Gabriel Luís Fernando de Souza
"""
from copy import deepcopy
from typing import Dict

from src.exceptions import VertexNotFoundError
from src.milanceous import create_file_audit


class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = []


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def __str__(self):
        return self.__pprint_tree(self.root)

    def __pprint_tree(self, node, _prefix="", _last=True):
        end_string = f'{_prefix} {"`- " if _last else "|- "} {node.value}\n'
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            end_string = f'{end_string}{self.__pprint_tree(child, _prefix, _last)}'
        return end_string


class AStarVertex:
    def __init__(self, title: str):
        self.title = title.upper()
        self.parent = None
        self.current_cost = 0
        self.heuristic_cost = 0
        self.relation_distances = {}

    def __str__(self):
        previous_cost = 0
        travel_cost = 0
        if self.parent:
            previous_cost = self.parent.current_cost
            travel_cost = self.parent.relation_distances[self.title]

        return (
            f'{self.title} -> '
            f'custo = {self.heuristic_cost} + ({previous_cost} + {travel_cost}) = {self.current_cost}'
        )


class AStarGraph:
    def __init__(self, vertexes):
        self.time = 0
        self.vertexes = vertexes
        self.tree: Tree

    def search(self, beginning_vertex, end_vertex, heuristic):
        self.tree = Tree(Node(self.vertexes[beginning_vertex]))

        found_vertex = self.__search(end_vertex, heuristic)
        item = found_vertex

        path = ''

        while item is not None:
            path = f'\n{item.value} {path}'
            item = item.parent

        output = f"Arvore de busca:\n\n{self.tree}\n\nCaminho percorrido:\n{path}"

        print(output)
        filename = create_file_audit('A_Star')

        open(filename, 'w+').write(output)

        print(f'\n\nArquivo {filename} criado.')

    def __search(self, end_vertex: str, heuristic: Dict[str, int]):
        previous_node = self.tree.root

        beginning_vertex: AStarVertex = previous_node.value
        beginning_vertex.level = 0
        beginning_vertex.discovery_time = 0

        explored_vertexes = [previous_node]
        while explored_vertexes:

            current_vertex = min(explored_vertexes, key=lambda x: x.value.current_cost)
            explored_vertexes.remove(current_vertex)

            if current_vertex.value.title == end_vertex.upper():
                return current_vertex

            for title, distance in current_vertex.value.relation_distances.items():
                vertex = deepcopy(self.vertexes[title])

                vertex.parent = current_vertex.value
                vertex.heuristic_cost = heuristic[title]
                vertex.current_cost = vertex.heuristic_cost + current_vertex.value.current_cost + distance
                vertex = Node(vertex)
                current_vertex.children.append(vertex)
                vertex.parent = current_vertex
                explored_vertexes.append(vertex)

        raise VertexNotFoundError
