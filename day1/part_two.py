calibration_document_path = "day1/calibration_doc.txt"

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

sum_of_calibration_values = 0

with open(calibration_document_path, "r") as calibration_document:
    for text_line in calibration_document:
        digit_list = []
        while len(text_line) > 0:

            if text_line[0].isdigit():
                digit_list.append(text_line[0]) 
            else:
                for word in number_dict:
                    if text_line.startswith(word):
                        # text_line = text_line.replace(word, "", 1)
                        digit_list.append(number_dict[word]) 
            text_line = text_line[1:]
        first_digit = digit_list[0]
        second_digit = digit_list[-1]

        calibration_value = str(first_digit) + str(second_digit)
        sum_of_calibration_values += int(calibration_value)
print (sum_of_calibration_values)