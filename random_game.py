from random import randint
from time import sleep
import colorama
from colorama import Fore, Style
from tkinter import *
from tkinter import ttk 

delay = 1

class User:
    # конструктор
    def __init__(self, name):
        self.name = name
    power = 10
    health = 30
    armor =2

user1 = User(name="Саша")
user2 = User(name="Миша")

user1.power = randint(15, 40)
user2.power = randint(15, 40)
user1.health = randint(40, 100)
user2.health = randint(40, 100)
user1.armor = randint(4, 8)
user2.armor = randint(4, 8)

def user1_hit():
    power_hit = randint(1, user1.power)
    label5["text"] = f"{user1.name} ударил с силой {power_hit}"
    if power_hit <= user2.armor:
        label_u2_ar["text"] = f"{user2.name} отразил удар благодатя своей броне"
        power_hit = user2.armor
    else:
        label_u2_ar["text"] = f"{user2.name} смягчил удар благодаря своей броне"
    user2.health = user2.health - (power_hit - user2.armor)
    label6["text"] = f"У бойца {user2.name} осталось жизней = {user2.health}"

def user2_hit():
    power_hit = randint(1, user2.power)
    label7["text"] = f"{user2.name} ударил с силой {power_hit}"
    if power_hit <= user1.armor:
        label_u1_ar["text"] = f"{user1.name} отразил удар благодаря своей броне"
        power_hit = user1.armor
    else:
        label_u1_ar["text"] = f"{user1.name} смягчил удар благодаря своей броне"
    user1.health = user1.health - (power_hit - user1.armor)
    label8["text"] = f"У бойца {user1.name} осталось жизней {user2.health}"

def users_hit():
    user1_hit()
    if user2.health <= 0:
        user2.health = 0
        label_win["text"] = f"Боец {user1.name} победил!"
        btn["state"] = "disable"
        label5.pack_forget()
        label6.pack_forget()
        label7.pack_forget()
        label8.pack_forget()
        label_u1_ar.pack_forget()
        label_u2_ar.pack_forget()
    else:
        label6["text"] = f"У бойца {user2.name} осталось жизней = {user2.health}"
    user2_hit()
    if user1.health <= 0:
        user2.health = 0
        label_win["text"] = f"Боец {user2.name} победил!"
        btn["state"] = "disable"
        label5.pack_forget()
        label6.pack_forget()
        label7.pack_forget()
        label8.pack_forget()
        label_u1_ar.pack_forget()
        label_u2_ar.pack_forget()
    else:
        label8["text"] = f"У бойца {user1.name} осталось жизней = {user1.health}"

# Добавляем графику
root = Tk()
root.title("Game: Random Fight")
root.geometry("400x400") 
label1 = Label(text=f"Первого бойца зовут {user1.name}")
label2 = Label(text=f"Его характерискики: Сила = {user1.power}, Жизни = {user1.health}, Броня = {user1.armor}")
label3 = Label(text=f"Второго бойца зовут {user2.name}")
label4 = Label(text=f"Его характерискики: Сила = {user2.power}, Жизни = {user2.health}, Броня = {user2.armor}")
label1.pack()
label2.pack()
label3.pack()
label4.pack()

btn = ttk.Button(text="В бой", command=users_hit)
btn.pack()

label5 = Label()
label6 = Label()
label7 = Label()
label8 = Label()
label_u1_ar = Label()
label_u2_ar = Label()
label_win = Label()
label5.pack(anchor=W) # user1 power_hit
label_u2_ar.pack(anchor=E) # user2 ar
label6.pack(anchor=E) # user2 health
label7.pack(anchor=W) # user2 power_hit
label_u1_ar.pack(anchor=E) # user1 ar
label8.pack(anchor=E) # user1 health
label_win.pack()

root.mainloop()
