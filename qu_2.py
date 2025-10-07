# Problem: Find the sum of even Fibonacci numbers not exceeding 4 million

limit = 4000000
a, b = 1, 2
even_sum = 0

while b <= limit:
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b

print("Sum of even Fibonacci numbers up to 4 million:", even_sum)
