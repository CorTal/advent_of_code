import os
import re



string_to_number = {
   "one": "1",
   "two": "2",
   "three": "3",
   "four": "4",
   "five": "5",
   "six": "6",
   "seven": "7",
   "eight": "8",
   "nine": "9"
}
# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the file
file_path = os.path.join(dir_path, "input.txt")

with open(file_path, "r") as file:
     sum = 0
     for line in file:
      first_digit = ""
      last_digit = ""
      constructed_line = line

      for char in line:
            if char.isdigit():
               if first_digit == "":
                  first_digit = char
               last_digit = char
            elif constructed_line.startswith(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")):
               three_letters = constructed_line[0:3]
               four_letters = constructed_line[0:4]
               five_letters = constructed_line[0:5]
               letters_digit = None
               if three_letters in string_to_number:
                  letters_digit = string_to_number[three_letters]
               elif four_letters in string_to_number:
                  letters_digit = string_to_number[four_letters]
               elif five_letters in string_to_number:
                  letters_digit = string_to_number[five_letters]
               if first_digit == "":
                  first_digit = letters_digit
               last_digit = letters_digit
            constructed_line = constructed_line[1:]
            
               

      number = int(first_digit + last_digit)
      sum += number
print(sum)
        

