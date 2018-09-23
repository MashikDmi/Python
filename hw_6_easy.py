# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, model, max_speed, color, is_police):
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "Машина {} поехала".format(self.model)
    def stop(self):
        return "Машина {} остановилась".format(self.model)
    def turn(self, where_turn):
        if where_turn == 0:
            answer = "Машина {} повернула налево".format(self.model)
        elif where_turn == 1:
            answer = "Машина {} повернула направо".format(self.model)
        else:
            answer = "Машина {} остановилась".format(self.model)
        return answer

class TownCar(Car):
    def __init__(self, model, max_speed, color, is_police, owner, town):
        super().__init__(model, max_speed, color, is_police)
        #Car.__init__(self, model, max_speed, color, is_police)
        self.owner = owner
        self.town = town
    def function_for_town_car(self):
        pass

class SportCar(Car):
    def __init__(self, model, max_speed, color, is_police, company, racer):
        super().__init__(model, max_speed, color, is_police)
        #Car.__init__(self, model, max_speed, color, is_police)
        self.company = company
        self.racer = racer
    def function_for_sport_car(self):
        pass

class WorkCar(Car):
    def __init__(self, model, max_speed, color, is_police, company, name_driver):
        super().__init__(model, max_speed, color, is_police)
        #Car.__init__(self, model, max_speed, color, is_police)
        self.company = company
        self.name_driver = name_driver
    def function_for_work_car(self):
        pass

class PoliceCar(Car):
    def __init__(self, model, max_speed, color, is_police, police_station):
        super().__init__(model, max_speed, color, is_police)
        #Car.__init__(self, model, max_speed, color, is_police)
        self.police_station = police_station
    def function_for_police_car(self):
        pass
