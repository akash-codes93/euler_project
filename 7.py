def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_at(nth):
    n = 0
    prime_count = 0
    while prime_count < nth:
        if is_prime(n):
            prime_count += 1
        n += 1
    return n - 1

if __name__ == '__main__':
    print(prime_at(10001))
    # result : 104743
