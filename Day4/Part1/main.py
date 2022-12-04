data = []

with open("data.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        group = line.split(",")
        for krasnal in group:
            element = krasnal.split("-")
            element = [int(i) for i in element]
            print(element)
            data.append(element)


grouped:list[list[int]] = [(data[i:i+2]) for i in range(0, len(data), 2)]
print(grouped)

counter = 0

for ekipa in grouped:
    print(ekipa, end=" - ")
    if(
    ((ekipa[0][0] >= ekipa[1][0]) and (ekipa[0][1] <= ekipa[1][1]))
    or 
    ((ekipa[0][0] <= ekipa[1][0]) and (ekipa[0][1] >= ekipa[1][1]))):
        print("yes")
        counter+=1
    else:
        print("no")

print(counter)