import networkx as nx
import matplotlib.pyplot as plt

def inputGraph():
    Graph = nx.Graph()
    print("Ingrese las aristas del grafo en el formato 'nodo1 nodo2 peso'. Ingrese 'fin' para terminar:")

    while True:
        enter = input()
        if enter == 'fin':
            break
        try:
            node1, node2, weigth = enter.split()
            weigth = float(weigth)
            Graph.add_edge(node1, node2, weight=weigth)
        except ValueError:
            print("Formato incorrecto")

    return Graph

def ShowGraph(Graph):
    pos = nx.spring_layout(Graph)
    labels = nx.get_edge_attributes(Graph, 'weight')
    nx.draw(Graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)
    plt.show()

if __name__ == '__main__':
    graph = inputGraph()
    ShowGraph(graph)