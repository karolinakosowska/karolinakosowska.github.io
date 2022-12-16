from Graph import *


def add_vertex(g):
    g.add_vertex()


def add_multiple_vertices(g):
    v = int(input("Enter the number of vertices to add: "))
    for i in range(v):
        g.add_vertex()


def remove_vertex(g):
    v = int(input("Enter vertex to remove: "))
    if not g.has_vertex(v):
        print(f"Vertex {v} doesn't exist!")
    else:
        g.remove_vertex(v)


def add_edge(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge to add: ").split()]
    if not g.has_vertex(v1):
        print(f"Vertex {v1} doesn't exist!")
    elif not g.has_vertex(v2):
        print(f"Vertex {v2} doesn't exist!")
    elif v1 == v2:
        print("It's a simple graph. It doesn't contain loops.")
    elif g.has_edge(v1, v2):
        print("This edge has already existed!")
    else:
        try:
            w = int(input("Enter the edge weight. If you don't want to specify weight, press Enter: "))
        except ValueError:
            g.add_edge(v1, v2)
        else:
            g.add_edge(v1, v2, w)


def remove_edge(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge to remove: ").split()]
    if not g.has_vertex(v1):
        print(f"Vertex {v1} doesn't exist!")
    elif not g.has_vertex(v2):
        print(f"Vertex {v2} doesn't exist!")
    elif not g.has_edge(v1, v2):
        print("This edge doesn't exist!")
    else:
        g.remove_edge(v1, v2)


def modify_weight(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge: ").split()]
    if not g.has_vertex(v1):
        print(f"Vertex {v1} doesn't exist!")
    elif not g.has_vertex(v2):
        print(f"Vertex {v2} doesn't exist!")
    elif not g.has_edge(v1, v2):
        print("This edge doesn't exist!")
    else:
        w = int(input("Enter the new edge weight: "))
        g.modify_weight(v1, v2, w)


def has_vertex(g):
    v = int(input("Enter vertex: "))
    print(f"Vertex {v} exists" if g.has_vertex(v) else f"Vertex {v} doesn't exist")


def has_edge(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge: ").split()]
    if not g.has_vertex(v1):
        print(f"Vertex {v1} doesn't exist!")
    elif not g.has_vertex(v2):
        print(f"Vertex {v2} doesn't exist!")
    else:
        print(f"Edge ({v1}, {v2}) exists" if g.has_edge(v1, v2) else f"Edge ({v1}, {v2}) doesn't exist")


def weight(g):
    v1, v2 = [int(x) for x in input("Enter vertices of edge: ").split()]
    if not g.has_vertex(v1):
        print(f"Vertex {v1} doesn't exist!")
    elif not g.has_vertex(v2):
        print(f"Vertex {v2} doesn't exist!")
    elif not g.has_edge(v1, v2):
        print("This edge doesn't exist!")
    else:
        print(g.weight(v1, v2))


def print_matrix(g):
    if g.get_number_of_vertices == 0:
        print("Graph is empty!")
    else:
        g.print_matrix()


def print_vertices(g):
    for vertex in g.iter_vertices():
        print(vertex, end=" ")
    print()


def print_edges(g):
    for edge in g.iter_edges():
        print(edge, end=" ")
    print()


def print_adjacent_vertices(g):
    v = int(input("Enter vertex: "))
    for vertex in g.iter_adjacent(v):
        print(vertex, end=" ")
    print()


def print_out_edges(g):
    v = int(input("Enter vertex: "))
    for edge in g.iter_out_edges(v):
        print(edge, end=" ")
    print()


def print_in_edges(g):
    v = int(input("Enter vertex: "))
    for edge in g.iter_in_edges(v):
        print(edge, end=" ")
    print()


def print_transposed(g):
    g.transpose().print_matrix()


def print_complement(g):
    g.complement().print_matrix()


def dfs(g):
    g.dfs()


def bfs(g):
    g.bfs()


if __name__ == '__main__':
    choice = 0
    graph = None
    while choice != 1 and choice != 2:
        choice = int(input("Select a graph type:\n"
                           "1. Directed\n"
                           "2. Undirected\n"))
        match choice:
            case 1:
                graph = Graph(True)
            case 2:
                graph = Graph()
            case _:
                print("Wrong option. Try again\n")

    while choice != 22:
        choice = int(input(
            "\nChoose what you want to do:\n"
            "1. Add vertex\n"
            "2. Add multiple vertices\n"
            "3. Remove vertex\n"
            "4. Add edge\n"
            "5. Remove edge\n"
            "6. Modify edge weight\n"
            "7. Get number of vertices\n"
            "8. Get number of edges\n"
            "9. Check if vertex exists\n"
            "10. Check if edge exists\n"
            "11. Check edge weight\n"
            "12. Display graph adjacency matrix\n"
            "13. Display vertices\n"
            "14. Display edges\n"
            "15. Display adjacent vertices\n"
            "16. Display outgoing edges\n"
            "17. Display incoming edges\n"
            "18. Display transposed graph\n"
            "19. Display graph complement\n"
            "20. DFS\n"
            "21. BFS\n"
            "22. Exit\n"
        ))

        match choice:
            case 1:
                add_vertex(graph)
            case 2:
                add_multiple_vertices(graph)
            case 3:
                remove_vertex(graph)
            case 4:
                add_edge(graph)
            case 5:
                remove_edge(graph)
            case 6:
                modify_weight(graph)
            case 7:
                print(graph.get_number_of_vertices())
            case 8:
                print(graph.get_number_of_edges())
            case 9:
                has_vertex(graph)
            case 10:
                has_edge(graph)
            case 11:
                weight(graph)
            case 12:
                print_matrix(graph)
            case 13:
                print_vertices(graph)
            case 14:
                print_edges(graph)
            case 15:
                print_adjacent_vertices(graph)
            case 16:
                print_out_edges(graph)
            case 17:
                print_in_edges(graph)
            case 18:
                print_transposed(graph)
            case 19:
                print_complement(graph)
            case 20:
                dfs(graph)
            case 21:
                bfs(graph)
            case 22:
                print("See you soon!")
            case _:
                print("Wrong option. Try again")
