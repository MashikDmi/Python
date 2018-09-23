# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    def _calculate_damage(self, damage, armor):
        return damage // armor
    def attack(self, who_attack, who_defend):
        damage = Person._calculate_damage(self, who_attack.damage, who_defend.armor)
        who_defend.health -= damage
        print("{} нанес {} {} урона, у того осталось {} жизней.".format(who_attack.name, who_defend.name, damage, who_defend.health))

class Player(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)

class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)

def start_game():
    player = Player("Игрок", 100, 30, 1.2)
    enemy = Enemy("Враг", 100, 20, 1.3)
    last_attacker = player
    while player.health > 0 and enemy.health > 0:
        if last_attacker == player:
            enemy.attack(enemy, player)
            last_attacker = enemy
        else:
            player.attack(player, enemy)
            last_attacker = player
    if player.health > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')

start_game()