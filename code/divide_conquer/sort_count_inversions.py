def read_input(f):

    x = []
    with open(f) as fp:
        for line in fp:
            y = line.rstrip("\n")
            x.append(int(y))

    return x

def split_lists(a):

    n = len(a)

    left = a[0:int(n/2)]
    right = a[int(n/2): ]

    return left, right

def sort_count_split(lsorted, rsorted):

    n = len(lsorted) + len(rsorted)
    out = [None]*n

    ind = 0
    lind = 0
    rind = 0
    count = 0

    while ind < n:
        if lind > len(lsorted) - 1:
            out[ind: ] = rsorted[rind: ]
            break

        if rind > len(rsorted) - 1:
            out[ind: ] = lsorted[lind: ]
            break

        if rsorted[rind] < lsorted[lind]:
            out[ind] = rsorted[rind]
            ind += 1
            rind += 1
            count += len(lsorted) - lind
        else:
            out[ind] = lsorted[lind]
            ind += 1
            lind += 1

    return out, count



def sort_count(x):

    if len(x) <= 1:
        sorted_out = x
        total_count = 0
        return sorted_out, total_count

    left, right = split_lists(x)

    lsorted, lcount = sort_count(left)
    print("lcount", lcount)
    rsorted, rcount = sort_count(right)
    print("rcount", rcount)

    sorted_out, split_count = sort_count_split(lsorted, rsorted)
    #print("left", lsorted)
    #print("right", rsorted)
    #print("scount", split_count)
    total_count = lcount + rcount + split_count

    return sorted_out, total_count





def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/inversions.txt'

    inp = read_input(f)
    print("input list:", inp)

    sorted_out, count = sort_count(inp)

    print("sorted array:", sorted_out)
    print("total inversions:", count)

if __name__ == '__main__':

    test_read_input()
