def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial of n is n times factorial of (n-1)
        return n * factorial(n - 1)

# Test the factorial function
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")