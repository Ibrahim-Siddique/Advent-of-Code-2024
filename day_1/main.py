def read_input():
    with open("input.txt") as file:
        return file.read().splitlines()


def parse_input(data: list[str]) -> list[list[int], list[int]]:
    left_line = []
    right_line = []

    for line in data:
        left_val, right_val = line.split()

        left_line.append(int(left_val))
        right_line.append(int(right_val))

    return left_line, right_line


def main():
    data = read_input()
    left_line, right_line = parse_input(data)
    left_line_copy = left_line.copy()

    left_line.sort()
    left_line.reverse()

    right_line.sort()
    right_line.reverse()

    total_distance = 0
    similarity_score = 0

    occurence_hashmap = {}

    while left_line != []:
        smallest_left_val = left_line[-1]
        smallest_right_val = right_line[-1]

        distance = abs(smallest_left_val - smallest_right_val)
        total_distance += distance

        occurence_hashmap[smallest_right_val] = occurence_hashmap.get(
            smallest_right_val, 0) + 1

        del left_line[-1]
        del right_line[-1]

    print("Total distance: ", total_distance)

    for number in left_line_copy:
        similarity_score += number * occurence_hashmap.get(number, 0)
    
    print("Similarity score: ", similarity_score)

if __name__ == "__main__":
    main()
