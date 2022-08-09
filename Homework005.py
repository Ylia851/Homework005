# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55 то в итоге будет, 3*x^3 + 12*x^2+10*x+66

path1 = 'D:\PythonHomework\Homework005\polynomial1.txt'
f1 = open(path1, 'r')
data1 = f1.read() + ' '
f1.close()
print(data1)


path2 = 'D:\PythonHomework\Homework005\polynomial2.txt'
f2 = open(path2, 'r')
data2 = f2.read() + ' '
f2.close()
print(data2)

def GetCoef(pol):
    coef = []
    for i in pol:
        if (i!=' + ') and (i!='+'):
            coef.append(i.split('*'))
    coef = [tuple(x) for x in coef]
    print(coef)

pol1 = data1.split()
pol2 = data2.split()
p1 = GetCoef(pol1)
p2 = GetCoef(pol2)

def Sum(a, b):
    sum = ()
    for i in a:
        for j in b:
            if (j[0] == i[0]) and (i[0] > 1):
                sum += {i[1]+j[1]}
                print(f'{sum}*x**i[1]')
            elif (j[0] == i[0]) and (i[0] == 1):
                sum += {i[1]+j[1]}
                print(f'{sum}*x')
            elif (j[0] == i[0]) and (i[0] == 0):
                sum += {i[1]+j[1]}
                print(f'{sum}')
    return sum


    


# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

array = [1, 5, 2, 3, 4, 1, 7]

def Fun(a):
    arr = []

    a[0] = min(a)
    for i in range(len(a)):
        if a[i] - 1 != a[i - 1]:
            a2 = a[i]
    arr = [min(a), a2]
    return arr

print(Fun(array))

