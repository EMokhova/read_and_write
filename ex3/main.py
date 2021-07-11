import os
import operator



def get_files_list(directory):
    files = os.listdir(directory)
    file_list = []
    for file in files:
        if os.path.isfile(os.path.join(directory, file)) and file.endswith('.txt'):
            file_list.append(file)
    print(file_list)
    return file_list


def read_and_write_files():
    file_list = get_files_list('D:\lesson 6\ex3')
    data = {}

    for files in file_list:
        with open(files, "r", encoding="utf-8") as file:
            count = 0
            for line in file:
                count += 1
            data[files] = count
        print(count)
    print(data)
    sorted_tuples = sorted(data.items(), key=operator.itemgetter(1))
    sorted_dict = {k: v for k, v in sorted_tuples}
    print(sorted_dict)

    for key, value in sorted_dict.items():
        with open("4.txt", "a", encoding="utf-8") as f:
            f.write(key + '\n')
            f.write(str(value) + '\n')
            with open(key, "r", encoding="utf-8") as fl:
                content = fl.read()
            f.write(content + '\n')



read_and_write_files()

