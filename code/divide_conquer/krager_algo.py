#!usr/bin/python3

import random

def create_dict(line, graph):

    x = line.split("\t")
    print(x)
    graph[x[0]] = x[1:]

def random_contraction(n1, n2, graph):

    for node in graph[n1]:
        if node != n2:
            graph[node].append(n2)
            graph[n2].append(node)
        graph[node].remove(n1)

    del graph[n1]

def compute_min_cut(graph):

    while len(graph.keys()) > 2:

        # pick a random edge
        n1 = random.choice(list(graph))
        n2 = random.choice(graph[n1])

        random_contraction(n1, n2, graph)
        #print("Graph after contraction:", n1, n2, graph)

    min_cut = len(graph[list(graph.keys())[0]])
    return min_cut




if __name__ == "__main__":

    count_cuts = []
    for i in range(1000):
        graph = build_graph('graph_ex.txt')
        #print(graph)
        count_cuts.append(compute_min_cut(graph))

    print("Min cut list =", count_cuts)
    print("Min cut =", min(count_cuts))
