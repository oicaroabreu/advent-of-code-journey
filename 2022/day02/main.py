with open("2022/day02/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

def rps_result(p1: str, p2: str) -> int:
    if (p1 == 'A' and p2 == 'C') or \
    (p1 == 'B' and p2 == 'A') or\
    (p1 == 'C' and p2 == 'B'):
        return 0 #lost
    
    if (p1 == 'A' and p2 == 'B') or \
    (p1 == 'B' and p2 == 'C') or\
    (p1 == 'C' and p2 == 'A'):
        return 6 #win
    
    if (p1 == 'A' and p2 == 'A') or \
    (p1 == 'B' and p2 == 'B') or\
    (p1 == 'C' and p2 == 'C'):
        return 3 #draw

#Part Two
def hand(elf: str, outcome: str) -> str:

    if outcome == 'Y':
        return elf

    if outcome == 'Z':
        if elf == 'A':
            return 'B' 
        elif elf == 'B':
            return 'C'
        elif elf == 'C':   
            return 'A'
    
    if outcome == 'X':
        if elf == 'A':
            return 'C'
        elif elf == 'B':
            return 'A'
        elif elf == 'C':
            return 'B'

rounds = content.splitlines()
file.close()

total_score = 0
scorring = {"A":1,"B":2,"C":3}

for play in rounds:
    elf, out = play.split()

    #Part Two
    me = hand(elf, out)

    total_score += scorring[me]
    total_score += rps_result(elf, me)
    
print(f"Total Score: {total_score}")

print("Finished")