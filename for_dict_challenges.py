# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
data = dict()
for student in students:#sorted(students, key=lambda d: d['first_name']):
    name = student['first_name']
    if data.get(name):
        data[name] = data[name] + 1
    else:
        data[name] = 1
for k, v in data.items():
    print(f'{k}: {v}')
# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
data = dict()
for student in students:
    name = student['first_name']
    if data.get(name):
        data[name] = data[name] + 1
    else:
        data[name] = 1
# весьма эзотерически выглядит, да, суть в том что я сортирую частотный словарь по значениям и беру последний элемент
most_frequent = sorted(data.items(), key=lambda item: item[1])[-1] # слава StackOverflow, а можно без лямбда-функций запилить?

print(f'\n{most_frequent[0]}: {most_frequent[1]}\n')
# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

def count_occurances_dry(input_list):
    data = dict()
    for student in input_list:
        name = student['first_name']
        if data.get(name):
            data[name] = data[name] + 1
        else:
            data[name] = 1
    return data
# ???


for index, class_element in enumerate(school_students, 1):
    names_frq = count_occurances_dry(class_element)
    # можно этого не делать, на конкретно этих данных все ок получается сразу но вообще говоря так не обязано быть
    most_frequent = sorted(names_frq.items(), key=lambda item: item[1], reverse=True)[0]
    print(f'Самое частое имя в классе {index}: {most_frequent[0]}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
print()
for klass in school:
    male_count = 0
    for student in klass['students']:
        if is_male[student['first_name']]:
            male_count += 1
    print(f"Класс {klass['class']}: девочки {len(klass['students']) - male_count}, мальчики {male_count}")




# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
print()
data = dict()
for klass in school:
    male_count = 0
    for student in klass['students']:
        if is_male[student['first_name']]:
            male_count += 1

    data[klass['class']] = (len(klass['students']) - male_count,male_count)

sorted_data = dict(sorted(data.items(),key=lambda item: item[1][1], reverse=True))

final_data = dict(zip(('Больше всего мальчиков в классе','Больше всего девочек'), sorted_data.keys())) # не по питонячьи много скобок больше скобок богу скобок
for k,v in final_data.items():
    print(f'{k} в классе {v}')

