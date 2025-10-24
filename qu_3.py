def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

number = 600851475143
print("Largest prime factor:", largest_prime_factor(number))
