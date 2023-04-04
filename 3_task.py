def create_list(name):
    with open(name, 'rt', encoding='utf-8') as file:
        list = file.readlines()
        f = [name, str(len(list))]
        for line in list:
            f.append(line.strip())
        return f

def write_to_file(name_1, name_2, name_3):
    all_list = [create_list(name_1),create_list(name_2), create_list(name_3)]
    all_list.sort(key=len)
    with open('4.TXT', 'w', encoding='utf-8') as task_3:
        for i in all_list:
            for j in i:
                task_3.write(j + '\n')

write_to_file('1.TXT', '2.TXT', '3.TXT')























