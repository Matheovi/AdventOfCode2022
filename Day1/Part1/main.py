def find_elf():
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


  return max(krasnale)






#if __name__ == "__main__":
print(find_elf())
