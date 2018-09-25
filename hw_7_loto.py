import random

class Ticket:
    def _generate_ticket_number(self, list_ticket):
        list_str = []
        while len(list_str) < 5:
            number = random.randint(1, 90)
            if number not in list_ticket:
                list_ticket.append(number)
                list_str.append(number)
        list_str = list_str + list(" " * 4)
        random.shuffle(list_str)
        list_str = self._filter_ticket_number(list_str)
        return list_str
    def _filter_ticket_number(self, list_str):
        list_temp = []
        for number in list_str:
            if number != " ":
                list_temp.append(number)
        list_temp = sorted(list_temp)
        ii = 0
        for i, number in enumerate(list_str):
            if number != " ":
                list_str[i] = list_temp[ii]
                ii += 1
        return list_str
    def generate_ticket(self, player_name):
        list_ticket = []
        list_general = []
        for _ in range(3):
            list_general.append(self._generate_ticket_number(list_ticket))
        return list_general
    def print_ticket(self, name, ticket):
        print("{}:".format(name))
        for str in ticket:
            print(str)

class Player(Ticket):
    def __init__(self, player_name):
        Ticket.__init__(self)
        self.player_name = player_name
        self.ticket = self.generate_ticket(self.player_name)
    def cross_out(self, number):
        for string in self.ticket:
            for i, elem in enumerate(string):
                if elem == number:
                    string[i] = "-"

class Computer(Ticket):
    def __init__(self):
        Ticket.__init__(self)
        self.computer_name = "Компьютер"
        self.ticket = self.generate_ticket(self.computer_name)
    def cross_out(self, number):
        if number in prepare_list(self.ticket):
            for string in self.ticket:
                for i, elem in enumerate(string):
                    if elem == number:
                        string[i] = "-"

def generator_random(list_number): # зачем тут использовать генератор?
    while True:
        number = random.randint(1, 90)
        if number not in list_number:
            return number

def prepare_list(list):
    general_list = []
    for str in list:
        for element in str:
            general_list.append(element)
    return general_list

def play():
    player = Player("Маша")
    computer = Computer()
    list_number = []
    quantity = 90
    while quantity > 0:
        number = generator_random(list_number)
        list_number.append(number)
        quantity -= 1
        print("Новый бочонок: {}(осталось: {})".format(number, quantity))
        player.print_ticket(player.player_name, player.ticket)
        computer.print_ticket(computer.computer_name, computer.ticket)
        answer = input("Зачеркнуть цифру? (y/n)")
        if answer == "y" and number not in prepare_list(player.ticket):
            print("Игрок: {} проиграл, числа {} нет на карточке".format(player.player_name, number))
            break
        elif answer == "n" and number in prepare_list(player.ticket):
            print("Игрок: {} проиграл, число {} есть на карточке".format(player.player_name, number))
            break
        elif number in prepare_list(player.ticket):
            player.cross_out(number)
        computer.cross_out(number)
        if quantity <= 75:
            if len(set(prepare_list(player.ticket))) == 2:
                print("Победил игрок: {}".format(player.player_name))
                break
            elif len(set(prepare_list(computer.ticket))) == 2:
                print("Победил игрок: {}".format(computer.computer_name))
                break

play()