from queue import Queue
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

    def is_empty(self):
        return True if self.vertex == 0 else False

    def get_number_of_vertices(self):
        return self.vertex

    def get_number_of_edges(self):
        return self.edge

    def is_directed(self):
        return True if self.directed else False

    def has_vertex(self, v):
        return True if v < self.vertex else False

    def add_vertex(self):
        self.vertex += 1
        self.matrix.append([0] * self.vertex)

        for i in range(self.vertex - 1):
            self.matrix[i].extend([0])

    def remove_vertex(self, v):
        self.vertex -= 1
        self.matrix.pop(v)
        for vertex in self.matrix:
            vertex.pop(v)

    def has_edge(self, v1, v2):
        return True if self.matrix[v1][v2] else False

    def add_edge(self, v1, v2, weight=1):
        self.edge += 1
        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        self.edge -= 1
        self.matrix[v1][v2] = 0
        if not self.directed:
            self.matrix[v2][v1] = 0

    def modify_weight(self, v1, v2, weight):
        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    def weight(self, v1, v2):
        return self.matrix[v1][v2]

    def print_matrix(self):
        print(" ", end="  ")
        for i in range(self.vertex):
            if i < 10:
                print(i, end="  ")
            else:
                print(i, end=" ")
        print()
        i = 0
        for vertex in self.matrix:
            if i < 10:
                print(i, end="  ")
            else:
                print(i, end=" ")
            for edge in vertex:
                print(edge, end="  ")
            print()
            i += 1

    def iter_vertices(self):
        for i in range(self.vertex):
            yield i

    def iter_adjacent(self, v):
        for i in range(self.vertex):
            if self.matrix[v][i] > 0:
                yield i

    def iter_out_edges(self, v):
        for i in range(self.vertex):
            if self.matrix[v][i] > 0:
                yield v, i

    def iter_in_edges(self, v):
        for i in range(self.vertex):
            if self.matrix[i][v] > 0:
                yield i, v

    def iter_edges(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                if self.matrix[i][j] > 0:
                    yield i, j

    def dfs(self, v=0):
        visited = [False] * self.vertex
        self.dfs1(visited, v)
        for v in range(self.vertex):
            if not visited[v]:
                self.dfs1(visited, v)

    def dfs1(self, visited, v):
        visited[v] = True
        print(v, end=" ")
        for vertex in self.iter_adjacent(v):
            if not visited[vertex]:
                self.dfs1(visited, vertex)

    def bfs(self, v=0):
        visited = [False] * self.vertex
        q = Queue()
        self.bfs1(visited, v, q)
        for v in range(self.vertex):
            if not visited[v]:
                self.bfs1(visited, v, q)

    def bfs1(self, visited, v, q):
        q.put(v)
        visited[v] = True
        while not q.empty():
            v = q.get()
            print(v, end=" ")
            for vertex in self.iter_adjacent(v):
                if not visited[vertex]:
                    q.put(vertex)
                    visited[vertex] = True

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
        g.__set_matrix(new_matrix)
        g.__set_vertex(self.vertex)
        g.__set_edge(self.edge)
        return g
