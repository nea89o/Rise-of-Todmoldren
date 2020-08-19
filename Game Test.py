import os
import random
import time
import turtle

os.chdir('riseoftodmoldren/res')  # Moved assets
window = turtle.Screen()
window.setup(1280, 720)
window.bgcolor("black")
window.title("Rise of Todmoldren [BETA]")

window.register_shape("forest1.gif")
window.register_shape("forest2.gif")
window.register_shape("forest3.gif")
window.register_shape("forest4.gif")
window.register_shape("forest5.gif")
window.register_shape("forest6.gif")
window.register_shape("forest7.gif")
window.register_shape("forest8.gif")

window.register_shape("sword.gif")
window.register_shape("sword2.gif")

window.register_shape("d_sword.gif")
window.register_shape("d_sword2.gif")

window.register_shape("heal_potion_icon.gif")
window.register_shape("towel_icon.gif")
window.register_shape("d_sword_icon.gif")

window.register_shape("sack.gif")

window.register_shape("chest1.gif")
window.register_shape("chest2.gif")

window.register_shape("castle1.gif")

window.register_shape("cave_enternace.gif")
window.register_shape("cave1.gif")
window.register_shape("cave2.gif")
window.register_shape("cave3.gif")
window.register_shape("cave_exit.gif")

window.register_shape("menu1.gif")
window.register_shape("menu2.gif")

window.bgpic("menu2.gif")

hp = 100

xp = 0

level = 1

levelAttack = 0

hpE = 10
hpE2 = 15

hPotion = 3

money = 0

alive = False

characters = True

towel = False
d_Sword = False

Market = False

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

loader = turtle.Turtle()
loader.hideturtle()
loader.penup()

player = turtle.Turtle()
player.hideturtle()
player.speed(10)
player.penup()
player.hideturtle()
player.speed(10)

Pick = turtle.Turtle()
Pick.hideturtle()
Pick.penup()
Pick.speed(10)
Pick.goto(0, 0)

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

def start():
    player.forward(10)

turtle.listen()
turtle.onkey(start, "")

while characters == True:

    loader.forward(1)
    if abs(player.pos() - Pick.pos()) > 5:
        characters = False
    else:
        time.sleep(0.5)


alive = True

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

window.bgpic("forest1.gif")

up = True
right = True
left = True
cave = False
hrad = False

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

hpU = turtle.Turtle()
hpU.speed(10)
hpU.hideturtle()
hpU.pu()
hpU.turtlesize
hpU.color("red")
hpU.goto(-625, -350)
hpU.write(hp, font=("Impact", 60, "normal"))

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

                                                #GUI


sword = turtle.Turtle()
sword.speed(10)
sword.penup()
sword.hideturtle()
sword.shape("sword.gif")
sword.goto(500, -225)
sword.showturtle()

healPotion = turtle.Turtle()
healPotion.hideturtle()
healPotion.speed(10)
healPotion.penup()
healPotion.shape("heal_potion_icon.gif")
healPotion.color("red")
healPotion.turtlesize(3)
healPotion.goto(0, -275)
healPotion.showturtle()

healPotionNumber = turtle.Turtle()
healPotionNumber.speed(10)
healPotionNumber.penup()
healPotionNumber.hideturtle()
healPotionNumber.color("white")
healPotionNumber.goto(-10, -350)
healPotionNumber.write(hPotion, font=("Impact", 25, "normal"))



coin = turtle.Turtle()
coin.speed(10)
coin.penup()
coin.hideturtle()
coin.shape("sack.gif")
coin.turtlesize(1)
coin.goto(-615, -240)
coin.showturtle()

coinNumber = turtle.Turtle()
coinNumber.speed(10)
coinNumber.penup()
coinNumber.hideturtle()
coinNumber.color("yellow")
coinNumber.goto(-590, -260)
coinNumber.write(money, font=("Impact", 25, "normal"))

xpNumber = turtle.Turtle()
xpNumber.speed(10)
xpNumber.penup()
xpNumber.hideturtle()
xpNumber.color("green")
xpNumber.goto(-500, -260)
xpNumber.write(xp, font=("Impact", 25, "normal"))

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

enemy = turtle.Turtle()
enemy.speed(10)
enemy.shape("circle")
enemy.color("green")
enemy.hideturtle()
enemy.penup()
enemy.turtlesize(6)

enemyD = turtle.Turtle()
enemyD.speed(10)
enemyD.hideturtle()
enemyD.penup()

enemyHP = turtle.Turtle()
enemyHP.speed(10)
enemyHP.hideturtle()
enemyHP.color("red")
enemyHP.penup()
enemyHP.goto(0, -100)
enemyHP.clear()
enemyHP.write(hpE, font=("Impact", 25, "normal"))
enemyHP.clear()

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

chest = turtle.Turtle()
chest.speed(10)
chest.hideturtle()
chest.shape("chest1.gif")
chest.penup()

chestCheck = turtle.Turtle()
chestCheck.speed(10)
chestCheck.hideturtle()
chestCheck.penup()

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

sword_i = turtle.Turtle()
sword_i.penup()
sword_i.hideturtle()
sword_i.shape("d_sword_icon.gif")
sword_i.goto(0, 75)

towel_i = turtle.Turtle()
towel_i.penup()
towel_i.hideturtle()
towel_i.shape("towel_icon.gif")
towel_i.hideturtle()
towel_i.goto(150, 75)

potion_i = turtle.Turtle()
potion_i.penup()
potion_i.hideturtle()
potion_i.shape("heal_potion_icon.gif")
potion_i.goto(-150, 75)

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################



#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

#up = turtle.Turtle()
#up.color("white")
#up.hideturtle()
#up.penup()
#up.setheading(90)
#up.shape("square")
#up.goto(0, 800)
#up.turtlesize(50)

#right = turtle.Turtle()
#right.color("white")
#right.hideturtle()
#right.penup()
#right.setheading(90)
#right.shape("square")
#right.goto(800, 0)
#right.turtlesize(25)

#left = turtle.Turtle()
#left.color("white")
#left.hideturtle()
#left.penup()
#left.setheading(90)
#left.shape("square")
#left.goto(-800, 0)
#left.turtlesize(25)

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

check = turtle.Turtle()
check.hideturtle()
check.penup()
check.goto(0, 0)

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

def dev_cords(x, y):
    player.goto(x, y)
    print(player.pos())

def action(x, y):
    player.goto(x, y)

def attack(x, y):
    player.goto(x, y)
    if d_Sword == True:
        sword.shape("d_sword2.gif")
    if d_Sword == False:
        sword.shape("sword2.gif")
    player.goto(0, 0)
    enemyD.forward(10)

def open_chest(x, y):
    player.goto(x, y)
    player.goto(0, 0)
    chest.shape("chest2.gif")
    chestCheck.forward(10)


#########################################################################################################################



#########################################################################################################################

while alive == True:
    if xp >= 50 and level == 1:
        xp = xp - 50

        level = 2

        xpNumber.clear()
        xpNumber.write("Level Up!", font=("Impact", 25, "normal"))
        time.sleep(2)
        xpNumber.clear()
        xpNumber.write(xp, font=("Impact", 25, "normal"))

        levelAttack = levelAttack + 1

    if xp >= 100 and level == 2:
        xp = xp - 100

        level = 3

        xpNumber.clear()
        xpNumber.write("Level Up!", font=("Impact", 25, "normal"))
        time.sleep(2)
        xpNumber.clear()
        xpNumber.write(xp, font=("Impact", 25, "normal"))

        levelAttack = levelAttack + 1

    if xp >= 150 and level == 3:
        xp = xp - 150

        level = 4

        xpNumber.clear()
        xpNumber.write("Level Up!", font=("Impact", 25, "normal"))
        time.sleep(2)
        xpNumber.clear()
        xpNumber.write(xp, font=("Impact", 25, "normal"))

        levelAttack = levelAttack + 1

    if xp >= 200 and level == 4:
        xp = xp - 200

        level = 5

        xpNumber.clear()
        xpNumber.write("Level Up!", font=("Impact", 25, "normal"))
        time.sleep(2)
        xpNumber.clear()
        xpNumber.write(xp, font=("Impact", 25, "normal"))

        levelAttack = levelAttack + 1

    if xp >= 250 and level == 5:
        xp = xp - 250

        level = 5

        xpNumber.clear()
        xpNumber.write("Level Up!", font=("Impact", 25, "normal"))
        time.sleep(2)
        xpNumber.clear()
        xpNumber.write(xp, font=("Impact", 25, "normal"))

        levelAttack = levelAttack + 1

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

    if Market == True:
        if d_Sword == False:
            sword_i.showturtle()
        if towel == False:
            towel_i.showturtle()

        potion_i.showturtle()

        if abs(player.pos() - sword_i.pos()) < 45 and money >= 15 and sword_i.isvisible():
            money = money - 15
            coinNumber.clear()
            coinNumber.write(money, font=("Impact", 25, "normal"))
            d_Sword = True
            sword.shape("d_sword.gif")
            sword_i.hideturtle()

        if abs(player.pos() - towel_i.pos()) < 45 and money >= 10 and towel_i.isvisible():
            money = money - 10
            coinNumber.clear()
            coinNumber.write(money, font=("Impact", 25, "normal"))
            towel = True
            towel_i.hideturtle()

        if abs(player.pos() - potion_i.pos()) < 45 and money >= 5 and potion_i.isvisible():
            money = money - 5
            coinNumber.clear()
            coinNumber.write(money, font=("Impact", 25, "normal"))
            hPotion = hPotion + 1
            healPotionNumber.clear()
            healPotionNumber.write(hPotion, font=("Impact", 25, "normal"))

    if Market == False:
        sword_i.hideturtle()
        potion_i.hideturtle()
        towel_i.hideturtle()

    if enemy.isvisible():
        time.sleep(0.5)
        window.onclick(attack)

    if chest.isvisible():
        window.onclick(open_chest)


    if abs(chestCheck.pos() - check.pos()) > 5:
        chestCheck.goto(0, 0)
        hPotion = hPotion + 1
        healPotionNumber.clear()
        healPotionNumber.write(hPotion, font=("Impact", 25, "normal"))
        time.sleep(1.5)
        chest.shape("chest1.gif")
        time.sleep(0.5)
        chest.hideturtle()


    if abs(enemyD.pos() - check.pos()) > 5 and d_Sword == False:
        hpE = hpE - (random.randint(1, 10))
        hpE = hpE - levelAttack
        enemyHP.clear()
        enemyHP.write(hpE, font=("Impact", 25, "normal"))
        if d_Sword == False:
            sword.shape("sword.gif")
        print(hpE)
        hp = hp - (random.randint(1, 15))
        hpU.clear()
        hpU.write(hp, font=("Impact", 60, "normal"))
        enemyD.goto(0, 0)
        if hpE <= 0:
            enemy.hideturtle()
            enemyHP.clear()
            money = money + (random.randint(1, 8))
            coinNumber.clear()
            coinNumber.write(money, font=("Impact", 25, "normal"))
            xp = xp + (random.randint(1, 15))
            xpNumber.clear()
            xpNumber.write(xp, font=("Impact", 25, "normal"))
            hPotion = hPotion + 1
            healPotionNumber.clear()
            healPotionNumber.write(hPotion, font=("Impact", 25, "normal"))
            hpE = 10

    if abs(enemyD.pos() - check.pos()) > 5 and d_Sword == True:
        hpE = hpE - (random.randint(5, 15))
        enemyHP.clear()
        enemyHP.write(hpE, font=("Impact", 25, "normal"))
        sword.shape("d_sword.gif")
        print(hpE)
        hp = hp - (random.randint(1, 15))
        hpU.clear()
        hpU.write(hp, font=("Impact", 60, "normal"))
        enemyD.goto(0, 0)
        if hpE <= 0:
            enemy.hideturtle()
            enemyHP.clear()
            money = money + (random.randint(1, 8))
            coinNumber.clear()
            coinNumber.write(money, font=("Impact", 25, "normal"))
            hPotion = hPotion + 1
            healPotionNumber.clear()
            healPotionNumber.write(hPotion, font=("Impact", 25, "normal"))
            hpE = 10



    window.update()
    #window.onclick(dev_cords)
    window.onclick(action)

    if abs(player.pos() - healPotion.pos()) < 45 and hPotion > 0 and Market == False:
        player.goto(0, 0)
        hPotion = hPotion - 1
        healPotionNumber.clear()
        healPotionNumber.write(hPotion, font=("Impact", 25, "normal"))
        hp = hp + 10
        if hp > 100:
            hp = 100
        hpU.clear()
        hpU.write(hp, font=("Impact", 60, "normal"))

    if player.ycor() >= 300 and player.xcor() >= -500 and player.xcor() <= 500 and up == True and cave == False and hrad == False:
        co = random.randint(1, 10)
        if co == 1:
            window.bgpic("forest1.gif")
            up = True
            right = True
            left = True

        if co == 2:
            window.bgpic("forest2.gif")
            up = True
            right = True
            left = True

        if co == 3:
            window.bgpic("forest3.gif")
            up = True
            right = True
            left = True

        if co == 4:
            window.bgpic("forest4.gif")
            up = True
            right = True
            left = False

        if co == 5:
            window.bgpic("forest5.gif")
            up = False
            right = True
            left = True

        if co == 6:
            window.bgpic("forest6.gif")
            up = True
            right = False
            left = True

        if co == 7:
            window.bgpic("forest7.gif")
            up = False
            right = False
            left = True

        if co == 8:
            window.bgpic("forest8.gif")
            up = False
            right = True
            left = False

        if co == 9:
            window.bgpic("castle1.gif")
            up = True
            right = False
            left = False
            hrad = True
            Market = True

        if co == 10:
            window.bgpic("cave_enternace.gif")
            up = True
            right = False
            left = False
            cave = True
            player.goto(0, 0)

        Wchest = random.randint(1, 6)
        yeno = random.randint(1, 6)

        if Wchest == yeno:
            chest.showturtle()

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False





        player.goto(0, 0)

    if player.xcor() >= 550 and player.ycor() >= -250 and player.ycor() <= 250 and right == True and cave == False and hrad == False:
        co = random.randint(1, 10)
        if co == 1:
            window.bgpic("forest1.gif")
            up = True
            right = True
            left = True

        if co == 2:
            window.bgpic("forest2.gif")
            up = True
            right = True
            left = True

        if co == 3:
            window.bgpic("forest3.gif")
            up = True
            right = True
            left = True

        if co == 4:
            window.bgpic("forest4.gif")
            up = True
            right = True
            left = False

        if co == 5:
            window.bgpic("forest5.gif")
            up = False
            right = True
            left = True

        if co == 6:
            window.bgpic("forest6.gif")
            up = True
            right = False
            left = True

        if co == 7:
            window.bgpic("forest7.gif")
            up = False
            right = False
            left = True

        if co == 8:
            window.bgpic("forest8.gif")
            up = False
            right = True
            left = False

        if co == 9:
            window.bgpic("castle1.gif")
            up = True
            right = False
            left = False
            hrad = True
            Market = True



        if co == 10:
            window.bgpic("cave_enternace.gif")
            up = True
            right = False
            left = False
            cave = True
            player.goto(0, 0)

        Wchest = random.randint(1, 6)
        yeno = random.randint(1, 6)

        if Wchest == yeno:
            chest.showturtle()

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False

        player.goto(0, 0)

    if player.xcor() <= -550 and player.ycor() >= -250 and player.ycor() <= 250 and left == True and cave == False and hrad == False:
        co = random.randint(1, 10)
        if co == 1:
            window.bgpic("forest1.gif")
            up = True
            right = True
            left = True

        if co == 2:
            window.bgpic("forest2.gif")
            up = True
            right = True
            left = True

        if co == 3:
            window.bgpic("forest3.gif")
            up = True
            right = True
            left = True

        if co == 4:
            window.bgpic("forest4.gif")
            up = True
            right = True
            left = False

        if co == 5:
            window.bgpic("forest5.gif")
            up = False
            right = True
            left = True

        if co == 6:
            window.bgpic("forest6.gif")
            up = True
            right = False
            left = True

        if co == 7:
            window.bgpic("forest7.gif")
            up = False
            right = False
            left = True

        if co == 8:
            window.bgpic("forest8.gif")
            up = False
            right = True
            left = False

        if co == 9:
            window.bgpic("castle1.gif")
            up = True
            right = False
            left = False
            hrad = True
            Market = True


        if co == 10:
            window.bgpic("cave_enternace.gif")
            up = True
            right = False
            left = False
            cave = True
            player.goto(0, 0)

        Wchest = random.randint(1, 6)
        yeno = random.randint(1, 6)

        if Wchest == yeno:
            chest.showturtle()

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False

        player.goto(0, 0)

    if player.ycor() >= 300 and player.xcor() >= -500 and player.xcor() <= 500 and up == True and cave == True:
        co = random.randint(1, 4)
        c_exit = random.randint(1, 4)
        if co == 1:
            window.bgpic("cave1.gif")
            up = True
            right = False
            left = True
            cave = True
        if co == 2:
            window.bgpic("cave2.gif")
            up = True
            right = True
            left = False
            cave = True
        if co == 3:
            window.bgpic("cave3.gif")
            up = True
            right = False
            left = False
            cave = True
        if co == c_exit:
            window.bgpic("cave_exit.gif")
            up = True
            right = False
            left = False
            cave = False

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False

        player.goto(0, 0)

    if player.xcor() >= 550 and player.ycor() >= -250 and player.ycor() <= 250 and right == True and cave == True:
        co = random.randint(1, 4)
        c_exit = random.randint(1, 4)
        if co == 1:
            window.bgpic("cave1.gif")
            up = True
            right = False
            left = True
            cave = True
        if co == 2:
            window.bgpic("cave2.gif")
            up = True
            right = True
            left = False
            cave = True
        if co == 3:
            window.bgpic("cave3.gif")
            up = True
            right = False
            left = False
            cave = True
        if co == c_exit:
            window.bgpic("cave_exit.gif")
            up = True
            right = False
            left = False
            cave = False

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False

        player.goto(0, 0)

    if player.xcor() <= -550 and player.ycor() >= -250 and player.ycor() <= 250 and left == True and cave == True:
        co = random.randint(1, 4)
        c_exit = random.randint(1, 4)
        if co == 1:
            window.bgpic("cave1.gif")
            up = True
            right = False
            left = True
            cave = True
        if co == 2:
            window.bgpic("cave2.gif")
            up = True
            right = True
            left = False
            cave = True
        if co == 3:
            window.bgpic("cave3.gif")
            up = True
            right = False
            left = False
            cave = True
        if co == c_exit:
            window.bgpic("cave_exit.gif")
            up = True
            right = False
            left = False
            cave = False

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False

        player.goto(0, 0)

    if player.ycor() >= 300 and player.xcor() >= -500 and player.xcor() <= 500 and up == True and cave == False and hrad == True:
        Market = False
        co = random.randint(1, 10)
        if co == 1:
            window.bgpic("forest1.gif")
            up = True
            right = True
            left = True
            hrad = False

        if co == 2:
            window.bgpic("forest2.gif")
            up = True
            right = True
            left = True
            hrad = False

        if co == 3:
            window.bgpic("forest3.gif")
            up = True
            right = True
            left = True
            hrad = False

        if co == 4:
            window.bgpic("forest4.gif")
            up = True
            right = True
            left = False
            hrad = False

        if co == 5:
            window.bgpic("forest5.gif")
            up = False
            right = True
            left = True
            hrad = False

        if co == 6:
            window.bgpic("forest6.gif")
            up = True
            right = False
            left = True
            hrad = False

        if co == 7:
            window.bgpic("forest7.gif")
            up = False
            right = False
            left = True
            hrad = False

        if co == 8:
            window.bgpic("forest8.gif")
            up = False
            right = True
            left = False
            hrad = False

        if co == 9:
            window.bgpic("castle1.gif")
            up = True
            right = False
            left = False
            hrad = True
            Market = True


        if co == 10:
            window.bgpic("cave_enternace.gif")
            up = True
            right = False
            left = False
            hrad = False
            cave = True
            player.goto(0, 0)

        Wchest = random.randint(1, 6)
        yeno = random.randint(1, 6)

        if Wchest == yeno:
            chest.showturtle()

        underAttack = random.randint(1, 3)
        yn = random.randint(1, 3)
        if underAttack == yn and hrad == False:
            enemy.showturtle()
            if towel == True:
                hp = hp - (random.randint(1, 8))
                print("mas ochranu ručníku")
            else:
                hp = hp - (random.randint(1, 15))

            hpU.clear()
            hpU.write(hp, font=("Impact", 60, "normal"))
            print("Nepřítel!")
            if hp <= 0:
                alive = False

    #if abs(mobE.pos() - kontrola.pos()) > 5:
     #   hp = hp - (random.randint(1, 10))
      #  mobE.goto(0, 0)

    #if abs(hpH.pos() - kontrola.pos()) > 5:
     #   hp = hp + 10
      #  if hp > 100:
       #     hp = 100
        #hpH.goto(0, 0)