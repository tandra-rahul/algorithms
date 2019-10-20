#!user/bin/python3

from merge_sort import merge_sort
from utils import split_lists

def count_inversions(a):

    # Base case
    if len(a) <= 1:
        count = 0
        return count

    left, right = split_lists(a)

    left_count = count_inversions(left)
    right_count = count_inversions(right)
    split_count = count_split_inversions(left, right)
    count =  left_count + right_count + split_count
    return count


def count_split_inversions(left, right):

    count = 0
    left_index = 0
    right_index = 0

    # first sort the two lists
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    while ( (left_index < len(left_sorted)) and (right_index < len(right_sorted)) ):

        if right_sorted[right_index] < left_sorted[left_index]:
            count = count + len(left_sorted[left_index : ])
            right_index += 1
        else:
            left_index += 1

    return count

def test_split_lists():
    a = [1, 4, 6, 2, 0 ,5, 7]

    [left, right] = split_lists(a)
    print("Left:", left)
    print("Right:", right)



if __name__ == '__main__':

    #test_split_lists()

    a = [7, 6, 5, 4, 3, 2, 1]
    print("Num inversions = ", count_inversions(a))

    #Take input from a text file
    lines = [int(line.rstrip('\n')) for line in open('inversions_input.txt')]
    print("Num inversions = ", count_inversions(lines))
