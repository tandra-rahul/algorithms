def read_input(f):

    line_no = 0
    with open(f) as fp:
        for line in fp:
            x = line.rstrip("\n")
            if line_no == 0:
                y = x.split(" ")
                agap = float(y[0])
                amiss = float(y[1])
                line_no = 1
            elif line_no == 1:
                 seqx = list(x)
                 line_no = 2
            else:
                 seqy = list(x)

    return seqx, seqy,agap, amiss

def compute_opt_alignment(x, y, agap, amiss):

    m = len(x)
    n = len(y)

    P = [None] * (m +1)
    for i in range(0, m+1):
        P[i] = [None]*(n+1)

    # Base cases
    for j in range(0, n + 1):
        P[0][j] = j * agap

    for i in range(0, m+1):
        P[i][0] = i * agap

    # recursion
    for i in range(1, m+1):
        for j in range(1, n+1):
            t1 = P[i][j-1] + agap
            t2 = P[i-1][j] + agap
            if x[i-1] == y[j-1]:
                t3 = P[i-1][j-1]
            else:
                t3 = P[i-1][j-1] + amiss
            P[i][j] = min(t1, t2, t3)

    [xopt, yopt] = opt_alignment(P, x, y, agap, amiss)
    return P, xopt, yopt

def opt_alignment(P, x, y, agap, amiss):

    m = len(x)
    n = len(y)
    optx = []
    opty = []

    i = m
    j = n

    while (i > 0) or (j > 0):

        if (i == 0):
            opty.append('-')
            j -= 1
            continue

        if (j == 0):
            optx.append('-')
            i -= 1
            continue

        if P[i][j] == P[i][j-1] + agap:
            optx.append('-')
            opty.append(y[j-1])
            j -= 1
        elif P[i][j] == P[i-1][j] + agap:
            optx.append(x[i-1])
            opty.append('-')
            i -= 1
        else:
            optx.append(x[i-1])
            opty.append(y[j-1])
            i -= 1
            j -= 1

    return optx, opty

def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/sequence.txt'

    [x, y, agap, amiss] = read_input(f)
    print("Seq X =", x)
    print("Seq Y =", y)
    print("Gap penalty =", agap)
    print("Miss penalty =", amiss)

    [P, xopt, yopt] = compute_opt_alignment(x, y, agap, amiss)
    print("Optimal penalty =", P[-1][-1])
    print("Optimal X =", xopt)
    print("Optimal Y =", yopt)

if __name__ == '__main__':

    test_read_input()
