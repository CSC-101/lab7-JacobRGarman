from convert import str_to_float

def gather_numbers() -> list[float]:
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        converted_value = str_to_float(user_input)
        if converted_value is not None:
            numbers.append(converted_value)
        else:
            print("Invalid input, skipping.")
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print(f"The sum of the numbers is: {sum(numbers)}")

