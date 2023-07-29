with open("2022/day05/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

instructions = content.splitlines()
file.close()

message = ""

stacks = []

for i in range(9):
    stack = []

    for line in instructions[:8]:
        if line[4 * i + 1] != ' ':
            stack.append(line[4 * i + 1])
    
    stacks.append(list(reversed(stack)))  

for i, line in enumerate(instructions[10:]):
    quantity = int(line.split(' ')[1])
    from_number = int(line[-6]) - 1
    to_number = int(line[-1]) - 1

    CrateMover_9001 = []
    for move in range(quantity):
        crane_slot = stacks[from_number].pop()
        CrateMover_9001.append(crane_slot)
    
    stacks[to_number] += list(reversed(CrateMover_9001))

for s in stacks:
    message += s.pop()

print(f"Top crates: {message}")

print("Finished")