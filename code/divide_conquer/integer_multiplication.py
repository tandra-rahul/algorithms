
from utils import split_lists


def multiply_ints_recursive(a, b):
    # Assume the digits of the integers are input as split_lists

    if (len(a) == 0) or (len(b) == 0):
        return 0

    if (len(a) == 1) and (len(b) == 1):
        return a[0]*b[0]

    [a_l, a_r] = split_lists(a)
    [b_l, b_r] = split_lists(b)

    p1 = multiply_ints_recursive(a_l, b_l)
    p2 = multiply_ints_recursive(a_l, b_r)
    p3 = multiply_ints_recursive(b_l, a_r)
    p4 = multiply_ints_recursive(a_r, b_r)

    t1 = p1* (10**(len(a_r) + len(b_r)))
    t2 = p2* (10**(len(b_r)))
    t3 = p3* (10**(len(a_r)))
    t4 = p4

    prod = t1 + t2 + t3 + t4

    return prod

def test_multiply_ints(x, y):

    a = get_digits(x)
    b = get_digits(y)

    prod1 = multiply_ints_recursive(a, b)
    prod2 = int(x)*int(y)

    return (prod1 - prod2)


def get_digits(n):
    digits = [int(x) for x in str(n)]
    return digits


if __name__ == '__main__':
    x = '3141592653589793238462643383279502884197169399375105820974944592'
    y = '2718281828459045235360287471352662497757247093699959574966967627'

    a = get_digits(x)
    b = get_digits(y)

    print(test_multiply_ints(x, y))

    #c = multiply_ints_recursive(a, b)
    #print("Product =", c)
