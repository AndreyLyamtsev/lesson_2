box = [9, 7, 5, 3, 2, 2]
n = int(input('Введите элемент рейтинга:'))
a = 0
for el in box:
    if el >= n:
        a = a + 1
box.insert(a, n)
print(box)
