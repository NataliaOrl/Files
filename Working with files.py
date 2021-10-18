from pprint import pprint

with open('Recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipe in file:
        recipe_name = recipe.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            ing_name, quantity, measure = file.readline().split('|')
            temp_data.append(
                {'ing_name':ing_name.strip(), 'quantity': int(quantity.strip()),'measure':measure.strip()}
            )
            cook_book[recipe_name] = temp_data
        file.readline()
    print('cook_book =')
    pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    menu = []
    for k, v in cook_book.items():
    # print(k)
        if k in dishes:
            for el in v:
                menu.append({el['ing_name']:{'quantity':el['quantity'] * person_count, 'measure': el['measure']}})
    print(*menu, sep='\n')     

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)