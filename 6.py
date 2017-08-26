def euler_6(n):
    prod1 = (n*(n+1))/2
    prod2 = (3*(n ** 2) - n -2)/6

    return prod1*prod2


if __name__ == '__main__':
    print(euler_6(100))