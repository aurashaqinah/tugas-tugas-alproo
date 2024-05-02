class AdjacencyListGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    def display_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

# Create a graph
graph = AdjacencyListGraph()

# Add vertices
graph.add_vertex("Banjarnegara")
graph.add_vertex("Wonosobo")
graph.add_vertex("Temanggung")
