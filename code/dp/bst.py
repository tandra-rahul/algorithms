def read_input(f):

    probs = []
    with open(f) as fp:
        for line in fp:
            probs.append(int(line.rstrip("\n")))

    return probs

def compute_optimal_bst(probs):

    n = len(probs)
    c = [None]*n
    for s in range(0,n):
        c[s] = [None]*n

    # Base case, s=0
    for i in range(0, n):
        c[0][i] = probs[i]

    # Recursing case
    for s in range(1, n):
        for i in range(0, n - s):
            temp = [None] * (s+1)
            for r in range(0, s+1):
                if r == 0:
                    temp[r] = sum(probs[i:i+s+1]) + c[s-1][i+1]
                elif r == s:
                    temp[r] = sum(probs[i:i+s+1]) + c[s-1][i]
                else:
                    temp[r] = sum(probs[i:i+s+1]) + c[r-1][i] + c[s-r-1][i+r+1]

            temp_min = min(temp)
            c[s][i] = temp_min

    return c



def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/opt_bst.txt'

    probs = read_input(f)
    print(probs)
    c = compute_optimal_bst(probs)
    print("cost matrix", c)
    print("Optimal sol =", c[-1][0])


if __name__ == '__main__':

    test_read_input()
