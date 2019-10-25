import heapq


def build_graph_from_file(filename):

    G = {}
    with open(filename) as fp:
        for line in fp:
            x = line.split("\t")[:-1]
            G[x[0]]={}
            for i in x[1:]:
                G[x[0]][i.split(",")[0]] = int(i.split(",")[1])

    return G

def dijkstra_slow(G, source):

    # Initialize
    ds_vis = {}
    ds_unvis = {}

    for node in list(G.keys()):
        if node != source:
            ds_unvis[node] = 1000000
        else:
            ds_vis[node] = 0

    recent = source  #Most recently found vertex

    while ds_unvis:   # while non-empty
        for node in G[recent]:
            if node not in ds_vis:
                #print("source,dest:", recent, node, G[recent][node])
                #print("Visited", ds_vis)
                #print("Unvisited", ds_unvis)
                updated_dis = ds_vis[recent] + G[recent][node]
                ds_unvis[node] = min(ds_unvis[node], updated_dis)

        # find node with mininum dijkstra score
        [min_node, min_score] = find_min(ds_unvis)
        del ds_unvis[min_node]
        ds_vis[min_node] = min_score
        recent = min_node

    return ds_vis

def find_min(my_dict):

    # Find key with minimum value in dictionary

    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
    min_val = my_dict[key_min]

    return key_min, min_val





def dijkstra(G, source):

    nodes = []
    visited = {}
    visited[source] = True
    sp ={}
    for node in list(G.keys()):
        if node != source:
            sp[node] = 1000000
        else:
            sp[node] = 0

    for node in list(G.keys()):
        if node != source:
            visited[node] = False
            nodes.append((1000000, node))

    heapq.heapify(nodes)

    recent = (0, source)
    #while len(nodes) > 0:
    for k in range(0, len(nodes)):
        #print(len(nodes))
        for node in G[recent[1]]:
            if visited[node[0]] == False:
                new_distance = recent[0] + node[1]
                #print(new_distance)
                heapq.heappush(nodes, (new_distance, node[0]))

        (dist, pop_node) = heapq.heappop(nodes)
        #print(dist, pop_node)
        visited[pop_node] = True
        recent = (dist, pop_node)
        sp[pop_node] = dist

    return sp



def test_build_graph_from_edges():

    file = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/dd.txt'
    G = build_graph_from_file(file)
    #print("Graph:", G['1'])
    source = '1'
    sp = dijkstra_slow(G, source)

    inp = [7,37,59,82,99,115,133,165,188,197]
    dis_inp = []
    for node in inp:
        dis_inp.append(sp[str(node)])
        #print("Node, SP:", str(node), sp[str(node)])

    print(dis_inp)


if __name__ == '__main__':

    test_build_graph_from_edges()
