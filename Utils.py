import warnings

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def print_solution(rez):
    print(rez[2])
    print(rez[0])
    print(rez[1])


def modularity(communities, param, network):
    nodes = param['nodes']
    mat = network['mat']
    degrees = network['degrees']
    edges = network['edges']
    M = 2 * edges
    Q = 0.0
    for i in range(0, nodes):
        for j in range(0, nodes):
            if (communities[i] == communities[j]):
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M

def read_network(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['nodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    edges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                edges += mat[i][j]
        degrees.append(d)
    net["edges"] = edges
    net["degrees"] = degrees
    f.close()
    return net


def read_gml(filename):
    G = nx.read_gml(filename, 'id')
    network = {}
    matrix = [[0 for x in range(len(G))] for y in range(len(G))]
    network['nodes'] = len(G)
    network['edges'] = G.size()
    for e in G.edges:
        matrix[e[0] - 1][e[1] - 1] = matrix[e[1] - 1][e[0] - 1] = 1
    degrees = []
    for nodes in G.nodes:
        degrees.append(G.degree(nodes))
    network['mat'] = matrix
    network['degrees'] = degrees
    return network


def show_communities(communities, network):
    # plot a particular division in communities
    A = np.matrix(network)
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=100, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()


def showNetwork(network):
    warnings.simplefilter('ignore')
    A = np.matrix(network)
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlGn)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()


def get_parameters(data):
    # setez parametrii problemei special pentru a-i avea la indemana
    # parameters care contine: min = nodul minim, max = nodul maxim, nodes = nr de noduri, modularity = functia de modularitate
    # pe langa asta, imi setez populatia originala de 10
    parameters = {}
    parameters["min"] = 1
    parameters["max"] = data["nodes"]
    parameters["nodes"] = data["nodes"]
    parameters['modularity'] = modularity

    sizePopulation = {}
    sizePopulation["size"] = 10

    return parameters, sizePopulation


def get_communities(representation):
    # toate valorile unice
    return len(set(representation))
