#!/usr/bin/env python3

def group_elves():
  krasnale = []
  suma = 0
  with open("data.txt", "r") as file:
    for line in file:
      line = line.replace("\n","")
      if len(line) == 0:
        krasnale.append(suma)
        suma = 0
      else:
        suma += int(line)
  return krasnale



elves = group_elves()
elves.sort(reverse=True)

sum_of_three_elves = elves[0]+elves[1]+elves[2]


#if __name__ == "__main__":
print(sum_of_three_elves)
