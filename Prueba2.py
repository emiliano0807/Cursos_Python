#Codigo que realiza un corazon
import turtle
import time
import math

# Configuración inicial de la ventana de Turtle
wn = turtle.Screen()
wn.title("Corazón Latiendo")
wn.bgcolor("black")

# Función para dibujar un corazón
def draw_heart(size):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("red")
    t.penup()

    t.goto(0, -size)
    t.pendown()
    t.begin_fill()

    t.left(140)
    t.forward(size * 2 * math.sqrt(2))
    t.circle(size, -180)
    t.left(90)
    t.circle(size, -180)
    t.forward(size * 2 * math.sqrt(2))

    t.end_fill()
    t.penup()

# Función para animar el latido del corazón
def heartbeat():
    for size in range(5, 25, 2):  # Cambia el tamaño del corazón de 5 a 25
        wn.clear()
        draw_heart(size)
        wn.update()
        time.sleep(0.2)  # Tiempo de espera entre cambios de tamaño
    for size in range(25, 5, -2):  # Cambia el tamaño del corazón de 25 a 5
        wn.clear()
        draw_heart(size)
        wn.update()
        time.sleep(0.2)  # Tiempo de espera entre cambios de tamaño

# Dibujar el corazón inicialmente y luego iniciar la animación del latido
draw_heart(5)
heartbeat()

# Mantener la ventana abierta
wn.mainloop()