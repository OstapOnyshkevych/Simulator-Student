"<----------------------------- Simulator Student ------------------------------>"
import  random
print("<----------------------------- Simulator Student ------------------------------>")
class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1000   #гроші
        self.health = 100   #здоров'я
        self.alive = True
    #study
    def study(self):
        print("Time to study!")
        self.progress += 0.15
        self.gladness -= 3
    def sleep(self):
        print("I want to sleep")
        self.gladness += 1
    def rest(self):
        print("I want to rest")
        self.gladness += 3
        self.progress -= 0.1
        self.money -= 20
        self.health += 3
    def work(self):                 #робота
        print("I should work")
        self.gladness -= 0.3
        self.progress -= 0.003
        self.money += 7
    def sick(self):                   #хворий
        print("I`m sick")
        self.gladness -= 0.02
        self.progress -= 0.003
        self.money -= 10
        self.health -= 3
    def medicine(self):               #лікування
        print("I must medicine")
        self.gladness += 5
        self.progress -= 0.0005
        self.money -= 3
        self.health += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out!")
            self.alive = False
        elif self.gladness < 0:
            print("Depresion!")
            self.alive = False
        elif self.progress >= 5:
            print("Pass exam!")
            self.alive = False
        elif self.money <= 0:           #перевірка грошей
            print("I`m loser")
            self.alive = False
        elif self.health <= 10:       #перевірка здоров'я
            print("I can die")
            self.alive = False

    def end_of_day(self):
        print(f"gladness: {round(self.gladness)}\nprogress: {round(self.progress,2)}\nMoney: {self.money}\nHealth: {self.health}")

    def live(self,day):
        day = "Day " + str(day) + "name: " + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,5)
        if live_cube == 1:
            self.study()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.rest()
        elif live_cube == 4:       #треба попрацювати
            self.work()
        elif live_cube == 5:         #хворіємо
            self.sick()
        self.must()
        self.end_of_day()
        self.is_alive()

    def must(self):
        if self.money <= 50:            #якщо бракує грошей,треба попрацювати
            self.work()
        if self.progress <= -0.1:       #якщо прогрес малий,треба повчитися
            self.study()
        if self.health <= 20:           #якщо здоров'я мале,треба полікуватися
            self.medicine()

student = Student("John")
for day in range(366):
    if student.alive == False:
        break
    student.live(day)