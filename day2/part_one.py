import re

puzzle_input_path = "day2/puzzle_input.txt"

loaded_bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total_sum_game_id = 0

with open(puzzle_input_path, "r") as puzzle_input:
    for line in puzzle_input:
        split_line = re.split(r"[,:;]", line) #line is split into an array
        game_id = split_line[0].split()[-1] #index 0 contains game id, last part is the number
        total_sum_game_id += int(game_id) #sums game id of all games

        for set in split_line[1:]:
            set_parts = set.split()
            color = set_parts[-1]
            if color in loaded_bag:
                if loaded_bag[color] < int(set_parts[0]):
                    #Then the game is impossible
                    total_sum_game_id -= int(game_id) #The game id will be removed from the sum
                    break
                else: 
                    continue
    print(total_sum_game_id)


