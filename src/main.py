"""
Gabriel Luís Fernando de Souza
"""

import sys
from copy import deepcopy

from src.mocks import mocked_first_question, mocked_heuristic_cost_file, mocked_relation_file
from src.second_question.graph import Graph
from src.second_question.vertex import Vertex
from src.third_question.graph import AStarGraph, AStarVertex


def print_answers():
    print(mocked_first_question)


def create_a_star_graph():

    vert = {}
    heuristic = {}
    for line in mocked_heuristic_cost_file.split('\n'):
        title, cost = line.split(' ')
        vert[title] = AStarVertex(title)
        heuristic[title] = int(cost)

    header, relation_file = mocked_relation_file.split("\n", maxsplit=1)
    for line in relation_file.split('\n'):
        origin, destiny, cost = line.split(' ')
        vert[origin].relation_distances[destiny] = int(cost)

    start, end = header.split(' ')

    a_star_graph = AStarGraph(vert)
    a_star_graph.search(start, end, heuristic)


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


def create_normal_graph():
    current_graph = read_input_file()

    def input_dfs():
        imputed_vertex = input('\n\nDe qual vértice que você quer inciar a busca?')
        current_graph.dfs(int(imputed_vertex))

    def input_bfs():
        imputed_vertex = input('\n\nDe qual vértice que você quer inciar a busca?')
        current_graph.bfs(int(imputed_vertex))

    sub_options = {
        '1': ('Relatório', current_graph.report),
        '2': ('Matriz de adjacência', current_graph.adjacency_matrix),
        '3': ('Lista de adjacencia', current_graph.adjacency_list),
        '4': ('DFS', input_dfs),
        '5': ('BFS', input_bfs),
        '9': ('Voltar', lambda: None)
    }
    
    input_option(sub_options)


def input_option(options):
    prompt = "\n".join(f'{key} - {value[0]}' for key, value in options.items())

    imputed_option = input(
        f"\n\nSelecione o número da opção desejada:\n{prompt}\n"
    )

    selected_option = options.get(imputed_option)

    if selected_option:
        selected_option[1]()
        return

    print("\n\nOpção invalida... Tente novamente!")


if __name__ == '__main__':

    while True:
        input_option({
            '1': ('Questão 1', print_answers),
            '2': ('Questão 2', create_normal_graph),
            '3': ('Questão 3', create_a_star_graph),
            '9': ('Sair', sys.exit)
        })

    print('Shall it never reach here!!!')
