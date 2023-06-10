import numpy as np


def build_graph():
    graph_type = input("Podaj typ grafu (skierowany/directed, nieskierowany/undirected): ")
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    num_edges = int(input("Podaj liczbę połączeń: "))

    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    adjacency_list = [[] for _ in range(num_vertices)]

    if graph_type.lower() in ['skierowany', 'directed']:
        directed = True
    else:
        directed = False

    print("Podaj połączenia w formacie 'wierzchołek1 wierzchołek2 waga' (oddzielone spacjami):")
    for _ in range(num_edges):
        edge_info = input().split()
        source = int(edge_info[0])
        target = int(edge_info[1])
        weight = float(edge_info[2]) if len(edge_info) > 2 else 1.0

        adjacency_matrix[source][target] = weight
        adjacency_list[source].append((target, weight))

        if not directed:
            adjacency_matrix[target][source] = weight
            adjacency_list[target].append((source, weight))

    print("\nMacierz sąsiedztwa:")
    for row in adjacency_matrix:
        print(row)

    print("\nLista sąsiedztwa:")
    for vertex, neighbors in enumerate(adjacency_list):
        print(f"{vertex}: {neighbors}")

build_graph()