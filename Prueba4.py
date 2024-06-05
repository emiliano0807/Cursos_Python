#Codigo que dibuja una estrella de 5 puntas con recursividad
import turtle

def draw_star(size):
    if size < 10:
        return
    else:
        for _ in range(5):
            turtle.forward(size)
            draw_star(size/3)
            turtle.left(216)

turtle.speed(0)
turtle.bgcolor('black')
turtle.color('yellow')
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
draw_star(300)