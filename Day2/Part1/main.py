#Rock Paper Scissors data
#A - Rock, enemy, 1 point
#B - Paper, enemy, 2 points
#C - Scissors, enemy, 3 points
#X - Rock, player, 1 point
#Y - Paper, player, 2 points
#Z - Scissors, player, 3 points

#    X   Y   Z
#
# A   4   8   3
#
# B   1   5   9
#
# C   7   2   6

data = {
    "A X\n": 4,
    "A Y\n": 8,
    "A Z\n": 3,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 7,
    "C Y\n": 2,
    "C Z\n": 6,
}

sum_of_points = 0
with open("data.txt", "r") as file:
    for line in file:
       sum_of_points+=data[line]


print(sum_of_points)
