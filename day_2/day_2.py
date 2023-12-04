
import os
import re
# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the file
file_path = os.path.join(dir_path, "input.txt")




with open(file_path, "r") as file:
    sum_of_powers = 0

    for line in file:
        game = line.split(':')[0]
        game_id = int(re.search(r'\d+', game).group())
        constructed_line = line[7:]
        sets = constructed_line.split(";")
        sets_bag = {"green": 0, "red": 0, "blue": 0}

        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                number_of_cubes = re.search(r'\d+', cube).group()
                color_of_cubes = re.search(r'[a-z]+', cube).group()
                if color_of_cubes in sets_bag:
                    if int(number_of_cubes) > sets_bag[color_of_cubes]:
                        sets_bag[color_of_cubes] = int(number_of_cubes)
        set_power_value = None
        for color, value in sets_bag.items():
            if set_power_value is None:
                set_power_value = value
            else:
                set_power_value *= value
        sum_of_powers += set_power_value




print(sum_of_powers)