dict_1 = {}

with open('1.txt', encoding='utf-8') as file_1:
    line_1 = file_1.readlines()
    x = len(line_1)
    dict_1['1.txt'] = x

with open('2.txt', encoding = 'utf-8') as file_2:
    line_2 = file_2.readlines()
    y = len(line_2)
    dict_1['2.txt'] = y

with open ('3.txt', encoding= 'utf-8') as file_3:
    line_3 = file_3.readlines()
    z = len(line_3)
    dict_1['3.txt'] = z 

sorted_dict = sorted(dict_1.items(), key=lambda x: -x[1])

def max_line(dict__):
    for key,value in dict__:
        print(f'''{key}
Количество строк: {value}''')


max_line(sorted_dict)