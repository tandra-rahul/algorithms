import time

def read_input(f):

    items = []
    line_no = 0
    with open(f) as fp:
        for line in fp:
            x = line.rstrip("\n").split(" ")
            #print(x)
            if line_no == 0:
                W = int(x[0])
                line_no += 1
            else:
                items.append( (int(x[1]), int(x[0])) )   # (weight, value)

    return items, W

def fast_knapsack(items, W):

    n = len(items)
    A_prev = [None]* (W + 1)  # Proxy for A[w][i-1], w = 0,1,2 ... W
    A_curr = [None]*(W + 1)   # Proxy for A[w][i], w = 0,1,2 ... W

    # Initialization (i = 1)
    for w in range(0, W +1):
        if w < items[0][0]:
            A_prev[w] = 0
        else:
            A_prev[w] = items[0][1]

    # Recursion
    for i in range(1, n):
        #print(i)
        for w in range(0, W +1):
            t1 = A_prev[w]
            if w < items[i][0]:
                t2 = 0
            else:
                t2 = items[i][1] + A_prev[w - items[i][0]]
            #print("t1, t2 =", t1, t2)
            A_curr[w] = max(t1, t2)
        #print(A_prev, A_curr)
        #time.sleep(1)
        A_prev = list.copy(A_curr)

    max_value = A_curr[W]
    return max_value


def compute_optimal_packing(items, W):

    # Assume items are numbered 1,2,3, ... len(items)
    n = len(items)
    A = [None]*n
    for i in range(0, n):
        A[i] = [None]*(W +1)

    # Base case (when number of items is 1)
    for w in range(0, W+1):
        if w < items[0][0]:
            A[0][w] = 0
        else:
            A[0][w] = items[0][1]

    # Recursion
    for i in range(1, n):
        for w in range(0, W+1):
            t1 = A[i-1][w]
            if w < items[i][0]:
                t2 = 0
            else:
                t2 = items[i][1] + A[i-1][w - items[i][0]]

            A[i][w] = max(t1, t2)

    packed_items = return_optimal_packing(items, A, W)
    return A, packed_items

def compute_optimal_packing_v2(items, W):

    # Assume items are numbered 1,2,3, ... len(items)
    n = len(items)
    A = [None]*n

    for i in range(0, n):
        A[i] = [None]*(W +1)

    # Base case (when number of items is 1)
    for w in range(0, W+1):
        if w < items[0][0]:
            A[0][w] = 0
        else:
            A[0][w] = items[0][1]

    # Recursion
    for w in range(0, W+1):
        for i in range(1, n):
            t1 = A[i-1][w]
            if w < items[i][0]:
                t2 = 0
            else:
                t2 = items[i][1] + A[i-1][w - items[i][0]]

            A[i][w] = max(t1, t2)

    packed_items = return_optimal_packing(items, A, W)
    return A, packed_items

def return_optimal_packing(items, A, W):

    # Returning the list of packed items
    n = len(items)
    i = n -1
    w = W
    packed_items=[]

    while (i >=0) and (w > 0):
        if (i == 0):
            if (w >= items[0][0]):
                packed_items.append(items[i])
                i -= 1
                w -= items[0][0]
            else:
                i -= 1
        elif (A[i][w] != A[i-1][w]):
            packed_items.append(items[i])
            i -= 1
            w -= items[i][0]
        else:
            i -= 1

    return packed_items





def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/knapsack1.txt'

    [items, W] = read_input(f)

    print("Total capacity:", W)
    #print("Items =", items)
    [A, packed_items] = compute_optimal_packing(items, W)
    #print("Packing matrix", A)
    print("Packed items", packed_items)
    print("Optimal value", A[-1][-1])

def test_fast_knapsack():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/knapsack1.txt'
    [items, W] = read_input(f)
    print("Total capacity:", W)

    max_value = fast_knapsack(items, W)
    print("Max value =", max_value)


if __name__ == '__main__':

    #test_read_input()
    test_fast_knapsack()
