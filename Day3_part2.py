File = open("Day_3_Input.txt", "r")
Lines = File.readlines()
Solution = 0
from collections import Counter
Group1 = []
Group2 = []
# Group3 = []
Solution = 0
def get_unique_letter(Lines):
    Unique_letter = []
    for ele in Lines[0].strip():
        if ele in Lines[1].strip() and ele in Lines[2].strip():
            if ele not in Unique_letter:
                Unique_letter.append(ele)
    return Unique_letter
for i in range(0,int(len(Lines)/3)):
    Unique_letter = get_unique_letter(Lines[i*3:i*3+3])[0]
    print(Unique_letter)

    if int(ord(Unique_letter)) > 96:
        print(ord(Unique_letter)-96)
        Solution += ord(Unique_letter)-96
    else:
        print(ord(Unique_letter)-65+27)
        Solution += ord(Unique_letter)-65+27

print(Solution)