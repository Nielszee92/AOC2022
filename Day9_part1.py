import pandas as pd
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
# print(sum(Dict["U"]))
# print(sum(Dict["D"]))
# print(sum(Dict["L"]))
# print(sum(Dict["R"]))
print(Steps)
print(Directions)
MaxColumns = 0
MinColumns = 0
MaxRows = 0
MinRows = 0
CurrentCol = 0
CurrentRow = 0

for i in range(0,len(Lines)):
    if Directions[i] == "R":
        CurrentCol += Steps[i]
        MaxColumns = max(MaxColumns,CurrentCol)
        MinColumns = min(MinColumns, CurrentCol)
    if Directions[i] == "L":
        CurrentCol -= Steps[i]
        MinColumns = min(MinColumns, CurrentCol)
        MaxColumns = max(MaxColumns,CurrentCol)
    if Directions[i] == "U":
        CurrentRow += Steps[i]
        MinRows = min(MinRows, CurrentRow)
        MaxRows = max(MaxRows,CurrentRow)
    if Directions[i] == "D":
        CurrentRow -= Steps[i]
        MinRows = min(MinRows, CurrentRow)
        MaxRows = max(MaxRows,CurrentRow)
    # print(CurrentRow, CurrentCol)
print(MaxColumns,MaxRows)
print(MinColumns,MinRows)

#Create Grid:
DF = pd.DataFrame()
for i in range(0,MaxColumns-MinColumns):
    list = []
    for j in range(0,MaxRows-MinRows):
        list.append(".")
    DF[i]=list
print(DF)

def calc_distance_head_tail(HeadX,HeadY,TailX,TailY):
    Xdistance = abs(HeadX-TailX)
    Ydistance = abs(HeadY-TailY)
    if Xdistance <= 1 and Ydistance <= 1:
        Move = False
    else:
        Move = True
    return Move

HeadX = 0-MinRows
HeadY = 0-MinColumns
TailX = 0-MinRows
TailY = 0-MinColumns
NewHeadY = 0-MinRows
NewHeadX = 0-MinColumns
for i in range(0,len(Lines)):
    for j in range(0,Steps[i]):
        HeadY = NewHeadY
        HeadX = NewHeadX
        if Directions[i] == "U":
            NewHeadY += 1
        if Directions[i] == "D":
            NewHeadY -= 1
        if Directions[i] == "L":
            NewHeadX -= 1
        if Directions[i] == "R":
            NewHeadX += 1
        # print(NewHeadX,NewHeadY)
        if calc_distance_head_tail(NewHeadX,NewHeadY,TailX,TailY) == True:
            TailX = HeadX
            TailY = HeadY
        DF_New = DF.copy(deep=False)
        DF_New[TailX][TailY] = "T"
        # print(DF_New)
tail_visited = 0
# print(DF_New.columns)
# print(DF_New.columns.tolist())
for col in DF_New.columns.tolist():
    # print(DF_New[col])
    tail_visited+=DF_New[col].tolist().count("T")
print(tail_visited)