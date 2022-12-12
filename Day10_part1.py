import pandas as pd
import numpy as np
File = open("Day_10_Input.txt", "r")
Lines = File.readlines()

Cycles = {}
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
#20th, 60th, 100th, 140th, 180th,
Times = [20,60,100,140,180,220]
Ans = 0

for time in Times:
    print(Cycles[time],time)
    Ans += Cycles[time]*time
print(Ans)