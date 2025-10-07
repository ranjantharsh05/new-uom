def special_pythagorean_triplet():
    """
    Finds the unique Pythagorean triplet (a, b, c) such that a + b + c = 1000, 
    and returns the product a * b * c.
    """
    TARGET_SUM = 1000
    
    # a must be less than TARGET_SUM / 3 (~333) because a < b < c
    for a in range(1, TARGET_SUM // 3):
        
        # b must be less than c, and a + b < 1000. Start b from a + 1.
        for b in range(a + 1, TARGET_SUM // 2): 
            
            # Calculate c using the sum condition
            c = TARGET_SUM - a - b
            
            # Since a < b, we only need to check if b < c, 
            # but b < c is guaranteed if a and b are small enough.
            # We must check the Pythagorean condition: a^2 + b^2 == c^2
            
            # Check if it's a Pythagorean triplet
            if a*a + b*b == c*c:
                # Triplet found! Return the product a * b * c
                return a * b * c
                
    # If no triplet is found (shouldn't happen for this problem)
    return None

# Execute the function and print the result
result = special_pythagorean_triplet()
print(f"The product abc is: {result}")