def sum_primes(limit):
    # Sieve array: True means potentially prime
    is_prime = [True] * limit 
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p < limit:
        if is_prime[p]:
            # Mark multiples of p as not prime
            for i in range(p * p, limit, p):
                is_prime[i] = False
        p += 1
        
    # Sum all primes
    total_sum = 0
    for p in range(2, limit):
        if is_prime[p]:
            total_sum += p
            
    return total_sum

LIMIT = 2000000
result = sum_primes(LIMIT)
print(f"Sum: {result}")