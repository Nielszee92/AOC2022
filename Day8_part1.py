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
    print("row, column =", row,column)
    Visible = False
    #Up
    if all(item < DF[column][row] for item in DF.iloc[0:row,column].values.tolist()):
        # print("up")
        # print('Tree is visible')
        # print(DF[column][row])
        # print(DF.iloc[0:row,column].values.tolist())
        Visible = True
    # else:
    #     print("up")
    #     print('Tree is not visible')
    #     print(DF[column][row])
    #     print(DF.iloc[0:row,column].values.tolist())
    #Down
    if all(item < DF[column][row] for item in DF.iloc[row+1:,column].values.tolist()):
        # print("down")
        # print('Tree is visible')
        # print(DF[column][row])
        # print(DF.iloc[row+1:,column].values.tolist())
        Visible = True
    # else:
    #     print("down")
    #     print('Tree is not visible')
    #     print(DF[column][row])
    #     print(DF.iloc[row+1:,column].values.tolist())
    #Left
    if all(item < DF[column][row] for item in DF.iloc[row,0:column].values.tolist()):
        # print('Tree is visible')
        # print("left")
        # print(DF[column][row])
        # print(DF.iloc[row,0:column].values.tolist())
        Visible = True
    # else:
        # print("left")
        # print('Tree is not visible')
        # print(DF[column][row])
        # print(DF.iloc[row,0:column].values.tolist())
    #Right
    if all(item < DF[column][row] for item in DF.iloc[row,column+1:].values.tolist()):
        # print('Tree is visible')
        # print("right")
        # print(DF[column][row])
        # print(DF.iloc[row,column+1:].values.tolist())
        Visible = True
    # else:
        # print("right")
        # print('Tree is not visible')
        # print(DF[column][row])
        # print(DF.iloc[row,column+1:].values.tolist())

    return Visible
ans = 0
for k in range(1,len(Lines)-1):
    for l in range(1,len(Lines[k].strip())-1):
        if CheckVisibility(k,l) == True:
            print("+1")
            ans += 1
print(ans)
