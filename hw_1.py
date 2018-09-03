# Задача 1.1
a1 = 5
a2 = "Hello world!"
print("Переменная 1:", a1, " Переменная 2:", a2)
a3 = input("Введите значение переменной 3:")
print("Перемнная 3:", a3)

print("")
# Задача 1.2
a = int(input("Введите значение переменной а:"))
a = a + 2
print(a)

print("")
# Задача 1.3
age = int(input("Укажите свой возраст:"))
if (age >= 18):
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

print("")
# Задача 2.1
a = int(input("Введите число:"))
if (a > 0 and a < 10):
    print(a**2)
else:
    while(a <= 0 or a >= 10):
        print("Введенное число не входит в заданный диапазон от 0 до 10 (не включая), введите корректное значение!")
        a = int(input())
    print(a**2)

print("")
# Задача 2.2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
a = a + b
b = a - b
a = a - b
print(a, b)

print("")
# Задача 3.1
name = input("Укажите Ваше имя:")
surname = input("Укажите Вашу фамилию:")
age = int(input("Укажите Ваш возраст:"))
weight = int(input("Укажите Ваш вес:"))
if (age <= 30 and weight >= 50 and weight <= 120):
    print(name, surname, ",", age, "лет, вес", weight, "- хорошее состояние")
elif ((age > 30 and age <= 40) and (weight < 50 or weight > 120)):
    print(name, surname, ",", age, "лет, вес", weight, "- следует заняться собой")
elif (age > 40 and (weight < 50 or weight > 120)):
    print(name, surname, ",", age, "лет, вес", weight, "- следует обратиться к врачу")
else:
    print(name, surname, ",", age, "лет, вес", weight, "- друг, все неплохо")