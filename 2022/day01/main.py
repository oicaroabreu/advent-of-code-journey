with open("2022/day01/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

meals = content.splitlines()
file.close()

elfs = []

calories = 0
for food in meals:
    if food:
        calories += int(food)
    else:
        elfs.append(calories)
        calories = 0

max_calories = max(elfs)

print("Part One")
print(f"The elf with the most calories is elf #{(elfs.index(max_calories) + 1)} carrying {max_calories} calories")

#Part Two - top three Elves
elfs_sorted = sorted(elfs, reverse=True)
max_calories_three_elves = sum(elfs_sorted[:3])
print("\nPart Two")
print(f"The first elf with the most calories is elf #{(elfs.index(elfs_sorted[0]) + 1)} carrying {elfs[elfs.index(elfs_sorted[0])]} calories")
print(f"The second elf with the most calories is elf #{(elfs.index(elfs_sorted[1]) + 1)} carrying {elfs[elfs.index(elfs_sorted[1])]} calories")
print(f"The third elf with the most calories is elf #{(elfs.index(elfs_sorted[2]) + 1)} carrying {elfs[elfs.index(elfs_sorted[2])]} calories")

print(f"The total calories carried by these three elves is {max_calories_three_elves}")

print("Finished")
