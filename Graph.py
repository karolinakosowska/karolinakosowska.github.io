from json import JSONDecodeError
from queue import Queue
import numpy as np
import json


class Graph:
    """
    A class to represent a graph.

        Attributes:
            matrix : list
                graph adjacency matrix
            directed : bool
                boolean flag for the graph type - True means directed graph, False means undirected
            vertex : int
                number of graph vertices
            edge : int
                number of graph edges

        Methods:
            is_empty()
                Returns boolean if graph is empty.
            get_number_of_vertices()
                Returns number of graph vertices.
            get_number_of_edges()
                Returns number of graph edges.
            is_directed()
                Returns boolean if graph is directed.
            has_vertex(v)
                Returns boolean if graph contains vertex v.
            add_vertex()
                Adds vertex to graph.
            has_edge(v1, v2)
                Returns boolean if graph contains edge between vertices v1 and v2.
            add_edge(v1, v2, weight=1)
                Adds edge between vertices v1 and v2 with weight to graph.
            remove_edge(v1, v2)
                Removes edge between vertices v1 and v2 from graph.
            remove_connections_with_vertex(v)
                Removes all connections with vertex v.
            modify_weight(v1, v2, weight)
                Modifies edge weight between vertices v1 and v2.
            weight(v1, v2)
                Returns edge weight between vertices v1 and v2.
            print_matrix()
                Prints graph matrix adjacency.
            iter_vertices()
                Iterates over vertices of graph.
            iter_adjacent(v)
                Iterates over adjacent vertices of vertex v.
            iter_out_edges(v)
                Iterates over outgoing edges from vertex v.
            iter_in_edges(v)
                Iterates over incoming edges to vertex v.
            iter_edges()
                Iterates over edges of graph.
            dfs(v=0)
                Prints vertices in DFS order.
            bfs(v=0)
                Prints vertices in BFS order.
            transpose()
                Prints transposed graph matrix adjacency.
            complement()
                Prints complement of graph matrix adjacency.
            load_from_file(name)
                Loads graph from file.
            save_to_file(name)
                Saves graph to file.
    """

    def __init__(self, directed=False):
        """
        Constructs all the necessary attributes for graph object.

        :param directed: boolean flag that specifies graph type
        :type directed: bool or None
        """
        self.matrix = []
        self.directed = directed
        self.vertex = 0
        self.edge = 0

    def __set_matrix(self, matrix):
        """
        Sets graph matrix adjacency.

        :param list matrix: graph matrix adjacency
        """
        self.matrix = matrix

    def __set_vertex(self, vertex):
        """
        Sets number of graph vertices.

        :param int vertex: number of graph vertices
        """
        self.vertex = vertex

    def __set_edge(self, edge):
        """
        Sets number of graph edges.

        :param int edge: number of graph edges
        """
        self.edge = edge

    def is_empty(self):
        """
        Returns boolean if graph is empty.

        :returns: boolean flag if graph is empty
        :rtype: bool
        """
        return True if self.vertex == 0 else False

    def get_number_of_vertices(self):
        """
        Returns number of graph vertices.

        :returns: number of graph vertices
        :rtype: int
        """
        return self.vertex

    def get_number_of_edges(self):
        """
        Returns number of graph edges.

        :returns: number of graph edges
        :rtype: int
        """
        return self.edge

    def is_directed(self):
        """
        Returns boolean if graph is directed.

        :returns: boolean flag if graph is directed
        :rtype: bool
        """
        return True if self.directed else False

    def has_vertex(self, v):
        """
        Returns boolean if graph contains vertex v.

        :param int v: number of vertex
        :return: boolean flag if graph contains given vertex
        :rtype: bool
        """
        return True if v < self.vertex else False

    def add_vertex(self):
        """ Adds vertex to graph. """
        self.vertex += 1
        self.matrix.append([0] * self.vertex)

        for i in range(self.vertex - 1):
            self.matrix[i].extend([0])

    def has_edge(self, v1, v2):
        """
        Returns boolean if graph contains edge between vertices v1 and v2.

        :param int v1: number of first vertex of edge
        :param int v2: number of second vertex of edge
        :return: boolean flag if graph contains edge of given vertices
        :rtype: bool
        :raise Exception: if one of given vertices doesn't exist
        """
        if not self.has_vertex(v1):
            raise Exception(f"Vertex {v1} doesn't exist!")
        elif not self.has_vertex(v2):
            raise Exception(f"Vertex {v2} doesn't exist!")
        else:
            return True if self.matrix[v1][v2] else False

    def add_edge(self, v1, v2, weight=1):
        """
        Adds edge between vertices v1 and v2 with weight to graph.

        :param int v1: number of first vertex of edge
        :param int v2: number of second vertex of edge
        :param weight: weight of edge
        :type weight: int or None
        :raise Exception: if one of given vertex doesn't exist, given vertices are identical, edge has already existed or given weight is equal to 0
        """
        if not self.has_vertex(v1):
            raise Exception(f"Vertex {v1} doesn't exist!")
        elif not self.has_vertex(v2):
            raise Exception(f"Vertex {v2} doesn't exist!")
        elif v1 == v2:
            raise Exception("It's a simple graph. It doesn't contain loops.")
        elif self.has_edge(v1, v2):
            raise Exception("This edge has already existed!")
        elif weight == 0:
            raise Exception("Weight mustn't be 0!")
        else:
            self.edge += 1
            self.matrix[v1][v2] = weight
            if not self.directed:
                self.matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        """
        Removes edge between vertices v1 and v2 from graph.

        :param int v1: number of first vertex of edge
        :param int v2: number of second vertex of edge
        :raise Exception: if one of given vertex or edge between given vertices doesn't exist
        """
        if not self.has_vertex(v1):
            raise Exception(f"Vertex {v1} doesn't exist!")
        elif not self.has_vertex(v2):
            raise Exception(f"Vertex {v2} doesn't exist!")
        elif not self.has_edge(v1, v2):
            raise Exception("This edge doesn't exist!")
        else:
            self.edge -= 1
            self.matrix[v1][v2] = 0
            if not self.directed:
                self.matrix[v2][v1] = 0

    def remove_connections_with_vertex(self, v):
        """
        Removes all connections with vertex v.

        :param int v: number of vertex
        :raise Exception: if given vertex doesn't exist
        """
        if not self.has_vertex(v):
            raise Exception(f"Vertex {v} doesn't exist!")
        else:
            for i in range(self.vertex):
                if self.has_edge(i, v):
                    self.remove_edge(i, v)
                if self.directed:
                    if self.has_edge(v, i):
                        self.remove_edge(v, i)

    def modify_weight(self, v1, v2, weight):
        """
        Modifies edge weight between vertices v1 and v2.

        :param int v1: number of first vertex of edge
        :param int v2: number of second vertex of edge
        :param int weight: new weight of edge
        :raise Exception: if one of given vertex or edge between given vertices doesn't exist or given weight is equal to 0
        """
        if not self.has_vertex(v1):
            raise Exception(f"Vertex {v1} doesn't exist!")
        elif not self.has_vertex(v2):
            raise Exception(f"Vertex {v2} doesn't exist!")
        elif not self.has_edge(v1, v2):
            raise Exception("This edge doesn't exist!")
        elif weight == 0:
            raise Exception("Weight mustn't be 0!")
        else:
            self.matrix[v1][v2] = weight
            if not self.directed:
                self.matrix[v2][v1] = weight

    def weight(self, v1, v2):
        """
        Returns edge weight between vertices v1 and v2.

        :param int v1: number of first vertex of edge
        :param int v2: number of second vertex of edge
        :raise Exception: if one of given vertex or edge between given vertices doesn't exist
        """
        if not self.has_vertex(v1):
            raise Exception(f"Vertex {v1} doesn't exist!")
        elif not self.has_vertex(v2):
            raise Exception(f"Vertex {v2} doesn't exist!")
        elif not self.has_edge(v1, v2):
            raise Exception("This edge doesn't exist!")
        else:
            return self.matrix[v1][v2]

    def print_matrix(self):
        """
        Prints graph matrix adjacency.

        :raise Exception: if graph is empty
        """
        if self.get_number_of_vertices == 0:
            raise Exception("Graph is empty!")
        else:
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
        """
        Iterates over vertices of graph.

        :return: next vertex
        """
        for i in range(self.vertex):
            yield i

    def iter_adjacent(self, v):
        """
        Iterates over adjacent vertices of vertex v.

        :param v: number of vertex
        :return: next adjacent vertex of given vertex
        :raise Exception: if given vertex doesn't exist
        """
        if not self.has_vertex(v):
            raise Exception(f"Vertex {v} doesn't exist!")
        else:
            for i in range(self.vertex):
                if self.matrix[v][i] > 0:
                    yield i

    def iter_out_edges(self, v):
        """
        Iterates over outgoing edges from vertex v.

        :param v: number of vertex
        :return: next outgoing edge from given vertex
        :raise Exception: if given vertex doesn't exist
        """
        if not self.has_vertex(v):
            raise Exception(f"Vertex {v} doesn't exist!")
        else:
            for i in range(self.vertex):
                if self.matrix[v][i] > 0:
                    yield v, i

    def iter_in_edges(self, v):
        """
        Iterates over incoming edges to vertex v.

        :param v: number of vertex
        :return: next incoming edge to given vertex
        :raise Exception: if given vertex doesn't exist
        """
        if not self.has_vertex(v):
            raise Exception(f"Vertex {v} doesn't exist!")
        else:
            for i in range(self.vertex):
                if self.matrix[i][v] > 0:
                    yield i, v

    def iter_edges(self):
        """
        Iterates over edges of graph.

        :return: next edge
        """
        for i in range(self.vertex):
            for j in range(self.vertex):
                if self.matrix[i][j] > 0:
                    yield i, j

    def dfs(self, v=0):
        """
        Prints vertices in DFS order.

        :param v: number of starting vertex
        :type v: int or None
        """
        visited = [False] * self.vertex
        self.__dfs1(visited, v)
        for v in range(self.vertex):
            if not visited[v]:
                self.__dfs1(visited, v)

    def __dfs1(self, visited, v):
        """
        Auxiliary function to perform DFS on all vertices.

        :param list visited: list of boolean values marking vertices as visited
        :param int v: number of vertex
        """
        visited[v] = True
        print(v, end=" ")
        for vertex in self.iter_adjacent(v):
            if not visited[vertex]:
                self.__dfs1(visited, vertex)

    def bfs(self, v=0):
        """
        Prints vertices in BFS order.

        :param v: number of starting vertex
        :type v: int or None
        """
        visited = [False] * self.vertex
        q = Queue()
        self.__bfs1(visited, v, q)
        for v in range(self.vertex):
            if not visited[v]:
                self.__bfs1(visited, v, q)

    def __bfs1(self, visited, v, q):
        """
        Auxiliary function to perform BFS on all vertices.

        :param list visited: list of boolean values marking vertices as visited
        :param int v: number of vertex
        :param Queue q: queue of vertices to visit
        """
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
        """ Prints transposed graph matrix adjacency. """
        g = Graph(self.directed)
        g.__set_matrix(np.array(self.matrix).T.tolist())
        g.__set_vertex(self.vertex)
        g.__set_edge(self.edge)
        return g

    def complement(self):
        """ Prints complement of graph matrix adjacency. """
        g = Graph(self.directed)
        new_matrix = self.matrix.copy()
        for i in range(self.vertex):
            new_matrix[i] = [1 if edge == 0 else 0 for edge in new_matrix[i]]
        g.__set_matrix(new_matrix)
        g.__set_vertex(self.vertex)
        g.__set_edge(self.edge)
        return g

    @staticmethod
    def load_from_file(name):
        """
        Loads graph from file.

        :param str name: name of file to load
        :return: Graph object
        :rtype: Graph
        """
        try:
            f = open(name)
            g = Graph(json.loads(f.readline()))
            g.__set_vertex(json.loads(f.readline()))
            g.__set_edge(json.loads(f.readline()))
            new_matrix = []
            for i in range(g.vertex):
                new_matrix.append(json.loads(f.readline()))
            g.__set_matrix(new_matrix)
            return g
        except FileNotFoundError as e:
            raise e
        except JSONDecodeError as e:
            raise e
        except Exception as e:
            raise e
        finally:
            f.close()

    def save_to_file(self, name):
        """
        Saves graph to file.

        :param str name: name of file to save
        """
        try:
            f = open(name, "w")
            f.write(json.dumps(self.is_directed()) + "\n")
            f.write(json.dumps(self.vertex) + "\n")
            f.write(json.dumps(self.edge) + "\n")
            for i in range(self.vertex):
                f.write(json.dumps(self.matrix[i]) + "\n")
        except Exception as e:
            raise e
        finally:
            f.close()
