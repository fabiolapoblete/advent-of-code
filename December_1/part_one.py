calibration_document_path = "calibration_doc.txt"

sum_of_calibration_values = 0

with open(calibration_document_path, "r") as calibration_document:
    for text_line in calibration_document:
        num_list = [int(char) for char in text_line if char.isdigit()]

        first_num = num_list[0]
        second_num = num_list[-1]

        calibration_value = str(first_num) + str(second_num)

        sum_of_calibration_values += int(calibration_value)

print(sum_of_calibration_values)
