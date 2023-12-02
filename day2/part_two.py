import re
import numpy as np

puzzle_input_path = "day2/puzzle_input.txt"

colors = ["red", "green", "blue"]
fewest_cubes_list = []
sum_of_power = 0

with open(puzzle_input_path, "r") as puzzle_input:
    for line in puzzle_input:
        split_line = re.split(r"[,:;]", line)
        fewest_cubes_list = []
        for color in colors: 
            highest_num = 0
            for set in split_line[1:]:
                set_parts = set.split()
                if color == set_parts[-1]:
                    current_num = int(set_parts[0])
                    if current_num >= highest_num:
                        highest_num = current_num
            fewest_cubes_list.append((highest_num))  
        power_of_set = np.prod(fewest_cubes_list)
        sum_of_power += power_of_set
        print(fewest_cubes_list)
print(sum_of_power)