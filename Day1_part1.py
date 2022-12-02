File = open("Day_1_Input.txt", "r")
Lines = File.readlines()

ElfCounter = 1
Calories = []
Dict = {}
TotalCalories = 0
for line in Lines:
    if len(line)==1:
        Dict["Elf_{0}".format(ElfCounter)] = {}
        Dict["Elf_{0}".format(ElfCounter)]["Snacks"] = Calories
        Dict["Elf_{0}".format(ElfCounter)]["Total"] = TotalCalories
        ElfCounter += 1
        TotalCalories = 0
        Calories = []
    else:
        Calories.append(float(line.strip()))
        TotalCalories += float(line.strip())
print(Dict)
MaxCalories = 0
for elf in Dict:
    MaxCalories = max(MaxCalories,Dict[elf]["Total"])
print(MaxCalories)
