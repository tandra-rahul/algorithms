import time


def makeset(x):

    ### Initializes set of objects into a union_find structure
    n = len(x)
    A = [None]*n
    rank = [None]*n
    Aindex = {}

    for i in range(0, n):
        A[i] = i
        rank[i] = 0
        Aindex[x[i]] = i

    return A, rank, Aindex

def find(x, A, rank, Aindex):

    ind = Aindex[x]
    while A[ind] != ind:
        ind = A[ind]

    return ind

def union(x, y, A, rank, Aindex):

    indx = find(x, A, rank, Aindex)
    indy = find(y, A, rank, Aindex)

    if rank[indx] < rank[indy]:
        A[indx] = indy
    elif rank[indx] > rank[indy]:
        A[indy] = indx
    else:
        A[indx] = indy
        rank[indy] += 1

def read_input(f):

    elements = []
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
                elements.append(int(x,2))

    return elements, b

def ham_cluster(elements, b):

    A, rank, Aindex = makeset(elements)
    ccount = len(list(Aindex.keys()))

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
        for c1 in list(Aindex.keys()):
            ind1 = find(c1, A, rank, Aindex)
            c_new = c1^c_ref   # xor operation
            if c_new in Aindex:
                ind2 = find(c_new, A, rank, Aindex)
                if   ind1 == ind2:
                    continue
                else:
                    union(c1, c_new, A, rank, Aindex)
                    ccount -= 1

    print("Cluster count", ccount)





def hamming_clustering(d, n, b):

    cindex = {}
    celements = {}
    ccount = len(list(d.keys()))

    # Initialization
    for i in list(d.keys()):
        cindex[i] = i
        celements[i] = [i]

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
            c_new = c1^c_ref   # xor operation
            if c_new in d:
                ind2 = cindex[c_new]
                if   ind1 == ind2:
                    continue
                else:
                    # Update cluster index
                    for val in celements[c_new]:
                        cindex[val] = ind1

                    # merge members of clusters
                    celements[ind1] = celements[ind1].append(celements[ind2])
                    del celements[ind2]
                    ccount -= 1
    print(ccount)
    #print("Cindex ", cindex)
    #print("Celements", celements)





def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/clustering_big.txt'

    elements, b = read_input(f)
    #print(d, n ,b)
    #print(elements)
    ham_cluster(elements, b)

#    [cindex, s] =hamming_clustering(d, n, b)
#    print(len(s))


if __name__ == '__main__':

    start = time.time()
    test_read_input()
    end = time.time()
    print("Total time =", end - start)
