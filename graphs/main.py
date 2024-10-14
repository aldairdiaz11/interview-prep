from random import randrange
from graph import Graph
from vertex import Vertex


def print_graph(graph: Graph):
    for vertex in graph.graph_dict:
        print(f"\n{vertex} connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges

        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print(f"=> {adjacent_vertex}")


def build_graph(directed: bool):
    g = Graph(directed)
    vertices = []

    for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)

    for v in range(len(vertices)):
        v_idx = randrange(0, len(vertices) - 1)
        v1 = vertices[v_idx]
        v_idx = randrange(0, len(vertices) - 1)
        v2 = vertices[v_idx]
        g.add_edge(v1, v2, randrange(1, 10))

    return g


if __name__ == "__main__":
    graph_test = build_graph(False)
    print_graph(graph_test)

    print(graph_test.find_path('a', 'b'))
