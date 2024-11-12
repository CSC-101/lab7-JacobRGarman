import sys
from convert import str_to_float

def sum_command_line_args(args: list[str]) -> float:
    total = 0.0
    for arg in args:
        converted_value = str_to_float(arg)
        if converted_value is not None:
            total += converted_value
    return total

if __name__ == '__main__':
    args = sys.argv[1:]  # Skip the script name
    total_sum = sum_command_line_args(args)
    print(f"The sum of the command-line arguments is: {total_sum}")

