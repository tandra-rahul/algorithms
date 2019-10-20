
import random
#from ..utils.utils import build_graph

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


if __name__ == '__main__':

    graph = build_graph("/Users/rahul/Coursera/Algorithms/coursera_stanford/inputs/test_graph.txt")
    v = list(graph.keys())[0]

    print("BFS test ----- ")
    bfs_test(graph, v)

    print("DFS test ----- ")
    dfs_test(graph, v)

    print("DFS Recursive test ----- ")
    dfs_rec_test(graph,v)
