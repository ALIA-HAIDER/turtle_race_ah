import turtle
import time
import random
COLORS=['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
# screen
def set_screen():
    screen=turtle.Screen()
    screen.setup(height=700,width=600)
    screen.title('turtlerace!!')

# no. of turtles
def no_of_racer():
    racers = 0
    while True:

     racers_input=input("enter no. of racer you want(2-8):")
     if racers_input.isdigit():
            racers=int(racers_input)
            if 2 <= racers <= 8:
                break
                

    else:
         
         print("try again!")
    return racers        
        
# color and spacing of turtle
def create_turtle(colors):
    turtles=[]
    spacing=600//(len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.up()
        racer.goto(-600//2+(i+1)*spacing,-330)
        racer.down()
        turtles.append(racer)
    return turtles
#race code
def race(colors):
    turtles=create_turtle(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.fd(distance)

            X,Y=racer.pos()
            if Y>=320:
                return colors[turtles.index(racer)]

random.shuffle(COLORS)
racers=no_of_racer()
colors=COLORS[:racers]            
set_screen()
winner=race(colors)
print("The Winner is the Turtle with color:",winner)

turtle.exitonclick()


