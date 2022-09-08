new_list = [8, 3, 14, 5, 7, 10, 1, 2]

def choosing_list():
    for i in new_list:
        smallest = i
        for a in range(i+1, len(new_list)):
            if new_list[a] < new_list[smallest]:
                smallest = a
    new_list[i] = 0
    new_list[smallest] = 0

choosing_list()


