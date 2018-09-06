# easy 1
fruits = ["яблоко", "банан", "киви", "арбуз"]
n = 1
for fruit in fruits:
    print("{}. {:>10}".format(n, fruit))
    n = n + 1

#easy 2
fruits1 = ["яблоко", "банан", "киви", "арбуз"]
fruits2 = ["киви", "груша", "инжир", "лимон", "яблоко"]
for fruit2 in fruits2:
    if fruit2 in fruits1:
        fruits1.remove(fruit2)
print(fruits1)
print(fruits2)

#easy 3
list1 = [1, 2, 3, 8, 76, 80, 33]
list2 = []
for i in list1:
    if i%2 == 0:
        list2.append(i/4)
    else:
        list2.append(i*2)
print(list1)
print(list2)