import pandas as pd
import numpy as np
File = open("Day_9_Input.txt", "r")
Lines = File.readlines()

#Define size of the grid:
# Dict = {}
# Dict["U"] = []
# Dict["D"] = []
# Dict["R"] = []
# Dict["L"] = []

Steps = []
Directions = []
for line in Lines:
    # Dict[line.strip().split(" ")[0]].append(int(line.strip().split(" ")[1]))
    Directions.append(line.strip().split(" ")[0])
    Steps.append(int(line.strip().split(" ")[1]))

def follow_motion(row_head,col_head,row_tail,col_tail):
    print(row_head,col_head,row_tail,col_tail)
    if abs(row_head-row_tail) > 1 and abs(col_head-col_tail)> 0:
        "move diagonal"
        move_x = (col_head-col_tail)/abs(col_head-col_tail)
        move_y = (row_head-row_tail) / abs(row_head-row_tail)
    elif abs(row_head-row_tail) > 0 and abs(col_head-col_tail)> 1:
        "move diagonal"
        move_x = (col_head-col_tail)/abs(col_head-col_tail)
        move_y = (row_head-row_tail) / abs(row_head-row_tail)
    elif abs(row_head-row_tail) > 1:
        move_x = 0
        move_y = (row_head-row_tail) / abs(row_head-row_tail)
        "move row"
    elif abs(col_head-col_tail) >1:
        move_x = (col_head-col_tail) / abs(col_head-col_tail)
        move_y = 0
        "move col"
    else:
        "dont move"
        move_x = 0
        move_y = 0
    return move_x, move_y
Dict = {}
N = 10
for n in range(0,N):
    Dict["Knots {0}".format(n)] = {}
    Dict["Knots {0}".format(n)]["Step {0}".format(1)] = {}
    Dict["Knots {0}".format(n)]["Step {0}".format(1)]["X"] = 0
    Dict["Knots {0}".format(n)]["Step {0}".format(1)]["Y"] = 0
MaxX = 0
MaxY = 0
MinX = 0
MinY = 0
Total_Steps = 1
for i in range(0,len(Lines)):
    for j in range(0,Steps[i]):
        # print(Dict)
        # print("Current step: ",Total_Steps)
        ActiveKnots = min(Total_Steps,N-1)
        # print("Active Knots: ",ActiveKnots)
        # print("Total steps: ", Total_Steps)
        Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)] = {}
        #The first knot always moves, the others follow through the function
        if Directions[i] == "U":
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["X"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["X"]
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["Y"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["Y"] + 1
            MaxY = max(MaxY,Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["Y"] + 1)
        if Directions[i] == "D":
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["X"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["X"]
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["Y"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["Y"] - 1
            MinY = min(MinY,Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["Y"] - 1)
        if Directions[i] == "L":
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["X"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["X"] - 1
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["Y"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["Y"]
            MinX = min(MinX, Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["X"] - 1)
        if Directions[i] == "R":
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["X"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["X"] + 1
            Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps + 1)]["Y"] = Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["Y"]
            MaxX = max(MaxX, Dict["Knots {0}".format(0)]["Step {0}".format(Total_Steps)]["X"] + 1)

        #The following knots are calculated using the function
        #In case not all the available knots are active, it means that only part of the knots will move
        # if ActiveKnots < N:
        #     for n in range(ActiveKnots,N):
        #         print("if N=",n)
        #         print(Dict)
        #         if "Step {0}".format(Total_Steps+1) not in list(Dict["Knots {0}".format(n)].keys()):
        #             Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps+1)] = {}
        #             Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps+1)]["X"] = \
        #                 Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps)]["X"]
        #             Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps+1)]["Y"] = \
        #                 Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps)]["Y"]
        #         print(Dict)
        # # print(Dict)
        for n in range(1,N):
            # print("N=", n)
            #Get all knots on the same steps:
            Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps+1)] = {}
            #Follows the previous knot
            row_head = Dict["Knots {0}".format(n-1)]["Step {0}".format(Total_Steps+1)]["Y"]
            col_head = Dict["Knots {0}".format(n-1)]["Step {0}".format(Total_Steps+1)]["X"]
            # print(row_head,col_head)
            row_tail = Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps)]["Y"]
            col_tail = Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps)]["X"]
            # print(row_tail, col_tail)
            move_x, move_y = follow_motion(row_head, col_head, row_tail, col_tail)
            # print(move_x,move_y)
            # print("Knots {0}".format(n))
            # print("Step {0}".format(Total_Steps + 1))
            Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps+1)]["X"] = col_tail + move_x
            Dict["Knots {0}".format(n)]["Step {0}".format(Total_Steps+1)]["Y"] = row_tail + move_y
            # print(Dict)
        Total_Steps += 1
# print(Dict)


# for step in Dict["Knots 0"]:
#     DF = pd.DataFrame(np.zeros((MaxY - MinY + 1,MaxX - MinX + 1)))
#     DF = DF.replace(0, ".")
#     for knot in Dict:
#         X = int(Dict[knot][step]["X"] - MinX)
#         Y = int(Dict[knot][step]["Y"] - MinY)
#         DF.iloc[Y,X] = str(knot).split(" ")[1]
#     # print(DF)

# DF = pd.DataFrame(np.zeros((MaxY - MinY + 1,MaxX - MinX + 1)))
# DF = DF.replace(0, ".")
List = []
for step in Dict["Knots 0"]:
    X = int(Dict["Knots 9"][step]["X"] - MinX)
    Y = int(Dict["Knots 9"][step]["Y"] - MinY)
    if str(X)+"_"+str(Y) not in List:
        List.append(str(X)+"_"+str(Y))
print(len(List))
    # DF.iloc[Y,X] = str(knot).split(" ")[1]
# print(DF)
#
# tail_visited = 0
# # print(DF_New.columns)
# # print(DF_New.columns.tolist())
# for col in DF.columns.tolist():
#     # print(DF_New[col])
#     tail_visited+=DF[col].tolist().count("9")
# print(tail_visited)