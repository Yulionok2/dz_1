def dict_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding = 'utf-8') as file:
        for line_ in file:
            dish_name = line_.strip()
            line = file.readline()
            number = int(line)
            list_of_ingridient = []
            for ingridient in range(number):
                dict_1 = {}
                lines = file.readline().strip().split(' | ')
                for item in lines:
                    dict_1['ingredient_name'] = lines[0]
                    dict_1['quantity'] = lines[1]
                    dict_1['measure'] = lines[2]
                list_of_ingridient.append(dict_1)
                menu = {dish_name: list_of_ingridient}
                cook_book.update(menu)
            file.readline()

# dict_cook_book('cookbook.txt')

def get_shop_list_by_dishes(dishes, person_count):
    file_txt = dict_cook_book('cookbook.txt')
    dish_person = {}
    for dish in dishes:
        for item in (file_txt[dish]):
            items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*person_count})])
            dish_person += items_list
    print(f"На {person_count} персон нам необходимо купить:")
    print(dish_person)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)