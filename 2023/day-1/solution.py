"""
--- Day 1: Trebuchet?! ---
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
input_type='prod'

def get_input(input_type):
    if input_type == 'test':
        file_name = '2023/day-1/sample_input.txt'
    elif input_type == 'prod':
        file_name = '2023/day-1/input.txt'
    else:
        raise Exception("Invalid input type. only test and prod is allowed.")

    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line[0] != '#']

    return lines


def solution_part1(lines):
    calibration_value = 0
    for line in lines:
        s = ''
        for i in range(0, len(line)):
            ch = line[i]
            if ch.isdigit():
                s += ch
                break
        for i in range(-1, -len(line)-1, -1):
            ch = line[i]
            if ch.isdigit():
                s += ch
                break
        calibration_value += int(s)
    return calibration_value


numbers = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

def replace_number(line):
    if len(line) < 3:
        return line
    
    new_line = ''
    windows = [3, 4, 5]
    for window in windows:
        cache = ''
        left, right = 0, window
        while right <= len(line)+1:
            # print(line[left:right])
            sub_str = line[left:right]
            if sub_str in numbers:
                new_line += str(numbers[sub_str])
                right += window
                left += window
            else:
                new_line += line[left]
                right += 1
                left += 1
        while left < len(line):
            new_line += line[left]
            left += 1
        line = new_line
        new_line = ''
    return line


def solution_part2_helper(line):
    s = ''
    for i in range(len(line)):
        if line[i].isdigit():
            s += line[i]
            break
        found = False
        for window_size in [3,4,5]:
            sub_str = line[i:i+window_size]
            if sub_str in numbers:
                s += str(numbers[sub_str])
                found = True
                break
        if found:
            break
    
    for i in range(-1, -len(line)-1, -1):
        if line[i].isdigit():
            s += line[i]
            break
        found = False
        for window_size in [3,4,5]:
            sub_str = line[len(line)+i-window_size+1:len(line)+i+1]
            # sub_str = sub_str[::-1]
            if sub_str in numbers:
                s += str(numbers[sub_str])
                found = True
                break
        if found:
            break
    
    return int(s)

    

def solution_part2(lines):
    calibration_value = 0
    for line in lines:
        calibration_value += solution_part2_helper(line)
    return calibration_value



lines = get_input(input_type)
# print(solution_part1(lines))
print(solution_part2(lines))
# print(replace_number('hrmbslbdgnine8nineeightseven8one3'))
# print(replace_number('eightseven8one3'))