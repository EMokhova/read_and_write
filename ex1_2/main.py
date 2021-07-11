import os
from pprint import pprint
from typing import Optional


def get_dict():
    #folder_path = os.getcwd()
    #path = f'{folder_path}/"recipes.txt"'
    cook_book = {}
    with open("recipes.txt", "r", encoding="utf-8") as file:
        for line in file:
            dish = line.strip()
            ingredient = int(file.readline().strip())
            ingredient_list = []
            for ingredients in range(ingredient):
                data = file.readline().strip()
                ingredient_dict = {'ingredient_name': None, 'quantity': None, 'measure': None}
                list = data.split('|')
                for key, value in zip(ingredient_dict.keys(), list):
                    ingredient_dict[key] = value
                ingredient_list.append(ingredient_dict)
            file.readline()
            cook_book[dish] = ingredient_list
    return cook_book


pprint(get_dict())


def get_shop_list_by_dishes(dishes, person_count=1):
    cook_book = get_dict()
    menu_list = {}
    for elem in dishes:
        for dish, ingredient_list in cook_book.items():
            if dish == elem:
                ingredient_list = cook_book.get(dish)
                for ingredient in ingredient_list:
                        for key, value in ingredient.items():
                            ingredient_name = ingredient.get('ingredient_name')
                            measure = ingredient.get('measure')
                            quantity = int(ingredient.get('quantity'))
                            quantitys = quantity * person_count
                            if ingredient_name in menu_list:
                                for key, quantity_list in menu_list.items():
                                    if key == ingredient_name:
                                        for k,v in quantity_list.items():
                                            quantity_list['quantity'] += quantitys
                        else:
                           quantity_list = {'measure': measure, 'quantity': quantitys}
                           menu_list[ingredient_name] = quantity_list
    pprint(menu_list)
    return menu_list



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
