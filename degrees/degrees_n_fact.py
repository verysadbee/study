#Функция проверки является ли переменные числами
def check_num(num): # принимает любое значение num
    num = str(num)
    k = 0
    for i in num:
        if i in '-.0123456789':
            k += 1
    if len(num) == k: # проверяет является ли num числом
        return True # возвращает True(bool)
    else: 
        return False # возращает False(bool)
 
#Степень
def stepen(num): # принимает любое значение num
    if check_num(num): # проверяет число, если функция возвращает True -
        st = (input('Введите степень: ')) # вводится степень
        if check_num(st): # проверяется, является ли степень числом
            return (num**float(st)) # возвращает число в степени st
        else:
            return ('Error_01') # если нет, выдает строку
    else: 
        return ('Error_01') # если нет, выдает строку

#Корень
def koren(num): # принимает любое значение num
    if check_num(num): # проверяет число, если функция возвращает True -
        st = (input('Введите степень: ')) # вводится степень
        if check_num(st): # проверяется, является ли степень числом
            return (num**(1/st)) # возвращает число в степени 1/st
        else:
            return ('Error_01') # если нет, выдает строку
    else: 
        return ('Error_01') # если нет, выдает строку
#Факториал
def fact(num): # принимает любое значение num
    if check_num(num) and num >= 0: # проверяет является ли num числом и больше ли оно нуля
        from math import factorial # импорт функции factorial из библотеки math
        return(factorial(num)) # возращает значение функции factorial(num)
    else:
        return ('Error_01$1') # если нет, выдает строку