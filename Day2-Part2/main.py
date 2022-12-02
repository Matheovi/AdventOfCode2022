#!/usr/bin/env python3
#Rock Paper Scissors data
#A - Rock, enemy, 1 point
#B - Paper, enemy, 2 points
#C - Scissors, enemy, 3 points
#X - loose
#Y - draw
#Z - win

#    X   Y   Z
#
# A   3   4   8
#
# B   1   5   9
#
# C   2   6   7

data = {
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7,
}

sum_of_points = 0
with open("data.txt", "r") as file:
    for line in file:
       sum_of_points+=data[line]


print(sum_of_points)
