#Codigo que realiza un dibujo de circulos con colores
import turtle

turtle.speed(0)
turtle.bgcolor('black')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(30):
    turtle.pencolor(colors[i % len(colors)])
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    
turtle.done()