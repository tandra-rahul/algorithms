def read_input(f):

    x = []
    line_no = 0
    with open(f) as fp:
        for line in fp:
            y = line.rstrip("/n")
            if line_no == 0:
                num_nodes = int(y)
                line_no += 1
            else:
                x.append( int(y))

    return x

def compute_wis(s):

    W = [None] * len(s)

    # Base cases
    W[0] = s[0]
    W[1] = max(W[0], s[1])

    # Recursion
    for i in range(2,len(s)):
        W[i] = max(W[i-1], s[i] + W[i-2])

    # Printing the max set
    # Assume that nodes are numbered 1,2,3, ... n

    max_wis = {}
    for i in range(1, len(s) +1):
        max_wis[i] = 0

    j = len(s) - 1
    while j >= 1:
        if W[j] != W[j -1]:
            max_wis[j+1] = 1
            j -= 2
        else:
            j -= 1

    if max_wis[2] == 0:
        max_wis[1] = 1

    return W[-1], max_wis

def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/mwis.txt'

    s = read_input(f)
    #print(s)
    W, max_wis = compute_wis(s)
    print("Max weight =", W)
    print("Max weight set =", max_wis)
    test_nodes = [1, 2, 3, 4, 17, 117, 517, 997]
    for i in test_nodes:
        print(i, max_wis[i])

if __name__ == '__main__':

    test_read_input()
