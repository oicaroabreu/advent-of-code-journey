with open("2022/day02/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

def rps_result(p1: str, p2: str) -> int:
    if (p1 == 'A' and p2 == 'Z') or \
    (p1 == 'B' and p2 == 'X') or\
    (p1 == 'C' and p2 == 'Y'):
        return 0 #lost
    
    if (p1 == 'A' and p2 == 'Y') or \
    (p1 == 'B' and p2 == 'Z') or\
    (p1 == 'C' and p2 == 'X'):
        return 6 #win
    
    if (p1 == 'A' and p2 == 'X') or \
    (p1 == 'B' and p2 == 'Y') or\
    (p1 == 'C' and p2 == 'Z'):
        return 3 #draw


rounds = content.splitlines()
file.close()

total_score = 0
scorring = {"X":1,"Y":2,"Z":3}

for play in rounds:
    elf, me = play.split()

    total_score += scorring[me]
    total_score += rps_result(elf, me)
    
print(f"Total Score: {total_score}")

print("Finished")