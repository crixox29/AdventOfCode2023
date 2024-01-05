import re


# Part 1
# Sum of digits inside a String:
# Example:
# 1abc2       ==>12
# pqr3stu8vwx ==>38
# a1b2c3d4e5f ==>15
# treb7uchet ==> 77 SUM==>142


def find_calibration_value(line):
    digits = re.findall(r'\d', line)
    if digits:
        return int(digits[0] + digits[-1])
    else:
        return 0


def sum_calibration_values(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += find_calibration_value(line.strip())  # strip to skip wrong spaces
    return total


file_path = 'input.txt'

result = sum_calibration_values(file_path)
print("Part 1 result is: ", result)


# Part two
# Some digits are spelled with letters...
def construct_integers():
    sum_of_digits = 0
    with open(file_path, 'r') as file:
        for i in file:
            # split string into list of characters
            chars = list(i)
            # check if a character is a digit
            first_digit = next((x for x in chars if x.isdigit()), None)
            last_digit = next((x for x in chars[::-1] if x.isdigit()), None)

            final_digit = int(first_digit + last_digit)
            sum_of_digits += final_digit

    return sum_of_digits

print(construct_integers())

# define a dictionary with the follwing format: {one: 1, two: 2, ...}
word_to_number = {
    'zero' : 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def replace_number_with_word(string):
    '''Replace all numbers in a string with their corresponding word
    Example: "two1nine" -> "twoonenine" '''
    for word, number in word_to_number.items():
        string = string.replace(str(number), word)
    return string

def find_substrings_with_digits(string):
    ''' Find all substrings in a string that contain digits
    Example: "eightwothree" -> ["eight", "two", "three"]
    The function returns the substrings in the order they appear in the string
    and translates them to their corresponding number'''
    substrings_with_indices = []

    for word in word_to_number.keys():
        index = string.find(word)
        while index != -1:
            substrings_with_indices.append((word, index))
            index = string.find(word, index + 1)

    # sort the substrings based on their indices
    substrings_with_indices.sort(key=lambda x: x[1])

    # extract the translated numbers from the sorted substrings
    substrings_translated = [word_to_number[word] for word, _ in substrings_with_indices]
    return substrings_translated


def construct_integers_from_words():
    second_sum_of_digits = 0
    with open(file_path, 'r') as file:

        for i in file:
            # replace numbers with words
            string = replace_number_with_word(i)
            # find all substrings with digits
            substrings = find_substrings_with_digits(string)

            first_digit = substrings[0]
            last_digit = substrings[-1]
            final_digit = first_digit * 10 + last_digit

            second_sum_of_digits += final_digit

    return second_sum_of_digits


print("Part 2 result is: ", construct_integers_from_words())
