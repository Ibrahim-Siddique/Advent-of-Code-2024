import re

def read_input_file(file_path):
    """Reads the content of the input file."""
    with open(file_path, "r") as file:
        return file.read()

def calculate_simple_sum(input_data, pattern):
    """Calculates the sum of products for matches of the given pattern."""
    matches = re.findall(pattern, input_data)
    return sum(int(x) * int(y) for x, y in matches)

def calculate_conditional_sum(input_data, mul_pattern, control_pattern):
    """
    Calculates the sum of products for matches of the given multiplication pattern,
    respecting the control commands (`do()` and `don't()`).
    """
    enabled = True
    results = []
    for token in re.finditer(f"{mul_pattern}|{control_pattern}", input_data):
        match = token.group()
        if "do()" in match:
            enabled = True
        elif "don't()" in match:
            enabled = False
        elif enabled:
            x, y = map(int, re.findall(r"\d+", match))
            results.append(x * y)
    return sum(results)

def main():
    """Main function to process input and calculate results."""
    file_path = "input.txt"
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"do\(\)|don't\(\)"
    
    input_data = read_input_file(file_path)
    
    # Part one
    total_sum = calculate_simple_sum(input_data, mul_pattern)
    print(total_sum)
    
    # Part two
    total_sum_part_two = calculate_conditional_sum(input_data, mul_pattern, control_pattern)
    print(total_sum_part_two)

if __name__ == "__main__":
    main()
