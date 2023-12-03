with open("2023/day01/input.txt", "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()
file.close()

digits = {
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

sum_calibration = 0
for line in lines:
    numbers = []
    for i, c in enumerate(line):
        if c.isdigit():
            numbers.append(int(c))
        for j in range(i + 1, len(line) + 1):
            substring = line[i:j]
            if substring in digits:
                first = digits.get(substring)
                numbers.append(first)
    number = str(numbers[0]) + str(numbers[-1])
    sum_calibration += int(number)

print(f"The sum of all of the calibration values: {sum_calibration}")

print("Finished")
