def same(a1, a2):
    a2copy = a2
    if len(a1) != len(a2): return False
    else:
        for i in range(len(a1)):
            if not contains(a2copy, a1[i]*a1[i]):
                return False
            a2copy.remove(a1[i]*a1[i])
        return True

def contains(niz, n):
    for i in range(len(niz)):
        if niz[i] == n: return True
    return False

def countUniqueValues(niz):
    b = list(set(niz))
    return len(b)
    return

def cammel(str):
    niz = str.split()
    rez=''
    for i in niz:
        if i[0].isupper():
            string = i[0].lower()+i[1:]
            rez += string
        else:
            rez += i.capitalize()
    rez=rez[:-1]
    return rez

print(same([1,2,3],[1,9]))

print(countUniqueValues([1, 2, 1, 2, 2, 4, 4]))

str = 'Aaa bbb ccc'

print(cammel('Enida je zavrsila c!'))

