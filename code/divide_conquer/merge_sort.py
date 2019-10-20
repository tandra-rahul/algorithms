#!user/bin/python3

def merge_sort(a):

    n = len(a)
    if n == 1:
        return a
    else:
        left = a[0 : int(n/2)]
        right = a[int(n/2) : ]

        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        sorted_array = merge_left_right(left_sorted, right_sorted)
        return sorted_array


def merge_left_right(a, b):

    left_index = 0
    right_index = 0
    index = 0

    n = len(a) + len(b)
    sorted_list = [None]*n

    while (index < n):
        if left_index >= len(a):
            sorted_list[index : ] = b[right_index : ]
            return sorted_list

        if right_index >= len(b):
            sorted_list[index : ] = a[left_index : ]
            return sorted_list

        if a[left_index] <= b[right_index]:
            sorted_list[index] = a[left_index]
            left_index += 1
        else:
            sorted_list[index] = b[right_index]
            right_index += 1

        index += 1

    return sorted_list

if __name__ == "__main__":

    A = [ 1, 9, 2, 14, 3, 10, 11, 4, 6, 25, -2, -4]
    a = merge_sort(A)

    #a = merge_left_right([1, 4, 15], [2, 3, 6, 7, 10])
    print("Sorted list", a)
