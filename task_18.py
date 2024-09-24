N = int(input("Введите число элементов в массиве: "))

A = []
for i in range(N):
    A.append(int(input(f'Введите {i+1} элемент массива: ')))
    
X = int(input('Введите число X: '))


def find_closest(A, X):
    closest_element = A[0]
    min_diff = abs(A[0] - X)
    for element in A:
        diff = abs(element - X)
        if diff < min_diff:
            min_diff = diff 
            closest_element = element
    return closest_element


count = find_closest(A, X)
print(f'Самый близкийэлмент к задому числу {X}: {count}')

