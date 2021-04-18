sentence = input("Введите слова, разделенные пробелами:")
separate_words = sentence.split()
n = 0
for el in separate_words:
    n = n + 1
    if len(el) <= 10:
        print(n, el)
    else:
        print(n, el[0:10])
