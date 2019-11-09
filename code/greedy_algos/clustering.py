import heapq

def read_input(f):

    line_no = 0
    edge_list = []
    with open(f) as fp:
        for line in fp:
            x = line.rstrip("\n")
            if line_no == 0:
                num_nodes = int(x)
                line_no += 1
            else:
                y = x.split(" ")
                tup = (int(y[2]), int(y[0]), int(y[1]))  # (cost, node1, node2)
                edge_list.append(tup)

    return num_nodes, edge_list

def single_link_clustering(edge_list, num_nodes, num_clusters):

    node_to_cindex = {}
    cindex_to_elements = {}
    ccount = num_nodes

    # Initialization
    for i in range(1, num_nodes+1):
        node_to_cindex[i] = i
        cindex_to_elements[i] = {i}

    # Add all edges to heap
    heapq.heapify(edge_list)

    while ccount > num_clusters:
        e = heapq.heappop(edge_list)

        n1 = e[1]
        n2 = e[2]
        ind1 = node_to_cindex[n1]
        ind2 = node_to_cindex[n2]
        # check if valid edge
        if   ind1 == ind2:
            continue
        else:
            # Update cluster index
            for val in cindex_to_elements[ind2]:
                node_to_cindex[val] = ind1

            # merge members of clusters
            cindex_to_elements[ind1] = cindex_to_elements[ind1].union(cindex_to_elements[ind2])
            del cindex_to_elements[ind2]
            ccount -= 1

    print(edge_list)
    while True:
        e = heapq.heappop(edge_list)
        if node_to_cindex[e[1]] != node_to_cindex[e[2]]:
            max_distance = e[0]
            break

    return max_distance, cindex_to_elements


def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/clustering1.txt'

    [n, edge_list] = read_input(f)
    print("Number of nodes=", n)
    #print("edge list =", edge_list)

    max_dis, clusters = single_link_clustering(edge_list, n, 4)
    print("Clusters: ", clusters)
    print("Max distance", max_dis)

if __name__ == '__main__':

    test_read_input()
