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

    if rank(indx) <= rank(indy):
        A[indx] = indy
    else:
        A[indy] = indx
