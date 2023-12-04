import os
import re
# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the file
file_path = os.path.join(dir_path, "input.txt")

gear_pattern = r"\*"
digit_pattern = r"\d+"

def match_in_substr(substr, line_numbers, start_index):
    digits_matches = re.finditer(digit_pattern, substr)
    next_digits = []
    for d_match in digits_matches:
        match_index = d_match.start() + start_index
        for index, number in line_numbers.items():
            if match_index >= index and match_index <= index + len(number): 
                next_digits.append(number)
    return next_digits

def find_digits_in_line(line):
    matches = re.finditer(digit_pattern, line)
    line_numbers = {}
    for match in matches:
        number = match.group()
        line_numbers[match.start()] = number
    return line_numbers



matrice = []
max_index_of_line = None
with open(file_path, "r") as file:
    sum_of_numbers = 0
    for line in file:
        matrice.append(line)
        if max_index_of_line is None:
            max_index_of_line = len(line) - 1
    max_index = len(matrice) - 1

    for index, line in enumerate(matrice):
        prev_line_numbers = {}
        if index > 0:
            prev_line = matrice[index - 1]
            prev_line_numbers = find_digits_in_line(prev_line)

        next_line_numbers = {}
        if index < max_index:
            next_line = matrice[index + 1]
            next_line_numbers = find_digits_in_line(next_line)

        this_line = matrice[index]
        this_line_numbers = find_digits_in_line(this_line)
        

        matches = re.finditer(gear_pattern, line)
        for match in matches:
            next_digits = []
            start_index = match.start() - 1
            if start_index < 0:
                start_index = 0
            end_index = match.end() + 1
            if end_index > max_index_of_line:
                end_index = max_index_of_line

            prev_line_substr = None
            this_line_substr = matrice[index][start_index:end_index]
            next_line_substr = None
            if index > 0: 
                prev_line_substr = matrice[index - 1][start_index:end_index]
                next_digits += match_in_substr(prev_line_substr, prev_line_numbers, match.start())

            if index < max_index:
                next_line_substr = matrice[index + 1][start_index:end_index]
                next_digits += match_in_substr(next_line_substr, next_line_numbers, match.start())

            next_digits += match_in_substr(this_line_substr, this_line_numbers, match.start())
            if len(next_digits) == 2:
                sum_of_numbers += (int(next_digits[0]) * int(next_digits[1]))

            



print(sum_of_numbers)