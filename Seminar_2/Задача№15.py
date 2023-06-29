# Задача №15. Общее обсуждение
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

from random import  randint

quantity = int(input("Введите кол-во арбузов на прилавке: "))
minimum_weight = float('inf') #Задается бесконечно минимальное число
maximum_weight = float('-inf') #Задается бесконечно максимальное число
count = 1
print(f"\nНа прилавке лежат арбузы массой, кг: ")
while count <= quantity:
    weight = randint(2, 30)
    print(f"{weight}", end=",")
    if weight > maximum_weight:
        maximum_weight = weight
    elif weight < minimum_weight:
        minimum_weight = weight
    count +=1
print(f"\nМасса самого большого арбуза составляет {maximum_weight}")
print(f"А масса самого маленького арбуза составляет {minimum_weight}")