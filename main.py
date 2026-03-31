from input_handler import get_input
from validator import validate
from core import process

def greeting():
    print("Welcome to the Event Processing System!")
    print("========================================")

def main():
    greeting()
    data = get_input()
    if validate(data):
        result = process(data)
        print(f"Result: {result}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
