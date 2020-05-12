import sys
from copy import deepcopy

from src.second_question.graph import Graph
from src.second_question.vertex import Vertex


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


def input_bfs():
    imputed_vertex = input('\n\nDe qual vértice que você quer inciar a busca?')
    current_graph.bfs(int(imputed_vertex))


if __name__ == '__main__':
    graph = read_input_file()
    while True:
        current_graph = deepcopy(graph)

        options = {
            '1': ('Relatório', current_graph.report),
            '2': ('Matriz de adjacência', current_graph.adjacency_matrix),
            '3': ('Lista de adjacencia', current_graph.adjacency_list),
            '4': ('DFS', input_dfs),
            '5': ('BFS', input_bfs),
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
