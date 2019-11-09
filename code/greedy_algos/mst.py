def read_input(file):

    edge_list = []
    with open(file) as fp:
        for line in fp:
            x = line.rstrip("/n").split(" ")
            #print(len(x))
            if len(x) == 2:
                n = int(x[0])
                m = int(x[1])
            else:
                tup = (float(x[2]), x[0], x[1])
                edge_list.append(tup)

    return edge_list, n, m

def compute_mst(e):

    v = create_vertex_set(e)

    s = set()
    vs = v
    tree = set()
    cost = 0

    s.add(vs.pop())   #pick a random element
    #print("initial conditions:", s, vs)

    while len(vs) > 0:

        #pick all valid edges to compute min
        min_edge_list = []
        for edge in e:
            test_set = {edge[1], edge[2]}
            #print("Test set:", test_set)
            if len(test_set.intersection(s)) == 1:
                min_edge_list.append(edge)

        # Find minimum
        #print("Min edge list", min_edge_list)
        min_edge = min(min_edge_list)
        min_edge_verts = {min_edge[1], min_edge[2]}
        #print("Min edge", min_edge)
        #print("Min Edge vers", min_edge_verts)

        tree.add(min_edge)
        cost += min_edge[0]

        s.update(min_edge_verts)
        vs = vs.difference(min_edge_verts)
        #print("S", s)
        #print( "VS", vs)

    return tree, cost



def create_vertex_set(e):

    v = set()

    for edge in e:
        v.update({edge[1], edge[2]})

    return v

def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/edges.txt'

    e, n, m = read_input(f)

    [tree, cost] = compute_mst(e)

    #print(e, n, m)
    #print("Min Spanning tree", tree)
    print("Cost", cost)

if __name__ == '__main__':

    test_read_input()
