# Задание №1



def create_cookbook():
    cook_book = {}
    with open("recipes.txt", encoding='utf-8') as fail:

        for i in fail:
            recipe_name = i.strip()
            ingredients_count = fail.readline()
            list_ingredients = []
            for j in range(int(ingredients_count)):
                recipe = fail.readline().strip().split(' | ')
                product, quantity, word = recipe
                list_ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': word})
            fail.readline()
            cook_book[recipe_name] = list_ingredients
        print("cook_book =", *cook_book.items(), sep="\n")
        # print("cook_book =", create_cookbook())
        return cook_book


cook_book = create_cookbook()



# Задание №2

def get_shop_list_by_dishes(dishes: list, person_count: int):
    shop_product = {}
    for dish in dishes:
        if dish in cook_book:  # Если ингридиент уже есть в словаре
            for product in cook_book[dish]:  # {'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'}
                if product['ingredient_name'] in shop_product:
                    shop_product[product['ingredient_name']]['quantity'] += int(product['quantity']) * person_count
                else:
                    shop_product[product['ingredient_name']] = {'measure': product['measure'],
                                                                'quantity': int(product['quantity']) * person_count}
        else:
            print('Блюда нет в кулинарной книге')
    print(shop_product)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)





