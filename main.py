from input_handler import get_input
from validator import validate
from core import process

def main():
	data = get_input()
	if validate(data):
		result = process(data)
		print(f"Result: {result}")
	else:
		print("Invalid input")

if __name__ == "__name__":
main()
