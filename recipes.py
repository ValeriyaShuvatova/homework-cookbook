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




def rewrite_file():
    with open("1.txt", 'r', encoding='utf-8') as f1:
        x_1 = len(f1.readlines())
        # print(x_1)
    with open("2.txt", 'r', encoding='utf-8') as f2:
        x_2 = len(f2.readlines())
        # print(x_2)

    with open("3.txt", 'r', encoding='utf-8') as f3:
        x_3 = len(f3.readlines())
        # print(x_3)
    with open("rewrite_file.txt", 'w', encoding='utf-8') as f_total:

        # f_total.write():
        if x_1 < x_2 and x_1 < x_3:
            f_total.write("1.txt" + '\n')
            f_total.write(str(x_1) + '\n')
            f_total.writelines(f1)
            f_total.write('\n')
        elif x_2 < x_1 and x_2 < x_3:
            f_total.write("2.txt" + '\n')
            f_total.write(str(x_2) + '\n')
            f_total.writelines(f2)
            f_total.write('\n')
        elif x_3 < x_1 and x_3 < x_2:
            f_total.write("3.txt" + '\n')
            f_total.write(str(x_3) + '\n')
            f_total.writelines(f3)
            f_total.write('\n')
        if x_2 > x_1 > x_3 or x_2 < x_1 < x_3:
            f_total.write("1.txt" + '\n')
            f_total.write(str(x_1) + '\n')
            f_total.writelines(f1)
            f_total.write('\n')
        elif x_1 > x_2 > x_3 or x_2 > x_1 and x_2 < x_3:
            f_total.write("2.txt" + '\n')
            f_total.write(str(x_2) + '\n')
            f_total.writelines(f2)
            f_total.write('\n')
        elif x_1 > x_3 > x_2 or x_3 > x_1 and x_3 < x_2:
            f_total.write("3.txt" + '\n')
            f_total.write(str(x_3) + '\n')
            f_total.writelines(f3)
            f_total.write('\n')
        if x_1 > x_2 and x_1 > x_3:
            f_total.write("1.txt" + '\n')
            f_total.write(str(x_1) + '\n')
            f_total.writelines(f1)
        elif x_2 > x_1 and x_2 > x_3:
            f_total.write("2.txt" + '\n')
            f_total.write(str(x_2) + '\n')
            f_total.writelines(f2)
        elif x_3 > x_1 and x_3 > x_2:
            f_total.write("3.txt" + '\n')
            f_total.write(str(x_3) + '\n')
            f_total.writelines(f3)
    return rewrite_file()

print("Задача №1")
print("cook_book =", *cook_book.items(), sep="\n")
print()
print("Задача №2")
print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2), sep="\n")
print()
print("Задача №3")

