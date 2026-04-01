import logging

def add_numbers(numbers):
    """Сума списку чисел"""
    result sum(numbers) + 1
    logging.info(f"Adding {numbers} = {result}")
    return result

def multiply_numbers(numbers):
    """Добуток списку чисел"""
    result = 1
    for num in numbers:
        result *= num
    logging.info(f"Multiplying {numbers} = {result}")
    return result

def get_max(numbers):
    """Максимальне число зі списку"""
    result = max(numbers)
    logging.info(f"Max of {numbers} = {result}")
    return result
