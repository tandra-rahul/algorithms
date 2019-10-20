import statistics

def quick_sort(a, comp_count, pivot_type):

    comp_count += len(a) - 1
    #print("Array =", a)
    #print("Count =", comp_count)

    #base case
    if len(a) == 1:
        return a, comp_count

    # Pre-processing step
    if pivot_type == 'last':
        temp = a[0]
        a[0] = a[len(a) -1]
        a[len(a) -1] = temp
    elif pivot_type == 'median3':
        middle = find_middle(a)
        f = [a[0], a[-1], a[middle] ]
        med = statistics.median(f)

        if a[int(middle)] == med:
            temp = a[0]
            a[0] = a[middle]
            a[middle] = temp
        elif a[-1] == med:
            temp = a[0]
            a[0] = a[-1]
            a[-1] = temp

    #partition subroutine
    partition_index = partition(a)

    #recursive calls
    if len(a[:partition_index]) > 0:
        [a_left, comp_count] = quick_sort(a[:partition_index], comp_count, pivot_type)
        #print("Count =", comp_count)
        a[:partition_index] = a_left

    if len(a[partition_index +1 :]) > 0:
        [a_right, comp_count] = quick_sort(a[partition_index +1 :], comp_count, pivot_type)
        #print("Count =", comp_count)
        a[partition_index +1 :] = a_right

    return a, comp_count

def partition(a):

    #pick pivot element
    p = a[0]
    partition_index = 0
    index_new = 1

    while index_new < len(a):
        if a[index_new] <= p:
            partition_index += 1
            # Perform swap
            if partition_index != index_new:
                temp = a[partition_index]
                a[partition_index] = a[index_new]
                a[index_new] = temp

        index_new += 1
    #swap pivot element
    a[0] = a[partition_index]
    a[partition_index] = p
    return partition_index

def find_middle(a):
    if len(a)%2 == 0:
        middle = int(len(a)/2 -1)
    else:
        middle = int((len(a)-1)/2)

    return middle


if __name__ == '__main__':

    pivot_type = 'median3'
    # a= [6, 4, 5, 2, 9, 7, 10, 15, 3, 1]
    # comp_count = 0
    # #print("Array before partition =", a)
    # [a , comp_count] = quick_sort(a, 0, pivot_type)
    # #print("Array after partition =", a)
    # print("Total count =", comp_count)

    #Take input from a text file
    pivot_type = 'median3'
    lines = [int(line.rstrip('\n')) for line in open('quick_sort_input.txt')]
    print(len(lines))
    print(lines[0], lines[-1])
    [lines_sorted , count_zero] = quick_sort(lines, 0, pivot_type)
    print("First element as pivot comparison count: ", count_zero )
