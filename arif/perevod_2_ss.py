#Функция проверки на двочиное число
def check_bin(num): #Принимает num- любое значение
    numbers = [] #Объявление списка
    num = str(num) #Перевод из числа в строку
    for i in num: #Проход по строке
        if i in ['1','0']: #Является ли ЦИФРА единицей или нулем
            numbers.append(i) #Если да, записывается в список
    if len(numbers) == len(num): #Если длина нового списка такая же как и длина изначального числа
        return True #То число двоичное
    else:
        return False #Если нет, то нет.

#Функция перевода из двоичной сс во все остальные
def perevod(num,convert_system): #Принимает num- любое значение, convert_system
    if check_bin(num): #Проверка является ли число двоичным
        if convert_system == 10: #Если нужно перевести в 10
            return int(num,2) #Переводит в 10-ую сс
        if convert_system == 8: #Если нужно перевести в 8
            ans = int(num,2) #Перевод в 10-ую сс
            ans = oct(int(ans)) #Перевод в 8-ую сс
            return ans.replace('0o','') #Вывод результата без 0о, которое образуется от функции oct
        if convert_system == 16: #Если нужно в 16-ую сс
            ans = int(num,2) #Перевод в 10-ую сс
            ans = hex(int(ans)) #Перевод в 16-ую сс
            return ans.replace('0x','').upper() #Вывод результата без 0х, котрое образуется от функции hex
        if convert_system == 2: #Если нужно перевести в 2 сс
            ans = int(num) #Ответ равен самому числу
            return num #Возвращает число
    else:
        raise Exception("Error 003") #Если число не является двоичный, то выдает ошибку
