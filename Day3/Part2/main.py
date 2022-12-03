
def find_badge(group: list[str]) -> str: 
    first_krasnal = group[0]
    second_krasnal = group[1]
    third_krasnal = group[2]

    for char in first_krasnal:
        if (char in second_krasnal) and (char in third_krasnal):
            print("found", char)
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
    list_from_file = []
    odd_items: list[int] = []
    with open('data.txt', "r") as file:
    
        for line in file:
            line = line.replace("\n", "")
            list_from_file.append(line)


    group_of_three = [list_from_file[i:i+3] for i in range(0, len(list_from_file), 3)]
    for group in range(0, len(group_of_three)):
        badge = find_badge(group_of_three[group])
        sum += convert_char_to_priority(badge)
        odd_items.append(convert_char_to_priority(badge))
            

    print(sum)





if __name__ == "__main__":
    main()


