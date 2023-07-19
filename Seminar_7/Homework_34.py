
vowels = 'ауоыэяюёие'
print(vowels)

list_vowels = [i for i in vowels]
print(list_vowels)

poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
list_poem = poem.split()
print(list_poem)

number_vowels = []
for i in list_poem:
    count = 0
    for j in i:
        if j in list_vowels:
            count += 1
    number_vowels.append(count)
print(number_vowels)

def result(my_list):
    for i in range(1, len(my_list)):
        if my_list[0] != my_list[i]:
            return 'Пам парам'
    return 'Парам пам-пам'

print(result(number_vowels))











