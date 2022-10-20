Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Модуль тригонометрии
from math import *  #библиотека для тригонометрии

def isint(s):   #проверка на целое число
    try:
        int(s)
        return True
    except ValueError: 
        return False

# Функции тригонометрии

def msin(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        return (str(sin(int(x)))) #возрат значения синуса

def mcos(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        return (cos(int(x))) #возврат значения косинуса

def mtg(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        if cos(int(x)) == 0:
            return "o1" #ошибка деления на ноль
        else:
            return (sin(int(x))/cos(int(x))) #возврат значения тангенса

def mctg(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        if sin(int(x)) == 0:
            return "o1" #ошибка деления на ноль
        else:
            return (cos(int(x))/sin(int(x))) #возврат значения котангенса

def masin(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        if int(x) < -1 or int(x) > 1:
            return "o3" #ошибка области определения
        else:
            return (asin(int(x))) #возврат значения арксинуса

def macos(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        if int(x) < -1 or int(x) > 1:
            return "o3" #ошибка области определения
        else:
            return (acos(int(x)))  #возврат значения аркосинуса

def matg(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        return (atan(int(x))) #возврат значения арктангенса

def mactg(x):
    if not isint(x): # проверка на ввод
        return "o2" # код ошибки ввода
    else:
        return ((cos(int(x))/sin(int(x)))**-1) #возврат значения аркатангенса 
    #переводы
def hex_to_bi(x): #перобразование числа 16-ую в 2-ую
    return(bin(int(x, 16))) #возврат значения двоичного числа
def hex_to_dec(x): #перобразование числа 16-ую в 10-ую
    return(int(x, 16)) #возврат значения десятиричного числа
def hex_to_oct(x): #перобразование числа 16-ую в 8-ую
    return(oct(int(x, 16))) #возврат значения восьмиричного числа

x =input("Введите x: ")

print(hex_to_dec(x))