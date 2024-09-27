def print_diamond(n):
    # Check if the input is an odd integer
    if n % 2 == 0:
        return "Please provide an odd integer."
    
    # Calculate the midpoint
    mid = n // 2
    
    # Print the upper part of the diamond
    for i in range(mid + 1):
        print(' ' * (mid - i) + '*' * (2 * i + 1))
    
    # Print the lower part of the diamond
    for i in range(mid - 1, -1, -1):
        print(' ' * (mid - i) + '*' * (2 * i + 1))

print_diamond(5)
