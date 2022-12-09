#         [Q] [B]         [H]        
#     [F] [W] [D] [Q]     [S]        
#     [D] [C] [N] [S] [G] [F]        
#     [R] [D] [L] [C] [N] [Q]     [R]
# [V] [W] [L] [M] [P] [S] [M]     [M]
# [J] [B] [F] [P] [B] [B] [P] [F] [F]
# [B] [V] [G] [J] [N] [D] [B] [L] [V]
# [D] [P] [R] [W] [H] [R] [Z] [W] [S]
#  1   2   3   4   5   6   7   8   9 
import re

def stackprinting(stacks):
    counter = 1
    for stack in stacks:

        print(counter, stack)
        counter += 1

stack1 = ["D", "B", "J", "V"]
stack2 = ["P", "V", "B", "W", "R", "D", "F"]
stack3 = ["R", "G", "F", "L", "D", "C", "W", "Q"]
stack4 = ["W", "J", "P", "M", "L", "N", "D", "B"]
stack5 = ["H", "N", "B", "P", "C", "S", "Q"]
stack6 = ["R", "D", "B", "S", "N", "G"]
stack7 = ["Z", "B", "P", "M", "Q", "F", "S", "H"]
stack8 = ["W", "L", "F"]
stack9 = ["S", "V", "F", "M", "R"]
stacks = [stack1,stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

data = []
counter = 0
with open("data.txt", "r") as file:
    for line in file:
        counter += 1
        line = line.replace("move", "")
        line = line.replace("from", "")
        line = line.replace("to", "")
        line = line.replace("\n", "")
        line = line.split()
        # line = re.split(r"[\D]", line)
        # line = [int(i) for i in line if i == i.isnumeric()]
        data.append(line)
        

data = [[int(item) for item in line] for line in data]
for item in data:
    print(item)
    try:
        for times in range(0, item[0]):
            poppeditem = stacks[item[1] - 1].pop()
            stacks[item[2] - 1].append(poppeditem)
            print("popped", poppeditem, "from", item[1], "to", item[2])
            stackprinting(stacks)

    except:
        pass

answer = []
for stack in stacks:
    if len(stack) != 0:
        answer.append(stack.pop())

print(answer)