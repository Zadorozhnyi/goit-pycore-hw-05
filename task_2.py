import re
from typing import Callable

# Generator function for identifying real numbers in text
def generator_numbers(text: str):
    # Regular expression to find real numbers separated by spaces
    re_pattern = r'\b\d+\.\d+\b'
    # Iterate through all found numbers and return them
    for match in re.findall(re_pattern, text):
        yield float(match)

# Function to sum numbers found by generator
def sum_profit(text: str, func: Callable):
    # Call generator function and sum up all found numbers
    return sum(func(text))


# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
