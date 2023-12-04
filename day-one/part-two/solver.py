"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""
from pathlib import Path


data = (Path(__file__).parent / "data.txt").read_text().splitlines()
NUMBERS_IN_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def get_number_from_string(string_):
    return NUMBERS_IN_WORDS.get(string_)

numbers_per_line = []
for line in data:
    idx_per_number = {}
    
    for idx, char in enumerate(line):
        if char.isdigit():
            idx_per_number[idx] = int(char)
            continue
        
        for i in range(len(line) - idx):
            chars = line[idx:idx+i+1]
            if (nmbr := get_number_from_string(chars)) is not None:
                idx_per_number[idx] = int(nmbr)
    numbers_per_line.append(idx_per_number)

sum = 0
for coll in numbers_per_line:
    vals = list(coll.values())
    sum += int(f"{vals[0]}{vals[-1]}")
print(numbers_per_line)
print(sum)
        
    
