import pandas as pd
File = open("Day_8_Input.txt", "r")
Lines = File.readlines()
width = len(Lines[0].strip())
height = len(Lines)
DF = pd.DataFrame()
for i in range(0,len(Lines[0])-1):
    list = []
    for j in range(0,len(Lines)):
        list.append(int(Lines[j][i]))
    DF[i]=list
print(DF)
def CheckVisibility(row,column):
    # print("row, column =", row,column)
    Visible = False
    #Up
    if all(item < DF[column][row] for item in DF.iloc[0:row,column].values.tolist()):
        Visible = True
    #Down
    if all(item < DF[column][row] for item in DF.iloc[row+1:,column].values.tolist()):
        Visible = True
    #Left
    if all(item < DF[column][row] for item in DF.iloc[row,0:column].values.tolist()):
        Visible = True
    #Right
    if all(item < DF[column][row] for item in DF.iloc[row,column+1:].values.tolist()):
        Visible = True
    return Visible

def calculate_scenic_score(row,column):
    upscore = 0
    downscore = 0
    leftscore = 0
    rightscore= 0
    # print("test")
    for upcounter in range(0,row):
        # print(upcounter)
        # print("up",DF[column][row] , DF[column][row-upcounter-1],DF[column][row] > DF[column][row-upcounter-1],upcounter)
        upscore += 1
        if DF[column][row] > DF[column][row-upcounter-1]:
            continue
        else:
            break
    for downcounter in range(row+1,len(Lines)):
        # print("down",DF[column][row], DF[column][downcounter], DF[column][row] > DF[column][downcounter],downcounter)
        downscore += 1
        if DF[column][row] > DF[column][downcounter]:
            continue
        else:
            break
    for leftcounter in range(0,column):
        # print("left",DF[column][row], DF[column-leftcounter-1][row], DF[column][row] > DF[column-leftcounter-1][row],leftcounter)
        leftscore += 1
        if DF[column][row] > DF[column-leftcounter-1][row]:
            continue
        else:
            break
    for rightcounter in range(column+1,len(Lines[0])-1):
        # print("right",DF[column][row], DF[rightcounter][row], DF[column][row] > DF[rightcounter][row],rightcounter)
        rightscore += 1
        if DF[column][row] > DF[rightcounter][row]:
            continue
        else:
            break

    # print("Scenic score = ",upscore,leftscore,downscore,rightscore)
    return upscore*downscore*leftscore*rightscore



ans = 0
scenic_score = 0
for k in range(1,len(Lines)-1):
    for l in range(1,len(Lines[k].strip())-1):
        # print("row,col",k,l)
        if CheckVisibility(k,l) == True:
            scenic_score = max(scenic_score,calculate_scenic_score(k,l))
            # print("+1")
            ans += 1
print(ans)
print(scenic_score)
