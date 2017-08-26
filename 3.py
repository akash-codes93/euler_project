from math import floor, sqrt
from generator import natural_steps


def euler_3(n):

    factors = list()

    if n %2 == 0 and n !=2:
        factors.append(2)

    for i in natural_steps(3, int(floor(sqrt(n))), 2):
        if n % i == 0:
            if len(euler_3(i)) == 0:
                factors.append(i)

    return factors

if __name__ == '__main__':
    print(euler_3(600851475143)[-1])