
def find_odd_item(line) -> str: 
    first_half:str = line[:len(line)//2]
    second_half:str = line[len(line)//2:]
    for char in first_half:
        if char in second_half:
            #print("found", char)
            return char
    return ""


#a - z => 1  - 26
#A - Z => 27 - 52
def convert_char_to_priority(char:str)->int:
    if char.isupper():
        print("converted:", char, ord(char) - 38)
        return ord(char) - 38
    else:
        print("converted:", char, ord(char) - 96)
        return ord(char) - 96





def main():
    sum = 0
    odd_items: list[int] = []
    with open('data.txt', "r") as file:
        for line in file:
            line = line.replace("\n", "")
            odd_char = find_odd_item(line)
            sum += convert_char_to_priority(odd_char)
            odd_items.append(convert_char_to_priority(odd_char))
            

    print(sum)





if __name__ == "__main__":
    main()


