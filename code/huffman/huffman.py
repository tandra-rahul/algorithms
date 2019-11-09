import heapq


def huffman_code(l):

    n = len(l)  # number of codewords
    d = [None]*n
    code ={}
    h = [None]*n
    for k in range(0, n):
        d[k] = 0
        code[k] = []
        h[k] = (l[k], [k])

    # initialize heap
    heapq.heapify(h)

    while (len(h) > 1):

        a1 = heapq.heappop(h)
        a2 = heapq.heappop(h)

        for i in a1[1]:
            d[i] += 1
            code[i].append('0')

        for j in a2[1]:
            d[j] += 1
            code[j].append('1')



        p = a1[0] + a2[0]
        n = (p, a1[1] + a2[1])

        heapq.heappush(h, n)

    l_avg = compute_ave_length(d, l)

    return l_avg, d, code

def compute_ave_length(d, l):

    alen = 0
    s = 0

    for n in range(0, len(l)):
        alen += l[n]*d[n]
        s += l[n]

    return float(alen)/float(s)



def read_input(filename):

    nodes = []
    line_no = 0
    with open(filename) as fp:
        for line in fp:
            x = line.rstrip("\n")
            if line_no == 0:
                num_nodes = int(x)
                line_no = 1
            else:
                nodes.append(float(x))

    return nodes

def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/huffman_ex.txt'

    nodes = read_input(f)
    print("Nodes =", nodes)

def test_huffman_code():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/huffman.txt'
    nodes = read_input(f)

    [lavg, d, c] = huffman_code(nodes)
    print("Depth", d)
    print("Average codword length =", lavg)
    print("Minimum codeword length =", min(d))
    print("Maximum codeword length =", max(d))
    #for node in list(c.keys()):
    #    print("Code =", node, c[node])




if __name__ == '__main__':

    #test_read_input()

    test_huffman_code()
