import turtle as t
import time
from random import randint, randrange
import decimal
import os

mode=input("Do you want 2 player or one player?: ")
if(mode!="one player" and mode!="two player" and mode!="2 player"):

    if(mode=="Abhijit Sudharsan"):

        print("The rules are inversed")
        mode="auto_win"

    else:

        print("Ok, one player it is")
        mode="one player"
player=0
if(mode=="one player" or mode=="auto_win"):
    players=1
else:
    players=2
screen = t.Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.tracer(0)
t.speed(0)

border = t.Turtle()
border.penup()
border.goto(-300, -300)
border.color("green")
border.pensize(5)
border.pendown()

border.forward(590)
border.left(90)
border.forward(590)
border.left(90)
border.forward(590)
border.left(90)
border.forward(590)
border.hideturtle()

score=0
score_chunck=0
passed=0
enemy_array=[]
random_array=[]
num_enemies=randint(0,5)
num_random=randint(1,90)
time_in_game=0
time_in_game2=0
game=True

pen = t.Turtle()
pen.penup()
pen.color("white")
pen.goto(0, 295)
pen.write('hello', align="center",font=("arial", 20, "normal"))
pen.hideturtle()
size=0
size2=0

if(mode=="auto_win"):
    score=10
    pen.goto(0,0)
    pen.write("you'll need this", align="center", font=("Courier", 25, "normal"))
    time.sleep(5)
    pen.goto(0,295)
    pen.clear()

def stars_make():
    for i in range(num_random):
        y=randint(-290,275)
        x=randint(-290,275)
        size2= float(decimal.Decimal(randrange(10, 30))/100)
        fillings = t.Turtle()
        fillings.showturtle()
        fillings.color("yellow")
        fillings.shape("circle")
        fillings.shapesize(size2,size2,size2)
        fillings.penup()
        fillings.speed(0)
        fillings.setposition(x, y)
        random_array.append(fillings)

stars_make()

player= t.Turtle()
player.color("sky blue")
player.shape("circle")
player.shapesize(1.25,1.25,1.25)
player.penup()
player.speed(0)
player.setposition(-100, 0)

def grow():
    global size2
    global time_in_game2
    for fillings in random_array:
        if(size2>=0.15):
            size2=0.000001
        size2=size2+0.00001
        fillings.setx(fillings.xcor()-5)
        if(time_in_game2>=5):
            for i in range(num_random):
                y=randint(-590,575)
                x=randint(-590,575)
                fillings = t.Turtle()
                fillings.showturtle()
                fillings.color("yellow")
                fillings.shape("circle")
                fillings.shapesize(size2,size2,size2)
                fillings.penup()
                fillings.speed(0)
                fillings.setposition(x, y)
                random_array.append(fillings)
                time_in_game2=0
    time_in_game2=time_in_game2+0.1
if(mode=="two player" or mode=="2 player"):

    def enemy_make(x,y):
        global size
        num_enemies=randint(0,2)
        global passed
        for i in range(num_enemies):
            size= float(decimal.Decimal(randrange(86, 200))/100)
            enemy = t.Turtle()
            enemy.showturtle()
            enemy.color("grey")
            enemy.shape("circle")
            enemy.shapesize(size,size,size)
            enemy.penup()
            enemy.speed(0)
            if(x<300):
                enemy.setposition(300,y)
            else:
                enemy.setposition(x,y)
            enemy_array.append(enemy)
        passed=0
else:

    def enemy_make2():
        global size
        num_enemies=randint(0,7)
        global passed
        for i in range(num_enemies):
            size= float(decimal.Decimal(randrange(86, 200))/100)
            y=randint(-275,280)
            enemy = t.Turtle()
            enemy.showturtle()
            enemy.color("grey")
            enemy.shape("circle")
            enemy.shapesize(size,size,size)
            enemy.penup()
            enemy.speed(0)
            enemy.setposition(300,y)
            if(abs(enemy.ycor()-enemy.ycor())<10):
                y=randint(-275,280)
                enemy.setposition(300,y)
            enemy_array.append(enemy)
        passed=0

def enemy_move():
    for enemy in enemy_array:
        speed=randint(1,7)
        x=enemy.xcor()
        x=x-speed
        enemy.setx(x)
        if(enemy.xcor()<=-295):
            enemy.hideturtle()

def score_check():
    global score
    global score_chunck
    global passed
    global size
    global game
    global mode
    for enemy in enemy_array:
        close_y=abs(player.ycor()-enemy.ycor())
        close_x=abs(player.xcor()-enemy.xcor())
        if(enemy.xcor()<=-80):
            if(close_x<size*22 and close_y<size*22 and passed==0):
                if(mode=="auto_win"):
                    score_chunck=score_chunck+3
                else:
                    game=False
                passed=1
                return score
                if(passed==1):
                    score=score+0
    if(passed==0):
        if(mode=="auto_win"):
            score=score-0.5
        else:
            score_chunck=score_chunck+1
        passed=1
        return passed
    elif(passed==1):
        score_chunck=score_chunck+0


gravity=1
move_time=25

def player_move():
    global gravity
    global move_time
    y=player.ycor()
    if(gravity==0):
        player.sety(y)
        return
    gravity=0
    move_time=25
    screen.update()
    gravity_player()

def gravity_player():
    global gravity
    global game
    global move_time
    y=player.ycor()
    if(player.ycor()>280):
        game=False
        return
    if(player.ycor()<-295):
        game=False
        return
    if(move_time<=0):
        move_time=25
        gravity=1
        return
    y=player.ycor()
    if(gravity==0):
        y=y+4.5
    elif(gravity==1):
        y=y-2
    player.sety(y)

screen.onkey(player_move, 'space')

if(mode=="two player" or mode=="2 player"):
        screen.onclick(enemy_make)
screen.listen()

while game:
    if(score_chunck>=5):
        os.system('afplay sfx_point.mp3&')
        score=score+1
        score_chunck=0

    if(mode=="one player" or mode=="auto_win"):
        if(time_in_game>=3.5):
            enemy_make2()
            time_in_game=0

    screen.update()
    enemy_move()
    time_in_game=time_in_game+0.1
    gravity_player()
    move_time=move_time-1
    if(move_time<=0):
        move_time=0

    for enemy in enemy_array:
        if(enemy.xcor()<-80 and passed==0):
            score_check()
            if(time_in_game==100):
                passed=1
                break
    if(score<0):
        game=False
    pen.clear()
    pen.write("Score: {}".format(score), align="center", font=("Courier", 15, "normal"))
    time.sleep(0.01)
    grow()

max_score=0
g=open("bird_score.txt", "r")
arr=g.readlines()
max_score=float(arr[3])
if(score>max_score):
    max_score=score
max_score=int(max_score)
z=max_score/players
x=score/players
x=str(x)
z=str(z)

with open("bird_score.txt", "w") as file:
    file.write("Your score........\n")
    file.write(x)
    file.write("\n")
    file.write("Max Score.........\n")
    file.write(z)

with open("bird_score.txt", "r") as y:
    a=y.read()

b=t.Turtle()
b.color("white")

y=open("bird_score.txt","r")
h=0
while(h<1000):
    b.write(a,align="center",font=("arial",25,"normal"))
    h=h+1
    screen.update()
