def caching_fibonacci():
    # Initialize empty dictionary for caching results
    cache = {}

    # Internal function to calculate the Fibonacci number
    def fibonacci(n):
        # If n <= 0, return 0
        if n <= 0:
            return 0
        # If n == 1, return 1
        elif n == 1:
            return 1
        # If the value is already in cache, just return it
        if n in cache:
            return cache[n]
        # Calculate the value and store it in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # Return the calculated value
        return cache[n]

    # Return the internal function
    return fibonacci


# Приклад використання

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
