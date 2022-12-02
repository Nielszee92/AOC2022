File = open("Day_1_Input.txt", "r")
Lines = File.readlines()

ElfCounter = 1
Calories = []
Dict = {}
TotalCalories = 0
for line in Lines:
    if len(line)==1:
        Dict["Elf_{0}".format(ElfCounter)] = TotalCalories
        ElfCounter += 1
        TotalCalories = 0
    else:
        TotalCalories += float(line.strip())
print(Dict)

Sorted_Elfs = sorted(Dict.values())

print(sum(Sorted_Elfs[-3:]))
