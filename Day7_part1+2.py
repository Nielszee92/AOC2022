File = open("Day_7_Input.txt", "r")
from collections import defaultdict
Lines = File.readlines()
FileTree = defaultdict(int)
CWD = []
for line in Lines:
    if "$ cd" in line:
        if ".." in line:
                CWD.pop()
        else:
            directory = line.replace("$ cd","").strip()
            CWD.append(directory)
        print(CWD)
    elif "$ ls" in line:
        continue
    elif "dir" in line:
        continue
    else:
        # try:
            size = int(line.split(" ")[0])
            print(line)
            for i in range(len(CWD)):
                print(i,CWD[i])
                print("/".join(CWD[:i+1]))
                FileTree["/".join(CWD[:i+1])] += size
        # except:
        #     pass
print(FileTree)
ans = 0
for ele in FileTree:
    print(ele, FileTree[ele])
    if FileTree[ele] <= 100000:
        ans += FileTree[ele]
print(ans)

Space = 70000000
Unused = 30000000
MaxUsed = Space-Unused
CurrentUsed = 40913445
Remove = CurrentUsed-MaxUsed
print(Remove)
Dict = {}
for ele in FileTree:
    if FileTree[ele] >= Remove:
        Dict[ele] = FileTree[ele]
a = sorted(FileTree.items(), key=lambda x: x[1])
print(a)