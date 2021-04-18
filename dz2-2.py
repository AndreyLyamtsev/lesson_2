str1 = input('Введите элемнты списка: ')
line = str1.split()
spis = list(line)
for el in range(1, len(spis), 2):
    spis.insert(el - 1, spis.pop(el))
print(spis)