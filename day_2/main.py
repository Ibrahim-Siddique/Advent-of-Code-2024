def read_input(file_path: str) -> list[str]:
    """Reads the input data from a file."""
    with open(file_path, "r") as file:
        return file.read().splitlines()

def parse_input(data: list[str]) -> list[list[int]]:
    """
    Parses the input data into a list of lists of integers.
    :param data: List of input strings
    :return: List of lists of integers
    """
    return [[int(column) for column in row.split()] for row in data]

def check_row(row: list[int], increasing: bool) -> bool:
    """
    Checks if a row is safe based on level differences.
    :param row: List of integers
    :param increasing: True if the row is expected to be increasing, otherwise False
    :return: True if the row is safe, False otherwise
    """
    for i in range(1, len(row)):
        diff = row[i] - row[i - 1]
        if increasing:
            if not (1 <= diff <= 3):
                return False
        else:
            if not (1 <= -diff <= 3):
                return False
    return True

def is_safe_with_dampener(row: list[int]) -> bool:
    """
    Determines if a row can be made safe by removing one level.
    :param row: List of integers
    :return: True if the row can be made safe, False otherwise
    """
    for i in range(len(row)):
        modified_row = row[:i] + row[i+1:]
        increasing = modified_row[1] > modified_row[0] if len(modified_row) > 1 else True
        if check_row(modified_row, increasing):
            return True
    return False

def validate_rows_with_dampener(parsed_input: list[list[int]]) -> int:
    """
    Validates rows and counts safe rows, considering the Problem Dampener.
    :param parsed_input: Parsed input data as a list of lists of integers
    :return: Count of total safe rows
    """
    safe_count = 0
    for row in parsed_input:
        increasing = row[1] > row[0] if len(row) > 1 else True
        if check_row(row, increasing) or is_safe_with_dampener(row):
            safe_count += 1
    return safe_count

def main():
    """
    Main function to handle input reading, processing, and output.
    """
    file_path = "input.txt"
    data = read_input(file_path)
    parsed_input = parse_input(data)
    total_safe_rows = validate_rows_with_dampener(parsed_input)
    print(f"Total safe rows with Problem Dampener: {total_safe_rows}")

if __name__ == "__main__":
    main()
