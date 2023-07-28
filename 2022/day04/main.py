with open("2022/day04/input.txt", "r",encoding="utf-8") as file:
    content = file.read()

assignment = content.splitlines()
file.close()
    
count_overlaps = 0

for a in assignment:
    elf1, elf2 = a.split(",")
    
    elf1_sec_start, elf1_sec_stop = [int(val) for val in elf1.split("-")]
    elf2_sec_start, elf2_sec_stop = [int(val) for val in elf2.split("-")]

    if (elf1_sec_stop >= elf2_sec_start and
    elf2_sec_stop >= elf1_sec_start):
        count_overlaps += 1

print(f"Total overlaps: {count_overlaps}")

print("Finished")