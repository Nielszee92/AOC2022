File = open("Day_5_Input.txt", "r")
Lines = File.readlines()
Statement = True
Dict = {}
move = []
from_ = []
to = []
for i in range(0,len(Lines)):
    if Statement == True:
        if len(Lines[i]) < 2:
            Statement = False
            # print(Lines[i-1])
            Columns = max(Lines[i-1].strip().split(" "))
            print("Columsn:",Columns)
            Rows = i
            print("Rows:",Rows)
    else:
        move.append(Lines[i].split(" ")[1])
        from_.append(Lines[i].split(" ")[3])
        to.append(Lines[i].strip().split(" ")[5])

for i in range(0,int(Columns)):
    Dict[i+1] = []
for j in range(0,Rows-1):
    for i in range(0,int(Columns)):

        if Lines[j][1+i*4] != " ":
            # print(Lines[j][1+i*4])
            Dict[i+1].append(Lines[j][1+i*4])
print(Dict)
for i in range(0,len(move)):
    for j in range(0,int(move[i])):
        print("to:",to[i])
        print("from:", from_[i])
        Dict[int(to[i])].insert(0,Dict[int(from_[i])][0])
        Dict[int(from_[i])].pop(0)
        print(Dict)
print(Dict)

string = ""
for i in range(0,int(Columns)):
    string += str(Dict[i+1][0])
print(string)