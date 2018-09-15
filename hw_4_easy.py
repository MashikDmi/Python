# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
numbers = [1, 2, 4, 0]
print([number**2 for number in numbers])

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ["яблоко", "лимон", "киви", "банан"]
fruits2 = ["киви", "груша", "хурма", "апельсин", "банан"]
print([fruit for fruit in fruits1 if fruit in fruits2])

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
numbers = [3, 12, -3, -5, 33, 11, 15]
print([number for number in numbers if number%3 == 0 and number >= 0 and number%4 != 0])