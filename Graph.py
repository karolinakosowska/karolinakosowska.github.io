import numpy as np

class Graph:

    def __init__(self, directed=False):
        self.matrix = []
        self.directed = directed
        self.vertex = 0
        self.edge = 0

    def __set_matrix(self, matrix):
        self.matrix = matrix

    def __set_vertex(self, vertex):
        self.vertex = vertex

    def __set_edge(self, edge):
        self.edge = edge

    def get_number_of_vertices(self):
        return self.vertex

    def get_number_of_edges(self):
        return self.edge

    def is_directed(self):
        return True if self.directed else False

    def add_vertex(self):
        self.vertex += 1
        self.matrix.append([0] * self.vertex)

        for i in range(self.vertex - 1):
            self.matrix[i].extend([0])

    def remove_vertex(self, v):
        if v < self.vertex:
            self.vertex -= 1
            self.matrix.pop(v)
            for vertex in self.matrix:
                vertex.pop(v)
        else:
            print("This vertex doesn't exist!")

    def has_vertex(self, v):
        return True if v < self.vertex else False

    def add_edge(self, v1, v2, weight=1):
        if v1 != v2:
            if not self.has_edge(v1, v2):
                self.edge += 1
                self.matrix[v1][v2] = weight
                if not self.directed:
                    self.matrix[v2][v1] = weight
            else:
                print("This edge has already existed!")
        else:
            print("It's a simple graph. It doesn't contain loops.")

    def modify_weight(self, v1, v2, weight):
        if self.has_edge(v1, v2):
            self.matrix[v1][v2] = weight
        else:
            print("This edge doesn't exist!")

    def remove_edge(self, v1, v2):
        if self.has_edge(v1, v2):
            self.edge -= 1
            self.matrix[v1][v2] = 0
            if not self.directed:
                self.matrix[v2][v1] = 0
        else:
            print("This edge doesn't exist!")

    def has_edge(self, v1, v2):
        return True if self.matrix[v1][v2] else False

    def weight(self, v1, v2):
        return self.matrix[v1][v2]

    def print_matrix(self):
        print(self.matrix)
        if self.vertex > 0:
            for vertex in self.matrix:
                for edge in vertex:
                    print(edge, end=" ")
                print()
        else:
            print("Graph is empty!")

    def copy(self):
        g = Graph(self.directed)
        g.__set_matrix(self.matrix.copy())
        g.__set_vertex(self.vertex)
        g.__set_edge(self.edge)
        return g

    def transpose(self):
        g = Graph(self.directed)
        g.__set_matrix(np.array(self.matrix).T.tolist())
        g.__set_vertex(self.vertex)
        g.__set_edge(self.edge)
        return g

    def complement(self):
        g = Graph(self.directed)
        new_matrix = self.matrix.copy()
        for i in range(self.vertex):
            new_matrix[i] = [1 if edge == 0 else 0 for edge in new_matrix[i]]

        for vertex in new_matrix:
            vertex = [1 if edge == 0 else 0 for edge in vertex]
        g.__set_matrix(new_matrix)
        g.__set_vertex(self.vertex)
        g.__set_edge(self.edge)
        return g

    def subgraph(self, nodes):
        pass  # zwraca podgraf indukowa


g = Graph(True)
g.add_vertex()
g.add_vertex()
g.add_vertex()
g.add_vertex()

g.add_edge(0, 3, 5)
g.add_edge(1, 3, 2)
g.add_edge(1, 2, 3)
g.print_matrix()
print()

g1 = g.complement()
g1.print_matrix()
# lista list - macierz sąsiedztwa
# dodawanie wierzchołków
# dodawanie krawędzi