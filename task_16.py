N = int(input("Введите число элементов в массиве: "))

A = []
for i in range(N):
    A.append(int(input(f'Введите {i+1} элемент массива: ')))
    
X = int(input('Введите число X: '))


count = 0
for element in A:
    if element == X:
        count += 1
        
    
        
print(f'Число {X} встречается в массиве {count} раз')

    



