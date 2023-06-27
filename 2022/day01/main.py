with open("2022/day01/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

meals = content.splitlines()
elfs = []

calories = 0
for food in meals:
    if food:
        calories += int(food)
    else:
        elfs.append(calories)
        calories = 0

max_calories = max(elfs)
print(f"The elf with the most calories is elf #{(elfs.index(max_calories) + 1)} caarrying {max_calories} caalories")

file.close()
print("Finished")
