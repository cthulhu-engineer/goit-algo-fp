import heapq


class Graph:
    """

    :class: Graph

    This class represents a graph data structure. It supports methods for adding edges between vertices and finding the shortest path using Dijkstra's algorithm.

    :ivar V: an integer representing the number of vertices in the graph
    :ivar graph: a dictionary representing the graph structure, where the keys are the vertices and the values are lists of tuples containing the neighbors and weights

    :func __init__(self, vertices):
        Constructs a new Graph object.

        :param vertices: an integer representing the number of vertices in the graph

    :func add_edge(self, u, v, w):
        Adds an edge between two vertices with a given weight.

        :param u: an integer representing the first vertex
        :param v: an integer representing the second vertex
        :param w: a numeric value representing the weight of the edge

    :func dijkstra(self, src):
        Finds the shortest path from a given source vertex to all other vertices using Dijkstra's algorithm.

        :param src: an integer representing the source vertex
        :return: a dictionary of the distances from the source vertex to all other vertices, where the keys are the vertices and the values are the corresponding distances

    """
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, src):
        min_heap = [(0, src)]
        distances = {i: float('inf') for i in range(self.V)}
        distances[src] = 0

        while min_heap:
            dist, current_vertex = heapq.heappop(min_heap)

            # Якщо дистанція в купі більше, ніж поточна дистанція, пропускаємо
            if dist > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances


if __name__ == "__main__":
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    distances = graph.dijkstra(0)
    print("Відстані від початкової вершини до всіх інших:")
    for vertex in range(graph.V):
        print(f"0 -> {vertex}: {distances[vertex]}")
