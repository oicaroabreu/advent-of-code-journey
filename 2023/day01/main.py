with open("2023/day01/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()
file.close()

sum_calibration = 0
for line in lines:
    calibration = list(filter(lambda c : c.isdigit(), line))
    sum_calibration += int(calibration[0] + calibration[-1])

print(f"The sum of all of the calibration values: {sum_calibration}")

print("Finished")