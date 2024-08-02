my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_element = 0

while number_element <= len(my_list):
    if my_list[number_element] > 0:
        print(my_list[number_element])
        number_element += 1
    elif my_list[number_element] == 0:
        number_element += 1
        continue
    else: 
        break