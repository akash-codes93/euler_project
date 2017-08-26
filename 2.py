from generator import febonacci


def euler_2(n):
    return sum([i for i in febonacci(1,2,n) if i%2==0])


if __name__ == '__main__':
    print(euler_2(4000000))
