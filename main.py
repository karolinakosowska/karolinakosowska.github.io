import sys

from Graph import *


def load():
    try:
        name = input("Enter name of file with extension .txt: ")
        return Graph.load_from_file(name)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    except JSONDecodeError as e:
        print("Empty file")
        sys.exit()
    except Exception as e:
        print("Unknown error")
        sys.exit()


def add_vertex(g):
    g.add_vertex()


def add_multiple_vertices(g):
    v = int(input("Enter the number of vertices to add: "))
    for i in range(v):
        g.add_vertex()


def add_edge(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge to add: ").split()]
    try:
        w = int(input("Enter the edge weight. If you don't want to specify weight, press Enter: "))
    except ValueError:
        try:
            g.add_edge(v1, v2)
        except Exception as e:
            print(e)
    else:
        try:
            g.add_edge(v1, v2, w)
        except Exception as e:
            print(e)


def remove_edge(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge to remove: ").split()]
    try:
        g.remove_edge(v1, v2)
    except Exception as e:
        print(e)


def remove_connections_with_vertex(g):
    try:
        v = int(input("Enter vertex to remove connections: "))
        g.remove_connections_with_vertex(v)
    except Exception as e:
        print(e)


def modify_weight(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge: ").split()]
    try:
        w = int(input("Enter the new edge weight: "))
        g.modify_weight(v1, v2, w)
    except Exception as e:
        print(e)


def has_vertex(g):
    v = int(input("Enter vertex: "))
    print(f"Vertex {v} exists" if g.has_vertex(v) else f"Vertex {v} doesn't exist")


def has_edge(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge: ").split()]
    try:
        print(f"Edge ({v1}, {v2}) exists" if g.has_edge(v1, v2) else f"Edge ({v1}, {v2}) doesn't exist")
    except Exception as e:
        print(e)


def weight(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge: ").split()]
    try:
        print(g.weight(v1, v2))
    except Exception as e:
        print(e)


def print_matrix(g):
    try:
        g.print_matrix()
    except Exception as e:
        print(e)


def print_vertices(g):
    for vertex in g.iter_vertices():
        print(vertex, end=" ")
    print()


def print_edges(g):
    for edge in g.iter_edges():
        print(edge, end=" ")
    print()


def print_adjacent_vertices(g):
    try:
        v = int(input("Enter vertex: "))
        for vertex in g.iter_adjacent(v):
            print(vertex, end=" ")
        print()
    except Exception as e:
        print(e)


def print_out_edges(g):
    try:
        v = int(input("Enter vertex: "))
        for edge in g.iter_out_edges(v):
            print(edge, end=" ")
        print()
    except Exception as e:
        print(e)


def print_in_edges(g):
    try:
        v = int(input("Enter vertex: "))
        for edge in g.iter_in_edges(v):
            print(edge, end=" ")
        print()
    except Exception as e:
        print(e)


def print_transposed(g):
    g.transpose().print_matrix()


def print_complement(g):
    g.complement().print_matrix()


def dfs(g):
    g.dfs()
    print()


def bfs(g):
    g.bfs()
    print()


def save(g):
    try:
        name = input("Enter name of file with extension .txt: ")
        g.save_to_file(name)
    except Exception as e:
        print("Unknown error")


if __name__ == '__main__':
    choice = 0
    graph = None
    new_graph = False

    while choice != 1 and choice != 2:
        choice = int(input("Choose what you want to do:\n"
                           "1. Create new graph\n"
                           "2. Load graph from file\n"))
        if choice == 1:
            new_graph = True
        elif choice == 2:
            graph = load()
        else:
            print("Wrong option. Try again\n")

    choice = 0
    if new_graph:
        while choice != 1 and choice != 2:
            choice = int(input("\nSelect a graph type:\n"
                               "1. Directed\n"
                               "2. Undirected\n"))
            if choice == 1:
                graph = Graph(True)
            elif choice == 2:
                graph = Graph()
            else:
                print("Wrong option. Try again\n")

    while choice != 24:
        choice = int(input(
            "\nChoose what you want to do:\n"
            "1. Add vertex\n"
            "2. Add multiple vertices\n"
            "3. Add edge\n"
            "4. Remove edge\n"
            "5. Remove connections with vertex\n"
            "6. Modify edge weight\n"
            "7. Get number of vertices\n"
            "8. Get number of edges\n"
            "9. Check if vertex exists\n"
            "10. Check if edge exists\n"
            "11. Check if graph is directed\n"
            "12. Check edge weight\n"
            "13. Display graph adjacency matrix\n"
            "14. Display vertices\n"
            "15. Display edges\n"
            "16. Display adjacent vertices\n"
            "17. Display outgoing edges\n"
            "18. Display incoming edges\n"
            "19. Display transposed graph\n"
            "20. Display graph complement\n"
            "21. DFS\n"
            "22. BFS\n"
            "23. Save graph to file\n"
            "24. Exit\n"
        ))

        if choice == 1:
            add_vertex(graph)
        elif choice == 2:
            add_multiple_vertices(graph)
        elif choice == 3:
            add_edge(graph)
        elif choice == 4:
            remove_edge(graph)
        elif choice == 5:
            remove_connections_with_vertex(graph)
        elif choice == 6:
            modify_weight(graph)
        elif choice == 7:
            print(graph.get_number_of_vertices())
        elif choice == 8:
            print(graph.get_number_of_edges())
        elif choice == 9:
            has_vertex(graph)
        elif choice == 10:
            has_edge(graph)
        elif choice == 11:
            print(graph.is_directed())
        elif choice == 12:
            weight(graph)
        elif choice == 13:
            print_matrix(graph)
        elif choice == 14:
            print_vertices(graph)
        elif choice == 15:
            print_edges(graph)
        elif choice == 16:
            print_adjacent_vertices(graph)
        elif choice == 17:
            print_out_edges(graph)
        elif choice == 18:
            print_in_edges(graph)
        elif choice == 19:
            print_transposed(graph)
        elif choice == 20:
            print_complement(graph)
        elif choice == 21:
            dfs(graph)
        elif choice == 22:
            bfs(graph)
        elif choice == 23:
            save(graph)
        elif choice == 24:
            print("See you soon!")
        else:
            print("Wrong option. Try again")
