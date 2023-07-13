with open("2022/day03/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

rucksacks = content.splitlines()
file.close()

sum_priorities = 0

get_priority = lambda l: ord(l) - 96 if l.islower() else ord(l) - 38

group = []
for s in rucksacks:
    group.append(s)
    if len(group) == 3:
        for c in s:
            if c in group[0] and c in group[1] and c in group[2]:
                sum_priorities += get_priority(c)
                group = []
                break

print(f"Total Priorities: {sum_priorities}")

print("Finished")