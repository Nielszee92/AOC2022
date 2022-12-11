File = open("Day_6_Input.txt", "r")
Lines = File.readlines()
print(Lines[0])
statement = True
Counter = 0
while statement == True:
    Start = max(0,Counter-13)
    Counter += 1

    # print(Lines[0][Start:Counter])
    uniques = list(set(Lines[0][Start:Counter]))
    # print(uniques)
    if len(uniques) == 14:
        print(Start, Counter)
        print("!00")
        statement = False
