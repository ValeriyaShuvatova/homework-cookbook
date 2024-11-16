from importlib.metadata import files
from operator import itemgetter
from socket import socket

cook_book = {}

with open('recipes.txt', encoding='utf-8') as file:
    last_key = ''
    for line in file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            last_key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))




def get_shop_list_by_dishes(dishes, person_count):
     ingr_list = {}
     for line in dishes:
         if line in cook_book:
             for i in cook_book[line]:
                meas_quan_list = {}
                if i['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = i['measure']
                    meas_quan_list['quantity'] = i['quantity'] * person_count
                    ingr_list[i['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[i['ingredient_name']]['quantity'] = ingr_list[i['ingredient_name']]['quantity'] + \
                                                                     i['quantity'] * person_count

         else:
            print(f'\n"Такого блюда нет в списке!"\n')
     return ingr_list



import os

list = ("1.txt", "2.txt", "3.txt")



for item in list:
    list_final = []
    with open("1.txt", 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
        list_general = ("1.txt", len(file1), file1)
        list_final.append(list_general)
    with open("2.txt", 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
        list_general = ("2.txt", len(file2), file2)
        list_final.append(list_general)
    with open("3.txt", 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
        list_general = ("3.txt", len(file3), file3)
        list_final.append(list_general)

list_total = sorted(list_final, key=itemgetter(2), reverse=True)
line = "\n".join(map(str, list_total))



with open("rewrite_file.txt", 'w', encoding='utf-8') as f_total:
    f_total.write(line)


print("Задача №1")
print("cook_book =", *cook_book.items(), sep="\n")
print()
print("Задача №2")
print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2), sep="\n")
print()
print("Задача №3")

