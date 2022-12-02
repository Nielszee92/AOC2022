File = open("Day_2_Input.txt", "r")
Lines = File.readlines()

# A Y = rock paper = win
# B Z = paper scissor = win
# C X = scissor rock = win
Wins = ["A Y", "B Z", "C X"]
Draws = ["A X", "C Z", "B Y"]
# A X = rock rock = drwa
# C Z = scissor scissor = draw
# B Y = paper paper = draw
Losses = ["A Z", "B X", "C Y"]
# A Z = rock scissor = lose
# B X = paper rock = lose
# C Y = scissor paper = lose
Points = 0
for line in Lines:
    print(line.strip())
    if line.strip() in Wins:
        print("Win")
        Points += 6
    if line.strip() in Draws:
        print("Draw")
        Points += 3
    if "X" in line.strip():
        Points += 1
    if "Y" in line.strip():
        Points += 2
    if "Z" in line.strip():
        Points += 3
print(Points)