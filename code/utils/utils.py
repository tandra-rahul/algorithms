def split_lists(a):

    n = len(a)

    left = a[0:int(n/2)]
    right = a[int(n/2): ]

    return left, right
