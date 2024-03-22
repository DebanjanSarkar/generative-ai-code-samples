# calculate the 14th Fibonacci number
n = 14

# initialize the first two numbers in the sequence
fibonacci = [0, 1]

# calculate the Fibonacci sequence up to the n-th number
for i in range(2, n+1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# get the 14th Fibonacci number
fibonacci_14th = fibonacci[n]

print(f"The 14th Fibonacci number is: {fibonacci_14th}")