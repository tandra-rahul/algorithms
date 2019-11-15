import time


def read_input(f):

    dindex = {}
    delement = {}
    line_no = 0
    with open(f) as fp:
        for line in fp:
            x = line.rstrip("\n")
            #print(x)
            if line_no == 0:
                x = x.split(" ")
                n = int(x[0])
                b = int(x[1])
                line_no += 1
            else:
                x = x.replace(" ","")
                #print(x)
                #dindex[line_no] = int(x,2)
                delement[int(x,2)] = int(x,2)

                line_no += 1

    return delement, n, b

def hamming_clustering_fast(d, n, b):

    cindex = {}
    ccount = len(list(d.keys()))
    cluster_set = set()

    # Initialization
    for i in list(d.keys()):
        cindex[i] = i

    # Reference hamming distance 1 and 2 codewords
    cref1 = []
    cref2 = []
    for j in range(0,b):
        cref1.append(2**j)

    for i in range(0,b):
        for j in range(i+1,b):
            cref2.append(2**i+2**j)

    ref_cwords = cref1 + cref2


    for ind,c_ref in enumerate(ref_cwords):
        print(ind)
        for c1 in list(d.keys()):
            ind1 = cindex[c1]
            cluster_set.add(ind1)
            c_new = c1^c_ref   # xor operation
            if c_new in d:
                ind2 = cindex[c_new]
                if   ind1 == ind2:
                    continue
                else:
                    # Update cluster index
                    cindex[c_new] = ind1

    #print(ccount)
    #print("Cindex ", cindex)
    #print("Celements", celements)
    return cindex, cluster_set

def hamming_clustering(d, n, b):

    cindex = {}
    celements = {}
    ccount = len(list(d.keys()))

    # Initialization
    for ind, i in enumerate(list(d.keys())):
        cindex[i] = ind
        celements[ind] = {i}

    # Reference hamming distance 1 and 2 codewords
    cref1 = []
    cref2 = []
    for j in range(0,b):
        cref1.append(2**j)

    for i in range(0,b):
        for j in range(i+1,b):
            cref2.append(2**i+2**j)

    ref_cwords = cref1 + cref2[1:100]


    for ind,c_ref in enumerate(ref_cwords):
        print(ind)
        for c1 in list(d.keys()):
            ind1 = cindex[c1]
            c_new = c1^c_ref   # xor operation
            if c_new in d:
                ind2 = cindex[c_new]
                if   ind1 == ind2:
                    continue
                else:
                    # Update cluster index
                    for val in celements[ind2]:
                        cindex[val] = ind1

                    # merge members of clusters
                    celements[ind1] = celements[ind1].union(celements[ind2])
                    del celements[ind2]
                    ccount -= 1
    print(ccount)
    #print("Cindex ", cindex)
    #print("Celements", celements)
    return cindex, celements





def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/clustering_big.txt'

    [d, n, b] = read_input(f)
    #print(d, n ,b)
    print(len(list(d.keys())))
    [cindex, s] = hamming_clustering(d, n, b)
    print(len(s))


if __name__ == '__main__':

    start = time.time()
    test_read_input()
    end = time.time()
    print("Total time =", end - start)
