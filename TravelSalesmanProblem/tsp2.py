import itertools
import networkx as nx
import matplotlib.pyplot as plt
import time


def tsp(graph):
    nodes = list(graph.nodes)
    permutations = itertools.permutations(nodes)
    min_cost = float('inf')
    best_route = None

    start_time = time.time()  # Inicio del temporizador dentro de la función tsp

    for perm in permutations:
        current_cost = 0
        valid_route = True
        for i in range(len(perm) - 1):
            if perm[i + 1] in graph[perm[i]]:
                current_cost += graph[perm[i]][perm[i + 1]]['weight']
            else:
                valid_route = False
                break
        if valid_route and perm[0] in graph[perm[-1]]:
            current_cost += graph[perm[-1]][perm[0]]['weight']
        else:
            valid_route = False

        if valid_route and current_cost < min_cost:
            min_cost = current_cost
            best_route = perm

    end_time = time.time()  # Fin del temporizador dentro de la función tsp
    elapsed_time = end_time - start_time

    return best_route, min_cost, elapsed_time  # Devolver también el tiempo de ejecución


def show_graph(graph, route):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')

    # Draw base graph
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')

    # Draw the edge labels
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    # Obtain the nodes and edges of the optimal route
    if route:
        route_edges = list(zip(route, route[1:] + route[:1]))
        route_nodes = route

        # Draw the nodes of the optimal route in red
        nx.draw_networkx_nodes(graph, pos, nodelist=route_nodes, node_color='r')

        # Draw the edges of the optimal route with arrows in red
        nx.draw_networkx_edges(graph, pos, edgelist=route_edges, edge_color='b', arrows=True, width=2)

    plt.show()


def main():
    print("Ingrese el grafo en el formato 'nodo1 nodo2 peso'. Ingrese 'fin' para terminar:")
    graph = nx.Graph()
    while True:
        entrada = input()
        if entrada.lower() == 'fin':
            break
        try:
            nodo1, nodo2, peso = entrada.split()
            peso = float(peso)
            graph.add_edge(nodo1, nodo2, weight=peso)
        except ValueError:
            print("Formato incorrecto. Por favor ingrese la arista nuevamente.")

    route, cost, elapsed_time = tsp(graph)  # Obtener también el tiempo de ejecución
    show_graph(graph, route)

    if route:
        print("La mejor ruta es:", " -> ".join(route))
        print("El costo mínimo es:", cost)
    else:
        print("No se encontró una ruta válida.")

    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")


if __name__ == "__main__":
    main()

"""
Grafo completo (todos los nodos están conectados entre sí)
A B 1
A C 2
A D 3
A E 4
B C 5
B D 6
B E 7
C D 8
C E 9
D E 10
fin

Grafo lineal
A B 1
B C 2
C D 3
D E 4
fin

Grafo con ciclo
A B 1
B C 2
C D 3
D E 4
E A 5
fin

Grafo desconectado
A B 1
C D 2
E F 3
B C 4
fin
"""
