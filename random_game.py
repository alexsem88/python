from random import randint
from time import sleep
import colorama
from colorama import Fore, Style

delay = 5

class User:
    # конструктор
    def __init__(self, name):
        self.name = name
    power = 10
    health = 30
    armor =2

user1 = User(name="Миша")
user2 = User(name="Саша")

user1.power = randint(5, 30)
user2.power = randint(5, 30)
user1.health = randint(40, 100)
user2.health = randint(40, 100)
user1.armor = randint(4, 20)
user2.armor = randint(4, 20)

print("Знакомьтесь с участниками турнира!")
print("Первого бойца зовут", user1.name)
print("Его характеристики:", "Сила =", user1.power, "Жизни =", user1.health, "Броня = ", user1.armor)
print("Второго бойца зовут", user2.name)
print("Его характеристики:", "Сила =", user2.power, "Жизни =", user2.health, "Броня = ", user2.armor)
print("Начинаем битву!!! \n")

def user1_hit():
    power_hit = randint(1, user1.power)
    print(Fore.RED + user1.name, "ударил с силой =", power_hit, Style.RESET_ALL)
    if power_hit <= user2.armor:
        print(user2.name, "отразил удар благодатя своей броне")
        power_hit = user2.armor
    user2.health = user2.health - (power_hit - user2.armor)

def user2_hit():
    power_hit = randint(1, user2.power)
    print(Fore.BLUE + user2.name, "ударил с силой =", power_hit, Style.RESET_ALL)
    if power_hit <= user1.armor:
        print(user1.name, "отразил удар благодатя своей броне")
        power_hit = user1.armor
    user1.health = user1.health - (power_hit - user1.armor)

# Основной игровой цикл
while user1.health >= 0 and user2.health >= 0:

    user1_hit()
    if user2.health <= 0:
        break
    print("У бойца", user2.name, "осталось жизней = ", user2.health, "\n")
    sleep(delay)

    user2_hit()
    if user1.health <= 0:
        break
    print("У бойца", user1.name, "осталось жизней = ", user1.health, "\n")
    sleep(delay)

if user1.health <= 0:
    print(user2.name, "победил!!!")
elif user2.health <=0:
    print(user1.name, "победил!!!")
