# calibration_document_path = "calibration_doc.txt"

# sum_of_calibration_values = 0

# number_dict = {
#     "one": "1",
#     "two": "2",
#     "three": "3",
#     "four": "4",
#     "five": "5",
#     "six": "6",
#     "seven": "7",
#     "eight": "8",
#     "nine": "9",
# }

# with open(calibration_document_path, "r") as calibration_document:
#     for text_line in calibration_document:
#         print(text_line)
#         num_list = []
#         words = text_line.split()
#         print(words)
#         for word in words:
#             print(word)
#             alpha_number = ""
#             numeric_number = ""
#             for char in word:
#                 if char.isalpha():
#                     alpha_number += char
#                     if alpha_number in number_dict:
#                         alpha_number = number_dict[alpha_number]
#                         num_list.append(alpha_number)
#                         alpha_number = ""

#                 elif char.isdigit():
#                     numeric_number = char
#                     num_list.append(numeric_number)
#             new_text_line = "".join(num_list)
#             print(new_text_line)

number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

input_string = "sevengjfdseven8nine"

# Kolla om strängen börjar med word om ej ta bort första bokstaven
print(len(input_string))
while len(input_string) > 1:
    for word in number_dict:
        print(word)
        if input_string.startswith(word):
            input_string = input_string.replace(word, "", 1)
            print(input_string)
            print(len(input_string))
    break

# elif word not in input_string:
#     input_string = input_string[1:]
#     print(input_string)
#     break

# else:
#     input_string = input_string[1:]
#     print(input_string)

# for word in number_dict:
#     if input_string.startswith(word):
#         print(word)
#         input_string = input_string.replace(word, "", 1)
#     else:
#         input_string.replace

# for word in number_dict:
#     index = 0
#     while input_string.startswith(word, index):
#         print("word", word)
#         index += len(word)
#     input_string = input_string[index:]
#     print("input", input_string)


# for value in number_dict:
#     for char in input_string:
#         if char.isalpha():
#             current_alpha += char
#             if value.startswith(char):
#                 result_numbers.append(number_dict[current_alpha])
#                 current_alpha = ""
#                 print(result_numbers)
#             elif char.isdigit():
#                 result_numbers.append(char)
#                 current_alpha = ""


# for char in input_string:
#     if char.isalpha():
#         current_alpha += char
#         print(current_alpha)
#         if current_alpha in number_dict:
#             result_numbers.append(number_dict[current_alpha])
#             current_alpha = ""
#             print(result_numbers)
#     elif char.isdigit():
#         result_numbers.append(char)
#         current_alpha = ""

# print(result_numbers)
