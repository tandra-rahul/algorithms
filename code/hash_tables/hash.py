import time


def read_input(file):

    l = []
    with open(file) as fp:
        for line in fp:
            l.append(float(line.rstrip("/n")))

    return l


def two_sum_hash(l, nmin, nmax):

    ldict = {}
    for i in l:
        ldict[i] = i

    count = 0

    for t in range(nmin, nmax +1):
        if does_two_sum_exist(l, ldict, t):
            count +=1

    return count

def two_sum(l, nmin, nmax):

    # First sort list
    l.sort()
    #print("sorted =", l)
    count = 0

    for t in range(nmin, nmax+1):

        if does_two_sum_exist(l, t):
            count += 1

    return count

def does_two_sum_exist(l, ldict, t):

    for i in l:
        x = t - i
        if (x != i) and (x in ldict):
            return True

    return False

def test_two_sum_hash():

    file = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/2sum.txt'
    l = read_input(file)
    #print("Original list:", l)
    nmin = -10000
    nmax = 10000
    start = time.time()
    count = two_sum_hash(l, nmin, nmax)
    print("Number of hits:", count)
    end = time.time()

    print("Elapsed time =", end - start)


def test_two_sum():

    file = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/2sum.txt'
    l = read_input(file)
    #print("Original list:", l)
    nmin = -10000
    nmax = 10000
    count = two_sum(l, nmin, nmax)
    print("Number of hits:", count)

def test_read_input():

    file = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/2sum_test.txt'
    print(read_input(file))

if __name__ == '__main__':

    #test_read_input()
    #test_two_sum()
    test_two_sum_hash()
