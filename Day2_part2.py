File = open("Day_2_Input.txt", "r")
Lines = File.readlines()

# A Y = rock paper = win
# B Z = paper scissor = win
# C X = scissor rock = win
Dict = {}
Dict["Wins"] = {}
Dict["Wins"]["A"] = 2
Dict["Wins"]["B"] = 3
Dict["Wins"]["C"] = 1

Dict["Draws"] = {}
Dict["Draws"]["A"] = 1
Dict["Draws"]["B"] = 2
Dict["Draws"]["C"] = 3

Dict["Losses"] = {}
Dict["Losses"]["A"] = 3
Dict["Losses"]["B"] = 1
Dict["Losses"]["C"] = 2
Wins = ["A 2", "B 3", "C 1"]
Draws = ["A 1", "C 3", "B 2"]
# A X = rock rock = drwa
# C Z = scissor scissor = draw
# B Y = paper paper = draw
Losses = ["A 3", "B 1", "C 2"]
# A Z = rock scissor = lose
# B X = paper rock = lose
# C Y = scissor paper = lose
Points = 0
for line in Lines:
    if line[2] == "X":
        print("loss")
        Points += Dict["Losses"][line[0]]
        print(line[2],line[0],Dict["Losses"])
    if line[2] == "Y":
        print("draw")
        Points += 3
        Points += Dict["Draws"][line[0]]
        print(line[2],line[0], Dict["Draws"])
    if line[2] == "Z":
        print("win")
        Points += 6
        Points += Dict["Wins"][line[0]]
        print(line[2],line[0], Dict["Wins"])


print(Points)