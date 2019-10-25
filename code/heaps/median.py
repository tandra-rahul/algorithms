import heapq
import os
import statistics

def read_file(filename):

    input_list = []
    with open(filename) as fp:
        for line in fp:
            input_list.append(int(line.rstrip("/n")))

    return input_list

def maintain_median_slow(l):

    med = []
    for ind,val in enumerate(l):
        m = statistics.median_low(l[0:ind+1])
        med.append(m)

    return med, sum(med)

def maintain_median(input_list):

    lheap = []
    rheap = []
    median = []

    for (ind, val) in enumerate(input_list):

        if ind == 0:
            lheap.append(-1*val)    # stores negative values
            median.append(val)
        elif ind == 1:
            if val > input_list[0]:
                rheap.append(val)
            else:
                temp = -1 * lheap.pop(0)
                lheap.append(-1*val)
                rheap.append(temp)
            median.append(-1*lheap[0])
        else:
            #print(ind, lheap, rheap, val)
            heapq.heapify(lheap)
            heapq.heapify(rheap)
            lmax = -1 * heapq.heappop(lheap)
            rmin = heapq.heappop(rheap)

            if not (ind % 2):
                # next element has to go into lheap
                if val < rmin:
                    #print("hi1")
                    heapq.heappush(lheap, -1*val)
                    heapq.heappush(lheap, -1*lmax)
                    heapq.heappush(rheap, rmin)
                else:
                    #print("hi2")
                    heapq.heappush(rheap, val)
                    heapq.heappush(lheap, -1*rmin)
                    heapq.heappush(lheap, -1*lmax)
            else:
                # next element has to go into rheap
                if val > lmax:
                    #print("hi3")
                    heapq.heappush(rheap, val)
                    heapq.heappush(rheap, rmin)
                    heapq.heappush(lheap, -1*lmax)
                else:
                    #print("hi4")
                    heapq.heappush(lheap, -1*val)
                    heapq.heappush(rheap, lmax)
                    heapq.heappush(rheap, rmin)


            med = -1* heapq.heappop(lheap)
            median.append(med)
            heapq.heappush(lheap, -1*med)

    return median,sum(median)


def test_read_file():

    filename = 'median.txt'
    dirname = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs'
    f = os.path.join(dirname, filename)

    l = read_file(f)
    print(l)

def test_maintain_median():

    filename = 'median.txt'
    dirname = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs'
    f = os.path.join(dirname, filename)
    l = read_file(f)
    #print("length of list", len(l))
    #print("Original list:", l)

    m, msum = maintain_median(l)
    print("Running median and sum (fast):", m, msum)

    # m, msum = maintain_median_slow(l)
    # print("Running median and sum (slow):", m, msum)


if __name__ == '__main__':

    #test_read_file()
    test_maintain_median()
