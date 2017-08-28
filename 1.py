#custom generator
from generator import natural

# simple approach

def euler_1(n):
    result = 0
    for i in natural(1,n):
        if i%5 == 0 or i%3 == 0:
            result += i

    return result


# alternate approach


def euler_1_alt(n):

    counters = [3,5,15]

    result = 0
    sum_sub = 0

    for t in range(len(counters)):
        main_counter, i = counters[t], counters[t]
        sum_sub = 0
        while(i < n):
            sum_sub += i
            i = i+ main_counter
        if counters[t] == 15:
            result -= sum_sub
        else:
            result += sum_sub

    return result


# optimised approach

def SumDivisbleBy(n, p):
    t = int(p / n)
    return (n * t * (t + 1)) >> 1


def euler_1_opt(n):
    n= n-1
    result = SumDivisbleBy(3, n) + SumDivisbleBy(5, n) - SumDivisbleBy(15, n)
    return result


if __name__ == '__main__':
    #ans 233168
    print(euler_1_opt(10))