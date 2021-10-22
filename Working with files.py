from pprint import pprint

def get_cook_book(file):
    with open(file, encoding='utf-8') as file:
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
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    menu = {}
    for dish in dishes:
        for ingr in get_cook_book('Recipes.txt')[dish]:
            if ingr['ing_name'] in menu.keys():
                menu[ingr['ing_name']]['quantity'] += ingr['quantity'] * person_count
            else:
                menu[ingr['ing_name']] = {}
                menu[ingr['ing_name']]['quantity'] = ingr['quantity'] * person_count
                menu[ingr['ing_name']]['measure'] = ingr['measure']
    return menu        

pprint(get_cook_book('Recipes.txt'))
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 3))