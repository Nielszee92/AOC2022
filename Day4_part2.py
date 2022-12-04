File = open("Day_4_Input.txt", "r")
Lines = File.readlines()
Solution = 0
for line in Lines:
    Elf1 = line.strip().split(",")[0]
    StartIdElf1 = int(Elf1.split("-")[0])
    EndIdElf1 = int(Elf1.split("-")[1])

    Elf2 = line.strip().split(",")[1]
    StartIdElf2 = int(Elf2.split("-")[0])
    EndIdElf2 = int(Elf2.split("-")[1])

    Locations1 = ""
    Locations2 = ""
    for i in range(0,100):
        if i < StartIdElf1 or i > EndIdElf1:
            Locations1 += "-"
        else:
            Locations1 += "X"
        if i < StartIdElf2 or i > EndIdElf2:
            Locations2 += "-"
        else:
            Locations2 += "X"

    print(Locations1)
    print(Locations2)
    print("")
    if EndIdElf1 >= StartIdElf2 and EndIdElf1 <= EndIdElf2:
        Solution += 1
        print("+1")
    elif EndIdElf2 >= StartIdElf1 and EndIdElf2 <= EndIdElf1:
        Solution += 1
        print("+1")
print(Solution)