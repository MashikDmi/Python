# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player_name = input("Введите имя первого игрока:")
enemy_name = input("Введите имя второго игрока:")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Наверное, я не правильно поняла задание,
# но мне кажется лучше использовать один словарь для хранения информации по игрокам, чем делать два,
# ведь количество игроков может быть больше и зачем плодить словари? Или я не права?
#game_dict = {"name": [player_name, enemy_name], "health": [100, 120], "damage": [50, 35]}


#def attack(person1, person2):
#    if person1 and person2 in game_dict.get("name"):
#        for k, v in game_dict.items():
#            for i, item in enumerate(v):
#                if item == person1:
#                    person1_index = i
#                elif item == person2:
#                    person2_index = i
#        person1_health = game_dict.get("health")[person1_index] - game_dict.get("damage")[person2_index]
#        person2_health = game_dict.get("health")[person2_index] - game_dict.get("damage")[person1_index]
#        for k, v in game_dict.items():
#            if k == "health":
#                v[person1_index] = person1_health
#                v[person2_index] = person2_health
#                return(game_dict)

#print(attack(player_name, enemy_name))

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

#game_dict = {"name": [player_name, enemy_name], "health": [100, 120], "damage": [50, 45], "armor": [1.2, 1.3]}
#for i in range(2):
#    for k, v in game_dict.items():
#        if k == "name":
#            my_file = open(str(v[i])+".txt", "w")
#        my_file.write("{} - {}\n".format(k, v[i]))
#        if k == "armor":
#            my_file.close()

def read_file(file_list):
    flag = True
    for file in file_list:
        with open(file) as my_file:
            list = [row.strip().split(" - ") for row in my_file]
            if flag == True:
                list_dict = dict(list)
                flag = False
            else:
                i = 0
                for k in list_dict.keys():
                    list_dict[k] = [list_dict[k], list[i][1]]
                    i = i + 1
    return(list_dict)

game_dict = read_file(["pl1.txt", "pl2.txt"])
print(game_dict)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Не совсем понимаю, зачем по заданию нужно разбивать атаку с бронью на две функции?
# Разве не логичнее, чтобы это все делалось в одной функции?
def attack_damage(person1, person2):
    if person1 and person2 in game_dict.get("name"):
        for k, v in game_dict.items():
            for i, item in enumerate(v):
                if item == person1:
                    person1_index = i
                elif item == person2:
                    person2_index = i
        person1_health = float(game_dict.get("health")[person1_index]) \
                         - float(game_dict.get("damage")[person2_index])/float(game_dict.get("armor")[person1_index])
        person2_health = float(game_dict.get("health")[person2_index]) \
                         - float(game_dict.get("damage")[person1_index])/float(game_dict.get("armor")[person2_index])
        for k, v in game_dict.items():
            if k == "health":
                v[person1_index] = person1_health
                v[person2_index] = person2_health
                return(game_dict)

def quantity_health(person):
    if person in game_dict.get("name"):
        for k, v in game_dict.items():
            for i, item in enumerate(v):
                if item == person:
                    person_index = i
        return(game_dict.get("health")[person_index])

while True:
    attack_damage(player_name, enemy_name)
    player_health = quantity_health(player_name)
    enemy_health = quantity_health(enemy_name)
    if player_health <= 0 and enemy_health <= 0:
        print("Оба игрока проиграли!")
        break
    elif player_health <= 0:
        print("Игрок {} победил! Оставшиеся единицы здоровья: {}".format(enemy_name, int(enemy_health)))
        break
    elif enemy_health <= 0:
        print("Игрок {} победил! Оставшиеся единицы здоровья: {}".format(player_name, int(player_health)))
        break