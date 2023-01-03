word = input('Введите текст :')
letter = input('Введите букву :')
count = 0

for i in word:
    if i == letter:
        count += 1
    
    
print('Число букв в тексте :', count)
