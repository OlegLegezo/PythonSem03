# 3. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

import time

l = int(input('Введите длинну числа: '))
a = time.time()
print(a)
ms = int(((a % 1) * (10 ** (l + 1))) % (10 ** (l)))
#ms = time.time()
#ms = int(time.time() % 10)

print(ms)







# from calendar import c

# i=1
# while i<100:
#     a = float(input('введите число a:'))
#     b=a*0.000123920123
#     d=round(int((b*1000192.94-b)/1000),4)
#     print(d)
#     i+=1
#     a=d

# 




# from datetime import datetime
# datetime.now()
# print(datetime.microsecond())


# from datetime import datetime 
# num = datetime.now()
# print(num.microsecond//1000)



# import time
# b = int(time.time())
# count = b%100
# if count == 0:
#     print (0)
# else:    
#     print(b%count*count)





# import time

# def sum_numbers(number):
#     sum = 0
#     for i in range(len(number)):
#         if number[i].isdigit():
#             sum += int(number[i])
#     return sum

# seconds = str(time.time())
# print(seconds)
# print(sum_numbers(seconds))