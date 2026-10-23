import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Час повчитись:")
        self.progress += 0.15
        self.gladness -= 5

    def to_sleep(self):
        print("Студент спить")
        self.gladness += 3

    def to_chill(self):
        print("Час відпочинку")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 15

    def to_work(self):
        print("Час попрацювати:")
        self.money += 35
        self.gladness -= 3
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Успішність на нулі")
            self.alive = False
        elif self.gladness <= 0:
            print("Студент в депресії")
            self.alive = False
        elif self.money < 0:
            print("Гроші закінчилися, банкрутство!")
            self.alive = False
        elif self.progress > 5:
            print("Ура! Сесію закрито!")
            self.alive = False

    def info_day(self):
        print(f"Щастя = {self.gladness}")
        print(f"Прогрес = {self.progress}")
        print(f"Гроші = {self.money}")

    def live(self, day):
        day_str = "День " + str(day) + " життя " + self.name
        print(day_str)
        print("=============================")

        if self.progress < -0.1:
            print("Проблеми з навчанням, треба вчитися!")
            self.to_study()
        elif self.money < 20:
            print("Брак коштів, треба йти на роботу!")
            self.to_work()
        elif self.gladness < 20:
            print("Час відпочити!")
            self.to_chill()
        else:
            vibirka = random.randint(1, 4)
            if vibirka == 1:
                self.to_study()
            elif vibirka == 2:
                self.to_sleep()
            elif vibirka == 3:
                self.to_chill()
            elif vibirka == 4:
                self.to_work()

        self.info_day()
        self.is_alive()

oleksandr = Student(name="Oleksandr")
for day in range(1, 366):
    if not oleksandr.alive:
        break
    oleksandr.live(day)