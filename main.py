import logging
from input_handler import get_input
from validator import validate
from core import process
from calculator import add_numbers, multiply_numbers, get_max

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def greeting():
    print("Welcome to the Event Processing System!")
    print("========================================")
    print("Available commands: single, add, multiply, max")
    print("========================================")

def process_command(command):
    if command == "single":
        data = get_input()
        if validate(data):
            result = process(data)
            print(f"Result: {result}")
        else:
            print("Invalid input")
    elif command == "add":
        nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
        result = add_numbers(nums)
        print(f"Sum: {result}")
    elif command == "multiply":
        nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
        result = multiply_numbers(nums)
        print(f"Product: {result}")
    elif command == "max":
        nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
        result = get_max(nums)
        print(f"Maximum: {result}")
    else:
        print("Unknown command")

def main():
    logging.info("Program started")
    greeting()
    command = input("Choose command: ").strip().lower()
    logging.info(f"Command selected: {command}")
    process_command(command)
    logging.info("Program finished")

if __name__ == "__main__":
    main()
