#Codiho que dibuja un arbol de color verde
import turtle

def draw_tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

turtle.speed(0)
turtle.bgcolor('black')
turtle.color('green')
turtle.left(90)
turtle.penup()
turtle.backward(100)
turtle.pendown()
draw_tree(75, turtle)
turtle.done()