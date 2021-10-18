with open('1.txt', encoding='utf-8') as file_1:
    counter_1 = 0
    lines_1 = ['1.txt\n']
    while True:
        line = file_1.readline()
        if len(line) == 0:
            break
        lines_1.append(line)
        counter_1 += 1
lines_1.insert(1, str(counter_1))
lines_1.insert(2, '\n')     
print(lines_1)

with open('2.txt', encoding='utf-8') as file_2:
    counter_2 = 0
    lines_2 = ['2.txt\n']
    while True:
        line = file_2.readline()
        if len(line) == 0:
            break
        lines_2.append(line)
        counter_2 += 1
lines_2.insert(1, str(counter_2))
lines_2.insert(2, '\n')  
print(lines_2)

with open('3.txt', 'a', encoding='utf-8') as file_3:
    if counter_1 >= counter_2:
        file_3.writelines(lines_1)
        file_3.write('\n')
        file_3.writelines(lines_2)
    else:
        file_3.writelines(lines_2)
        file_3.write('\n')
        file_3.writelines(lines_1)

        
