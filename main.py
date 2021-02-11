import turtle
import time
import random
t = turtle.Turtle()

t.speed(100)

t.pencolor("blue")

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

for count in range(90):
  t.forward(100)
  t.backward(100)
  t.left(4)

t.penup()
t.goto(-100,100)
t.pendown()
t.circle(100)

t.penup()
t.goto(-100,-100)
t.pendown
t.color("cyan")
t.begin_fill()
t.circle(50)
t.end_fill()

t.color("black")
t.penup()
t.goto(-200,-100)
t.write("MAX AND RALPH ARE THE BEST")

t.penup()
t.goto(200,-50)
t.pendown
t.color("cyan")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(150,-50)
t.pendown
t.color("cyan")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(5,25)
t.pendown
t.color("cyan")
t.begin_fill()
t.circle(50)
t.end_fill()

time.sleep(3)
t.clear()

t.pendown()
t.right(180)
colors = ("yellow","blue","red","cyan","green","orange")
for count in range(90):
  t.color(random.choice(colors))
  t.width(count/100+1)
  t.forward(count)
  t.left(59)


time.sleep(5)
t.clear()
t.color("orange")
t.write("AGGGGG I FELL DOWN THE HOLE!!!!")

time.sleep(2)
t.clear()
answer = input("Do you want to sart the story? (Y/N)")
if answer == 'Y':
  print("Ok; here goes (look up in 3 secs)")

  t.clear()
  time.sleep(3)
  print("Sorry, this section is in the making.")

if answer == 'N':
  print("Ok, but you will miss out.")

if not (answer == 'N' or 'Y'): 
  print("Sorry, we did not recoginse your answer. Please make sure it was N or Y and it was in capitals, then retry in the space below. (If you get a message saying 're-run', please re-run the code).")

  answer = input("Do you want to sart the story? (Y/N)")
  if answer == 'Y':
    print("Ok; here goes (look up in 3 secs)")

  if answer == 'N':
    print("oh")

  t.clear()
  time.sleep(3)

if answer == 'N':
  print("Ok, but you will miss out.")

answer = input("Do you want to play the quiz?")
if answer == 'Y':

  colours = ("red","azure","midnightblue","greenyellow","CornflowerBlue","NavyBlue","azure2")

for count in range(10):
  t.left(2)
  t.forward(60+count)
  t.left(100)
  t.pencolor(random.choice(colours))

t.clear()

for count in range(100):
  t.circle(count*5)
  t.pencolor(random.choice(colours))

time.sleep(5)
t.clear()
t.color("orange")