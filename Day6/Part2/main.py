with open("data.txt", 'r') as file:
    data = file.read()

#print(data)

counter = 0

for x in range(0, len(data)):
    counter += 1
    data_window = data[x:x+14]
    #sprint(data[x:x+4], x, x+4, set(data_window), len(set(data_window)))
    if len(set(data_window)) == 14:
        print(data_window, "C=", counter + 13)
        break










#TODO: ogarnij set zeby pakowal 4 itemy do setu i jesli len(set) jest 4 to znaczy ze kazdy znaczek jest unikalny