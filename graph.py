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
graph.add_edge("Wonosobo", "Kudus")
graph.add_edge("Wonosobo", "Semarang")
graph.add_edge("Wonosobo", "Kendal")
graph.add_edge("Wonosobo", "Pekalongan")
graph.add_edge("Temanggung", "Salatiga")
graph.add_edge("Temanggung", "Surakarta")
graph.add_edge("Temanggung", "Blora")
graph.add_edge("Temanggung", "Rembang")
graph.add_edge("Temanggung", "Pati")
graph.add_edge("Temanggung", "Kudus")
graph.add_edge("Temanggung", "Semarang")
graph.add_edge("Temanggung", "Kendal")
graph.add_edge("Temanggung", "Pekalongan")
graph.add_edge("Salatiga", "Surakarta")
graph.add_edge("Salatiga", "Blora")
graph.add_edge("Salatiga", "Rembang")
graph.add_edge("Salatiga", "Pati")
graph.add_edge("Salatiga", "Kudus")
graph.add_edge("Salatiga", "Semarang")
graph.add_edge("Salatiga", "Kendal")
graph.add_edge("Salatiga", "Pekalongan")
graph.add_edge("Surakarta", "Blora")
graph.add_edge("Surakarta", "Rembang")
graph.add_edge("Surakarta", "Pati")
graph.add_edge("Surakarta", "Kudus")
graph.add_edge("Surakarta", "Semarang")
graph.add_edge("Surakarta", "Kendal")
