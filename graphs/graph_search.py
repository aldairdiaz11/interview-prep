from heapq import heappop, heappush
from math import inf, sqrt


# Depth-first search function:
def dfs(graph, current_vertex, target_value, visited=None):
    if not visited:
        visited = []

    visited.append(current_vertex)
    if current_vertex == target_value:
        return visited

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            return path if path else None


# Breadth-first search function
def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor == target_value:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])


# Dijkstra's search algorithm
def dijkstra(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = inf

    distances[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        curren_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = curren_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances


def a_star(graph, start, target):
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, start.name]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        curren_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = curren_distance + edge_weight + heuristic(neighbor, target)
            new_path = paths_and_distances[1] + [neighbor.name]

            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))

    return paths_and_distances[target][1]


def heuristic(start, target):
    return sqrt(abs(start.position[0] - target.position[0]) ** 2)+sqrt(abs(start.position[1] - target.position[1]) ** 2)


if __name__ == "__main__":
    some_hazardous_graph = {
        'lava': {'sharks', 'piranhas'},
        'sharks': {'piranhas', 'bees'},
        'piranhas': {'bees'},
        'bees': {'lasers'},
        'lasers': set([])
    }

    dijkstra_graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }

    print(bfs(some_hazardous_graph, 'sharks', 'bees'))
    print(dfs(some_hazardous_graph, 'sharks', 'bees'))
    print(dijkstra(dijkstra_graph, 'D'))
