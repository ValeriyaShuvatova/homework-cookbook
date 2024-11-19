import operator
import os.path
import os

#Задача №1
with open("recipes.txt", encoding="utf-8") as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients =[]
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split("|")
            product, quantity, word = recepie
            ingredients.append({"product": product, "quantity": int(quantity), "measure": word})
        file.readline()
        cook_book[recepie_name] = ingredients
    print("cook_book =", *cook_book.items(), sep="\n")

# Задача №2
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist["product"]]["quantity"] = consist["quantity"]*person_count
                else:
                    result[consist["product"]] = {"measure": consist["measure"], "quantity": (consist["quantity"]*person_count)}
        else:
            print("Такого блюда нет в книге")

    print(result)
get_shop_list_by_dishes(2, ["Запеченный картофель", "Омлет"])


#Задача 3
import os
from operator import itemgetter


all_files = [file for file in os.listdir() if file.endswith(".txt")]
all_files = all_files[:3]
list_final = []
for item in all_files:

    with open(item, "r", encoding="utf-8") as file:
        read_file = file.readlines()
        list_final.append([item, len(read_file), read_file])

sorted_list_final = sorted(list_final, key=itemgetter(1))
line = "\n".join(map(str, sorted_list_final))
# print(line)
with open("rewrite_file.txt", 'a', encoding='utf-8') as f_total:
      f_total.writelines(line)














