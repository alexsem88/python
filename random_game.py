from random import randint
from time import sleep

delay = 7

class User:
    # конструктор
    def __init__(self, name, power, health, armor):
        self.name = name
        self.power = power
        self.health = health
        self.armor = armor

user1 = User(name="Миша", power=20, health=50, armor=8)
user2 = User(name="Саша", power=50, health=50, armor=8)

print("Знакомьтесь с участниками турнира!")
print("Первого бойца зовут", user1.name)
print("Его характеристики:", "Сила =", user1.power, "Жизни =", user1.health, "Броня = ", user1.armor)
print("Второго бойца зовут", user2.name)
print("Его характеристики:", "Сила =", user2.power, "Жизни =", user2.health, "Броня = ", user2.armor)
print("Начинаем битву!!! \n")

def user1_hit():
    power_hit = randint(10, user1.power)
    print(user1.name, "ударил с силой =", power_hit)
    if power_hit <= user2.armor:
        print(user2.name, "отразил удар благодатя своей броне")
        power_hit = user2.armor
    user2.health = user2.health - (power_hit - user2.armor)

def user2_hit():
    power_hit = randint(10, user2.power)
    print(user2.name, "ударил с силой =", power_hit)
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
