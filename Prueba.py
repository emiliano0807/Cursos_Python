#Codigo que dibuja flores de colores
import turtle
import random

# Configuración inicial
window = turtle.Screen()
window.bgcolor("white")

flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(0)  # Velocidad más rápida

# Función para dibujar un pétalo
def draw_petal():
    flower.color(random.choice(["red", "pink", "purple", "orange", "blue"]))
    flower.begin_fill()
    flower.circle(50, 60)
    flower.left(120)
    flower.circle(50, 60)
    flower.end_fill()

# Dibuja varios pétalos para formar una flor
def draw_flower():
    for _ in range(6):  # Cambia el número para más o menos pétalos
        draw_petal()
        flower.left(60)
    flower.hideturtle()

# Dibuja el tallo de la flor
def draw_stem():
    flower.color("green")
    flower.left(90)
    flower.forward(200)

# Dibuja una flor completa
def draw_complete_flower():
    draw_stem()
    draw_flower()

# Dibuja múltiples flores en diferentes posiciones
for _ in range(3):  # Cambia el número para más o menos flores
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    flower.penup()
    flower.goto(x, y)
    flower.pendown()
    draw_complete_flower()

# Cierra la ventana al hacer clic
window.exitonclick()