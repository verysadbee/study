#Перевод из 8 сс в другие
def check_oct(num): # функции для проверки число в восьмеричной системе или нет
    numbers = [] # объявление пустого списка
    num = str(num) # перевод числа в строку
    for i in num: # проход по элементам строки
        if i not in ['8','9']: # если элемент не 8 и не 9
            numbers.append(i) # то добавляется в список numbers
    if len(numbers) == len(num): # если длина списка = длине изначального числа
        return True # возвращает True(bool)
    else: # если нет
        return False # возращает False(bool) 

# Сам перевод из 8 системы счисления
def perevod_8_ss(num): # принимает число
    convert_system = int(input('Введите желаемую в выводе систему счисления (2,10,16): ')) 
    if check_oct(num): # если функция с принятым значением передает True(bool)
        if int(num) > 0:
            if convert_system == 8: # если желаемая система счислений - 8
                return num # возращает само число
            if convert_system == 10: # если желаемая система счислений - 10 
                return int(num,8) # возравщает число в 10 сс
            if convert_system == 2: # если желаемая система счислений - 2
                ans = int(num,8) # перевод в десятичную сс
                ans = bin(int(ans)) # перевод в 2-сс 
                return ans.replace('0b','') # уберается кодировка с помощью replace
            if convert_system == 16: # если желаемая система счислений - 16
                ans = int(num,8) # перевод в десятичную сс
                ans = hex(int(ans)) # перевод в 16-сс
                return ans.replace('0x','').upper() # уберается кодировка с помощью replace
            if convert_system not in [2,8,16,10]: # если желаемая сс не 2 10 16
                return 'Error_03'
        else:
            return ('Error_02') # возращает ошибку, если число не в 8 сс или меньше нуля
    else:
        return ('Error_02') # возращает ошибку, если число не в 8 сс или меньше нуля
