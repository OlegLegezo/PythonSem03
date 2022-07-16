# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.


a = ['qwe1', 'qwet2', 'qwer3', 'qwer']
for i in a:
    if 'qwet' in i:
        print("есть")
    else:
        print("нет")
    print(i)


if 'qwet' in a:
    print("есть2")