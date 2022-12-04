File = open("Day_3_Input.txt", "r")
Lines = File.readlines()
Solution = 0
from collections import Counter
for line in Lines:
    Compartiment_1 = Counter(line.strip()[:int(len(line)/2)])
    Compartiment_2 = Counter(line.strip()[int(len(line) / 2):])
    for ele in Compartiment_1:
        if ele in Compartiment_2.keys():
            Common_Snack = ele
            break
        else:
            pass
    print(ele)
    if int(ord(ele)) > 96:
        print(ord(ele)-96)
        Solution += ord(ele)-96
    else:
        print(ord(ele)-65+27)
        Solution += ord(ele)-65+27
print(Solution)