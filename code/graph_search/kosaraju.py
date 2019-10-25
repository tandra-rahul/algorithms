import random
import sys
import threading
#from ..utils.utils import build_graph
import resource

def build_graph_from_edges(file):

    graph = {}

    with open(file) as fp:
        for line in fp:
            x = line.rstrip("\n").split(" ")
            if x[0] in graph:
                graph[x[0]].append(x[1])
            else:
                graph[x[0]] = [x[1]]

    for i in range(1, 875714):
        if str(i) not in graph:
            graph[str(i)] = []

    return graph

def commpute_scc(G):

    n = len(list(G.keys()))
    order =  [str(x) for x in range( 1, n+1)]

    graph_reversal(G)
    print("First graph reversal done")
    print("Number of nodes in graph after reversal:", len(list(G.keys())))
    [final_order, temp] = dfs_loop(G, order)

    graph_reversal(G)
    print("Second graph reversal done")
    print("Number of nodes in graph after reversal:", len(list(G.keys())))
    [temp, leader] = dfs_loop(G, final_order)

    scc_count = group_sccs(leader)

    return leader, scc_count

def dfs_loop(G, order):

    visited = {}
    for node in list(G.keys()):
        visited[node] = 0

    n = len(list(G.keys()))

    finish_order = []
    index = 0
    leader = {}

    for node in reversed(order):
        leader_node = node
        if visited[node] == 0:
            #index = dfs_rec_scc(G, node, visited, finish_order, leader, leader_node, index)
            dfs(G, node, visited, finish_order, leader, leader_node)

    return finish_order, leader

def dfs(graph, v, visited, finish_order, leader, leader_node):

    #Initialization
    stack = [v]
    visited[v] = 1
    leader[v] = leader_node

    while len(stack) > 0:
        s = stack[-1]      # peek into top of stack
        if visited[s] > 1:
            stack.pop()
            finish_order.append(s)
        else:
            for node in graph[s]:
                if visited[node] == 0:
                    visited[node] = 1
                    stack.append(node)
                    leader[node] = leader_node
            visited[s] = 2

def dfs_rec_scc(G, node, visited, finish_order, leader,leader_node, index):

    visited[node] = True
    leader[node] = leader_node
    for n in G[node]:
        if visited[n] == False:
            dfs_rec_scc(G, n, visited, finish_order, leader, leader_node, index)

    finish_order[index] = node
    index += 1
    return index

def group_sccs(leader):

    scc_count = {}
    for node in list(leader.keys()):
        if leader[node] in scc_count:
            scc_count[leader[node]] += 1
        else:
            scc_count[leader[node]] = 1

    return scc_count


def build_graph(filename):

    graph = {}
    with open(filename) as fp:
        for line in fp:
            #create_dict(line.rstrip("\n"), graph)
            x = line.rstrip("\n").split(" ")
            graph[x[0]] = x[1:]

    #print(graph)
    return graph

def graph_reversal(G):

    degree = {}   # out degree of nodes
    for node in list(G.keys()):
        degree[node] = len(G[node])

    for node in list(G.keys()):
        for v in G[node][: degree[node]]:
            G[v].append(node)
        del G[node][: degree[node]]

def test_build_graph_from_edges():

    filename = ("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/scc.txt")

    G = build_graph_from_edges(filename)
    n = len(list(G.keys()))
    print("Building graph done. Number of nodes =", n)
    print(G['650962'])
    [leaders, scc_count] = commpute_scc(G)
    print(sorted(scc_count.items(), key=lambda x: x[1]))
    #print(scc_count['650962'])
    #print("SCCs =", scc_count)

def test_dfs_loop():

    G = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/test_dfs_loop.txt")
    n = len(list(G.keys()))
    print("Original Graph:", G)
    print("Number of nodes =", n)

    #graph_reversal(G)

    #order = ['2', '4', '5', '1', '3', '6']
    order =  [str(x) for x in range(1, n+1)]

    print("order:", order)
    #print("Reversed Graph:", G)
    print("Finish order:", dfs_loop(G, order))


if __name__ == '__main__':

    test_build_graph_from_edges()
    #test_dfs_loop()
