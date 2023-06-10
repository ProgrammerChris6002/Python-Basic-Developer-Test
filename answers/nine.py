def fibonacci_sum(n):
    fibonacci_sequence = [0, 1] # First two numbers of the fibonacci sequence
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return sum(fibonacci_sequence)

n = 50
fibonacci_sum_to_50 = fibonacci_sum(n)
print(fibonacci_sum_to_50)