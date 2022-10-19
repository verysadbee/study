from arif import arifmetika
from degrees import degrees_n_fact

def isnum(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def print_result(res):
    print('Результат:',res)

res = ''

while True:
    vibor = input('Введите команду: ')
    if vibor in ['sum','vich','chast','umn']:
        if res == '':
            x = input('Введите первое число: ')
        elif type(res) == float:
            x = res
        y = input('Введите второе число: ')
        if vibor == 'sum':
            if isnum(x) and isnum(y):
                res = arifmetika.summa(float(x),float(y))
                print_result(res)
            else:
                print_result(arifmetika.summa(x,y))
                res = ''
        if vibor == 'vich':
            if isnum(x) and isnum(y):
                res = arifmetika.vich(float(x),float(y))
                print_result(res)
            else:
                print_result(arifmetika.vich(x,y))
                res = ''
        if vibor == 'chast':
            if isnum(x) and isnum(y):
                res = arifmetika.chast(float(x),float(y))
                print_result(res)
            else:
                print_result(arifmetika.chast(x,y))
        if vibor == 'umn':
            if isnum(x) and isnum(y):
                res = arifmetika.umn(float(x),float(y))
                print_result(res)
            else:
                print_result(arifmetika.umn(x,y))
                res = ''
    elif vibor in ['fact','koren','stepen']:
        if res == '':
            x = input('Введите число: ')
        elif type(res) == float or type(res) == int:
            x = res
        if vibor == 'fact':
            if isnum(x):
                res = degrees_n_fact.fact(int(x))
                print_result(res)
            else:
                print_result(degrees_n_fact.fact(x))
                res = ''
        if vibor == 'koren':
            if isnum(x):
                res = degrees_n_fact.koren(float(x))
                print_result(res)
            else:
                print_result(degrees_n_fact.koren(x))
                res = ''
        if vibor == 'stepen':
            if isnum(x):
                res = degrees_n_fact.stepen(float(x))
                print_result(res)
            else:
                print_result(degrees_n_fact.stepen(x))
                res = ''      
    elif vibor == 'end':
        exit('ББ')
    elif vibor == 'sbros':
        res = ''
        print('Сброшено успешно :}')
    else:
        print('Такой команды нет :{')