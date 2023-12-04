"""
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
from pathlib import Path


data = (Path(__file__).parent / "data.txt").read_text()


print("Solution One-lined: ", sum(int(f"{number[0]}{number[-1]}") for number in list(map(lambda line: "".join(char for char in line if char.isdigit()), (l for l in (Path(__file__).parent / "data.txt").read_text().splitlines())))))


total = 0
for line in data.splitlines():
    number = ""
    for char in line:
        if char.isdigit():
            number = f"{number}{char}"

    total += int(f"{number[0]}{number[-1]}")

print("Solution sane: ", total)