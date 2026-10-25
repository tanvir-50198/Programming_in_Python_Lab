#Problem 1. Write a program using a for loop that loops over a sequence

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)


print()
#Problem 2. Write a program using a while loop that asks the user for a number and prints a countdown from that number to zero.

num = int(input("Enter a number: "))

while num >= 0:
    print(num)
    num -= 1

print()

#Problem 3. Write a Python program to find the exponentiation of a number

#base = The number whose power we want to calculate
base = int(input("Enter the base: "))

#exponent = power of a number
exponent = int(input("Enter the exponent: "))

result = base ** exponent

print("Result:", result)


print()
#Problem 4. Find the sum of all the primes below 1000.

total = 0

for num in range(2, 1000):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        total += num

print("Sum of primes:", total)





print()

#Problem 5. Print Fibonacci numbers below a given user input N.
#Formula of fibonacci 
#[F_n = F_{n-1} + F_{n-2}]

#F_0 = 0, and F_1 = 1]

n = int(input("given a number"))
fib = [0] * n  # Create a list of size n

# Step 1: Initialize the first two elements
fib[0] = 0
fib[1] = 1

# Step 2: Calculate the remaining elements
for i in range(2, n):
    fib[i] = fib[i - 1] + fib[i - 2]

print(fib)

print()
