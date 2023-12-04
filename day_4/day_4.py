import os
import re
# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the file
file_path = os.path.join(dir_path, "input.txt")

scratchcards = {}
number_of_scratchcards = 0
with open(file_path, "r") as file:
    total_score = 0
    for line in file:
        game_number = int(re.search(r"\d+", line).group())
        scratchcards.setdefault(game_number, 0)

        scratchcards[game_number] += 1

        match = re.search(r":", line)
        line = line[match.end():]

        cards = line.split("|")
        
        winning_cards = cards[0]
        my_cards = cards[1]
        
        winning_numbers = re.findall(r"\d+", winning_cards)
        my_numbers = re.findall(r"\d+", my_cards)
        game_number_scratchards = scratchcards[game_number]
        common_numbers_cnt = 0
        for number in my_numbers:
            if number in winning_numbers:
                common_numbers_cnt += 1
        
        for i in range(game_number+1, game_number+common_numbers_cnt+1):
            scratchcards.setdefault(i, 0)
            scratchcards[i] += 1*game_number_scratchards
        number_of_scratchcards += scratchcards[game_number]
    print(number_of_scratchcards)
