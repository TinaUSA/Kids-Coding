from turtle import *
from random import randint

#setup the race track
win = Screen()
win.bgcolor("linen")
t = Turtle()
t.speed(10)
t.penup()
t.goto(-260,200)
t.hideturtle()
for step in range(19):
	t.write(step)
	t.right(90)
	t.forward(10)
	t.pendown()
	t.forward(400)
	t.penup()
	t.backward(410)
	t.left(90)
	t.forward(30)

#create turtle to race
tom = Turtle()
tom.color('red')
tom.shape('turtle')
tom.penup()
tom.goto(-280,120)
tom.pendown()

jerry = Turtle()
jerry.color('green')
jerry.shape('turtle')
jerry.penup()
jerry.goto(-280,20)
jerry.pendown()

spike = Turtle()
spike.color('blue')
spike.shape('turtle')
spike.penup()
spike.goto(-280,-80)
spike.pendown()

players = [tom, jerry, spike]

for step in range(200):
	tom.forward(randint(1,8))
	jerry.forward(randint(1,8))
	spike.forward(randint(1,8))
	endline = 280
	if((tom.xcor() >= endline) or (jerry.xcor() >= endline) or (spike.xcor() >= endline)):
		break
			
done()