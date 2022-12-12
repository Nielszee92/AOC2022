import pandas as pd
import numpy as np
File = open("Day_10_Input.txt", "r")
Lines = File.readlines()

Cycles = {}
Cycles[0]= 1
X =1
NCycles = 1
Cycles[NCycles] = X
for i in range(0,len(Lines)):
    command = Lines[i].strip().split(" ")[0]
    if command == "addx":
        step = Lines[i].strip().split(" ")[1]
        NCycles += 1
        Cycles[NCycles] = X
        NCycles += 1
        X += int(step)
        Cycles[NCycles] = X
    else:
        NCycles += 1
        Cycles[NCycles] = X
for ele in Cycles:
    print(ele,Cycles[ele])

StartRow = [0,40,80,120,160,200]
EndRow = [39,79,119,159,199,239]
List = []
for i in range(0,len(StartRow)):
    for j in range(StartRow[i],EndRow[i]):
        if abs(Cycles[j]-(j-StartRow[i]-1))<=1:
            # print(j, Cycles[j], (StartRow[i]-1),"#")
            List.append("#")
        else:
            # print(j, Cycles[j], (StartRow[i]-1), ".")
            List.append(".")
    print(List[-39:])
# print(["#"]*39)
# print(List[0:39])
# print(List[40:79])
# print(List[80:119])
# print(List[120:159])
# print(List[160:199])
# print(List[200:239])

