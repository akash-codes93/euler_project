from generator import natural_dec


def check_palindrome(n):
    rev_number = 0
    p = n
    while n != 0:
        a = n%10
        rev_number = rev_number*10 + a
        n = int(n/10)
    if rev_number == p:
        return True
    else:
        return False


def euler_4():
    max =0
    for i in natural_dec(999,99,1):
        for j in natural_dec(999, 99, 1):
            if check_palindrome(i*j) and i*j > max:
                max = i*j

    return max

if __name__ == '__main__':
    print(euler_4())