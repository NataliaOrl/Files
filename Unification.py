def read_file(file):
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        return lines

def list_file(files):
        list = []
        len_dict = {}
        for el in files:
            len_dict |= {len(read_file(el)):[el, read_file(el)]}
        for key, value in sorted(len_dict.items(), key = lambda x: x[0]):
            list.append(value[0])
            list.append('\n')
            list.append(str(key))
            list.append('\n')
            for v in value[1]:
                list.append(v)
            list.append('\n')
        return list

def write_file(new_file, files):
    with open(new_file, 'a', encoding='utf-8') as new_f:
        new_f.writelines(list_file(files))

import os
directory = (r'C:\Users\Natalia\Desktop\PYTHON\Files')
files = os.listdir(directory)
for name in files:
    write_file('3.txt', files)

# write_file('3.txt', ['1.txt', '2.txt'])

        
