from math import floor, sqrt
from generator import natural_steps

#optimised approach

def euler_3_opt(n):
    num = n
    largest = 0
    counter = 2
    while counter*counter <= num:
        if num % counter == 0:
            largest = counter
            num /= counter
        else:
            counter += 1

    if num > largest:
        largest = num

    return largest


# brute force Approach
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