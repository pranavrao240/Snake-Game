import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

r = turtle.Screen()
r.title("snake")
r.bgcolor("black")
r.setup(height = 600, width = 600)
r.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("cyan")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0", align = "center", font = ("courier",24,"normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

r.listen()
r.onkeypress(go_up,'w')
r.onkeypress(go_down,'s')
r.onkeypress(go_left,'a')
r.onkeypress(go_right,'d')

while True:
    r.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segment.clear()

    if head.distance(food) < 20:

        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score:{} High Score: {}".format(score, high_score),align = "center", font = ("courier",24,"normal"))

    for index in range (len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

    time.sleep(delay)



r.mainloop()
   














