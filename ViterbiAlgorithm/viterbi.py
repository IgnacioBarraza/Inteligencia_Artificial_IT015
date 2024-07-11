import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def viterbi(obs, states, start_p, trans_p, emit_p):
    """
    Args:
    obs: Lista de observaciones.
    states: Lista de posibles estados.
    start_p: Diccionario de probabilidades iniciales de los estados.
    trans_p: Diccionario de diccionarios con las probabilidades de transición entre estados.
    emit_p: Diccionario de diccionarios con las probabilidades de emisión de observaciones.

    Returns:
    La secuencia de estados más probable, su probabilidad, y la matriz de Viterbi.
    """
    v = [{}]
    path = {}

    # Inicialización
    for state in states:
        v[0][state] = start_p[state] * emit_p[state][obs[0]]
        path[state] = [state]

    # Recursión
    for t in range(1, len(obs)):
        v.append({})
        new_path = {}

        for current_state in states:
            max_prob, prev_st = max(
                (v[t - 1][prev_state] * trans_p[prev_state][current_state] * emit_p[current_state][obs[t]], prev_state)
                for prev_state in states)
            v[t][current_state] = max_prob
            new_path[current_state] = path[prev_st] + [current_state]

        path = new_path

    # Terminación
    max_prob, final_state = max((v[len(obs) - 1][state], state) for state in states)
    best_path = path[final_state]

    # Convertir v a una matriz de numpy para facilitar el gráfico
    viterbi_matrix = np.zeros((len(states), len(obs)))
    for t in range(len(obs)):
        for i, state in enumerate(states):
            viterbi_matrix[i, t] = v[t][state]

    return max_prob, best_path, viterbi_matrix


# Función para ingresar el grafo
def ingresar_grafo():
    print("Ingrese los estados separados por comas:")
    states = input().split(',')

    print("Ingrese las observaciones separadas por comas:")
    observations = input().split(',')

    start_p = {}
    print("Ingrese las probabilidades iniciales (formato: estado=probabilidad):")
    for state in states:
        prob = float(input(f"{state}: "))
        start_p[state] = prob

    trans_p = {}
    print("Ingrese las probabilidades de transición (formato: estado1->estado2=probabilidad):")
    for state1 in states:
        trans_p[state1] = {}
        for state2 in states:
            prob = float(input(f"{state1}->{state2}: "))
            trans_p[state1][state2] = prob

    emit_p = {}
    print("Ingrese las probabilidades de emisión (formato: estado->observacion=probabilidad):")
    for state in states:
        emit_p[state] = {}
        for obs in observations:
            prob = float(input(f"{state}->{obs}: "))
            emit_p[state][obs] = prob

    return states, observations, start_p, trans_p, emit_p


def draw_hmm(states, trans_p, emit_p):
    G = nx.MultiDiGraph()

    # Añadir nodos
    for state in states:
        G.add_node(state)

    # Añadir probabilidades de transición como arcos
    for from_state in trans_p:
        for to_state in trans_p[from_state]:
            G.add_edge(from_state, to_state, label=f"{trans_p[from_state][to_state]:.2f}")

    # Añadir probabilidades de emisión como arcos hacia nodos de observaciones
    for state in emit_p:
        for obs in emit_p[state]:
            G.add_edge(state, obs, label=f"{emit_p[state][obs]:.2f}", color='blue')

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'label')
    edge_colors = [G[u][v][0]['color'] if 'color' in G[u][v][0] else 'black' for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold',
            edge_color=edge_colors, arrows=True, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Hidden Markov Model")
    plt.show()


if __name__ == "__main__":
    states, observations, start_p, trans_p, emit_p = ingresar_grafo()

    print("Ingrese la secuencia de observaciones separadas por comas:")
    obs_seq = input().split(',')

    prob, path, viterbi_matrix = viterbi(obs_seq, states, start_p, trans_p, emit_p)
    print(f"La secuencia de estados más probable es: {path} con una probabilidad de {prob}")

    draw_hmm(states, trans_p, emit_p)
