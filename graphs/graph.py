from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict: {str: Vertex} = {}

    def add_vertex(self, vertex: Vertex):
        self.graph_dict[vertex.value] = Vertex(vertex)

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)

        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex: str, end_vertex: str):
        start = [start_vertex]
        seen = {}

        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True

            print("Visiting " + current_vertex)

            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]

        return False
