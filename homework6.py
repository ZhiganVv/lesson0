my_dict = {'Anton': 11, 'Vasia': 12, 'Petia': 14}
print(my_dict)
print(my_dict.get('Vasia', 'Нет в списке'))
print(my_dict.get('Vladimir', 'Нет в списке'))
my_dict.update({'Vlaimir': 16,
                'Ivan': 20})
print(my_dict)
print(my_dict.pop('Vasia'))
print(my_dict)

print()

my_set = {2, 4, 5, 2, 1, 1, (5, 6, 7),'Ivan', 6, 8, 4}
print('Original_set: ', my_set)
my_set.add(11)  # Добавил 1 элемент
my_set.update({12, 14, 16})  # Добавил несколько элементов
my_set.remove('Ivan')
print('Update_set: ', my_set)
