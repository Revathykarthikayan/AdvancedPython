# Initializing the Fibonacci sequence with the first two numbers
fibonacci = [1, 1]

# Using  lambda function within a loop to generate the Fibonacci sequence up to 50
next_fibnumber = lambda x, y: x + y

while True:
    next_element= next_fibnumber(fibonacci[-1], fibonacci[-2])
    if next_element > 50:
        break
    fibonacci.append(next_element)

print(fibonacci)



