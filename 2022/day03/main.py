with open("2022/day03/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

def split_pockets(rucksack: str) -> str:
    middle_index = len(rucksack) // 2
    return rucksack[:middle_index], rucksack[middle_index:]

def get_item_type(rucksack: str) -> str:

    pocket_1, pocket_2 = split_pockets(rucksack)

    for c in pocket_1:
        if c in pocket_2:
            return c

rucksacks = content.splitlines()
file.close()

sum_priorities = 0

get_priority = lambda l: ord(l) - 96 if l.islower() else ord(l) - 38

for s in rucksacks:
    item = get_item_type(s)
    sum_priorities += get_priority(item)

print(f"Total Priorities: {sum_priorities}")

print("Finished")