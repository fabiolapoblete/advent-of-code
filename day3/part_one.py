import re

engine_schematic_path = "day3/example.txt"
valid_symbols =re.compile(r'[^0-9.]')
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def is_valid_part_number(matrix, row, col):
    if not matrix[i][j].isdigit():
        return False
    for dr, dc in directions:
        #Check adjacent positions
        new_row, new_col = row + dr, col + dc
        #Check so that the adjacent position is within the matrix
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            if matrix[new_row][new_col] in valid_symbols:
                return True
    return False

with open(engine_schematic_path, "r") as engine_schematic:
    for line in engine_schematic:
        matrix = [list(line.strip())]
        print(matrix)
    for i in range(len(matrix)): #Iterates over the rows of the matrix
        for j in range(len(matrix[0])): #Iterates over the columns of each row
            if is_valid_part_number:
                print(f"Valid number at position ({i+1}, {j+1}): {matrix[i][j]}")







# import numpy as np
# import re

# engine_schematic_path = "day3/example.txt"

# # with open(engine_schematic_path, "r") as engine_shematic:
# #     matrix = []
# #     for line in engine_shematic:
# #         formatted_line = line.replace(".", "A")
# #         line_list = list(formatted_line)
# #         matrix.append(line_list)
# #     print(matrix)

# #     for i, row in enumerate(matrix):
        
# with open(engine_schematic_path, "r") as engine_shematic:
#     matrix = []
#     found_digit = False
#     digits = []
#     for line in engine_shematic:
#         row = re.findall(r'\d|\D|\.', line)
#         matrix.append(row)
#     # print(matrix)
#         for i, row in enumerate(matrix):
#             for j, char in enumerate(row):
#                 if char.isdigit():
#                     found_digit = True
#                     digits.append((i,j))
#                 elif found_digit:
#                     break
#             print(digits)




#                     # pos_i = i
#                     # pos_j = j
#                     # #check if symbol at position (i, j-1)
#                     # print(char, (i,(j+1)))
                        
#                     # position = (i,j)

#                     # print(position)
#                     # print(f"Digit {char} at position ({i}, {j})")


#         #     for i, row in enumerate(matrix):
#         #         print(i, row)
#     #Varje rad är 10 lång
#     #Hitta en siffra. Kolla hur lång den är
#     #Find a digit
#     #Find index of that digit
#     #Check if symbol before or after digit
#     #Check if symbol on same index on row before and after (index +1 och index -1)