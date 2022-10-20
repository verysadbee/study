def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def to2(n):     # decimal to binary
    if n < 0:
        sign= '-'
    else:
        sign = ''
    n = abs(n)
    if str(n).isdigit() and not isint(n):     # input validation
        return(sign + "{0:b}".format(n))
    else:
        return "o1"
    

def to8(n):     # decimal to octal NS
    if n < 0:
        sign= '-'
    else:
        sign = ''
    n = abs(n)
    if str(n).isdigit() and not isint(n):     # input validation
        new_n = ''
        while n > 0:
            new_n = str(n % 8) + new_n
            n //= 8
        return(sign + new_n)
    else:
        return "o1"

def to16(n):    # decimal to hexadecimal
    if n < 0:
        sign= '-'
    else:
        sign = ''
    n = abs(n)
    if str(n).isdigit() and not isint(n):     # input validation
        if not hasattr(to16, 'table'):        
            to16.table = '0123456789ABCDEF'       
        x, y = divmod(n, 16)        
        return sign + to16(x) + to16.table[y] if x else sign + to16.table[y]
    else:
        return "o1"
