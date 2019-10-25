
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

def test_build_graph_from_edges():

    threading.stack_size(67108864)
    #sys.setrecursionlimit(2 ** 20)
    #resource.setrlimit(resource.RLIMIT_STACK, (10**10, 10**10))
    thread = threading.Thread(target=test_build_graph_from_edges)
    thread.start()

    sys.setrecursionlimit(800000)
    resource.setrlimit(resource.RLIMIT_STACK, (2**21, 2**22))

    filename = ("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/scc.txt")

    print("Recursion Limit", sys.getrecursionlimit())

    G = build_graph_from_edges(filename)
    print(G['472856'])
    [leaders, scc_count] = commpute_scc(G)
    print("SCCs =", scc_count)

def commpute_scc(G):

    #print("Original graph:", G)
    n = len(list(G.keys()))
    order =  [str(x) for x in range( 1, n+1)]

    graph_reversal(G)
    print("graph reversal done")
    #print("Reversed Graph:", G)
    [final_order, temp] = dfs_loop(G, order)
    #print("Final order in reverse DFS pass:", final_order)
    graph_reversal(G)
    #print("Get back original graph:", G)
    [temp, leader] = dfs_loop(G, final_order)

    scc_count = group_sccs(leader)

    return leader, scc_count

def dfs_loop(G, order):

    visited = {}
    for node in list(G.keys()):
        visited[node] = False

    n = len(list(G.keys()))

    finish_order = [None] * n
    index = 0
    leader = {}

    for node in reversed(order):
        leader_node = node
        if visited[node] == False:
            index = dfs_rec_scc(G, node, visited, finish_order, leader, leader_node, index)

    return finish_order, leader

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

def test_scc():

    G = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/test_dfs_loop.txt")
    [leaders, scc_count] = commpute_scc(G)
    print("SCCs =", scc_count)

def test_dfs_loop():

    G = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/test_dfs_loop.txt")
    n = len(list(G.keys()))
    print("Original Graph:", G)
    print("Number of nodes =", n)

    graph_reversal(G)

    order = ['2', '4', '5', '1', '3', '6']
    #order =  [str(x) for x in range( 1, n+1)]

    print("order:", order)
    print("Reversed Graph:", G)
    print("Finish order:", dfs_loop(G, order))



def graph_reversal(G):

    degree = {}   # out degree of nodes
    for node in list(G.keys()):
        degree[node] = len(G[node])

    for node in list(G.keys()):
        for v in G[node][: degree[node]]:
            G[v].append(node)
        del G[node][: degree[node]]

def test_graph_reversal():

    G = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/graph_rev_test.txt")
    print(G)
    graph_reversal(G)
    print("Reversed graph:", G)


def topological_order(G):

    # Assumes G is DAG
    n = len(list(G.keys()))   # Number of nodes in graph

    top_order = [None] * n
    index = n

    while index > 0:
        v = find_sink(G)
        print("Sink vertex:", v)
        top_order[index  -1] = v
        remove_sink(G, v)
        print("G:", G)
        index -= 1

    return top_order

def topological_order_dfs(G):

    n = len(list(G.keys()))    # number of nodes
    top_order = [None]* n
    index = n

    visited = {}
    for node in list(G.keys()):
        visited[node] = False

    for node in list(G.keys()):
        if visited[node] == False:
            index = dfs_top_order(G, node, visited, index, top_order)

    return top_order


def dfs_top_order(G, start, visited, index, top_order):
    print("Running DSF function with following parameters:")
    print("start vertex:", start)
    print("Index:", index)
    print("Visited:",visited)
    #print("visited =", visited)
    visited[start] = True
    for node in G[start]:
        if visited[node] == False:
            #print("Node not sink", node)
            visited[node] = True
            index = dfs_top_order(G, node, visited, index, top_order)


    top_order[index - 1] = start
    index -= 1

    return index


def find_sink(G):

    for node in list(G.keys()):
        if len(G[node]) == 0:
            return node

def remove_sink(G, v):

    for node in list(G.keys()):
        print("Node:", node)
        if v in G[node]: G[node].remove(v)
    del G[v]
    print("G after delete", G)



def bfs(graph, v):

    # Initialize all vertices are un-explored
    is_explored = {}
    dist = {}        # distance from source vertex
    for ver in graph.keys():
        is_explored[ver] = False
        dist[ver] = float("inf")


    queue = [v]    # used as queue
    bfs_order = []   # Final Breadth first search ordering
    is_explored[v] = True
    dist[v] = 0

    while len(queue) > 0:
        s = queue.pop(0)
        bfs_order.append(s)

        for w in graph[s]:
            if is_explored[w] == False:
                is_explored[w] = True
                queue.append(w)
                dist[w] = dist[s] + 1


    return bfs_order, dist


def dfs(graph, v):

    #Initialization
    stack = [v]
    visited = {}
    dfs_order = []

    for node in list(graph.keys()):
        if node != v:
            visited[node] = False
        else:
            visited[node] = True

    while len(stack) > 0:
        s = stack.pop()
        dfs_order.append(s)
        for v in graph[s]:
            if visited[v] == False:
                visited[v] = True
                stack.append(v)

    return dfs_order

def dfs_rec_out(graph, v):

    #Initialization
    visited = {}
    dfs_order = []

    for node in graph.keys():
        if node != v:
            visited[node] = False
        else:
            visited[node] = True

    dfs_rec(graph, v, visited, dfs_order)

    return dfs_order

def dfs_rec(graph, w, visited, dfs_order):


    dfs_order.append(w)

    for node in graph[w]:
        if visited[node] == False:
            visited[node] = True
            print(visited)
            dfs_rec(graph, node, visited, dfs_order)


def build_graph(filename):

    graph = {}
    with open(filename) as fp:
        for line in fp:
            #create_dict(line.rstrip("\n"), graph)
            x = line.rstrip("\n").split(" ")
            graph[x[0]] = x[1:]

    #print(graph)
    return graph

def bfs_test(graph, v):

    print("Graph:", graph)
    print("Vertex:", v)

    [bfs_order, dist] = bfs(graph, v)
    print("BFS order", bfs_order, dist)

def dfs_test(graph,v):
    print("Graph:", graph)
    print("Vertex:", v)

    dfs_order = dfs(graph, v)
    print("DFS order", dfs_order)

def dfs_rec_test(graph,v):
    print("Graph:", graph)
    print("Vertex:", v)

    dfs_order = dfs_rec_out(graph, v)
    print("DFS order", dfs_order)

def test_top_order():

    G = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/top_order_ex2.txt")
    print(G)
    #print("Topological order:", topological_order(G))
    print("Topological order:", topological_order_dfs(G))

if __name__ == '__main__':

    # graph = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/inputs/test_graph.txt")
    # v = list(graph.keys())[0]
    #
    # print("BFS test ----- ")
    # bfs_test(graph, v)
    #
    # print("DFS test ----- ")
    # dfs_test(graph, v)
    #
    # print("DFS Recursive test ----- ")
    # dfs_rec_test(graph,v)
    #test_top_order()

    #test_graph_reversal()

    #test_dfs_loop()
    #test_scc()

    test_build_graph_from_edges()
