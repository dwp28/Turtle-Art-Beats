import turtle
import math
import pygame


# Reproducir música
pygame.mixer.init()
pygame.mixer.music.load("Music/The Police - Every Breath You Take.wav")
pygame.mixer.music.play(-1)  # Reproduce en bucle

# Configuración del turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

# Función para calcular puntos del corazón
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

# Dibujar múltiples corazones
t.penup()
for i in range(15):
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 100, 2):
        x, y = corazon(n / 10)
        t.goto(x * i, y * i)
    t.penup()

# Dibujar firma "Daniel" abajo a la derecha
t.hideturtle()
screen = turtle.Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()

# Posicionar turtle para la firma
margin_x = 150
margin_y = 100
t.goto(screen_width/2 - margin_x, -screen_height/2 + margin_y)
t.pendown()
t.color("white")  # Cambia el color para que contraste con el fondo negro
t.write("Daniel", font=("Lucida Handwriting", 24, "normal"))  # Puedes cambiar fuente

# Línea debajo como firma
t.penup()
t.goto(t.xcor(), t.ycor() - 10)
t.pendown()
t.forward(80)

# Finalizar
t.hideturtle()
turtle.done()

# Detener música
pygame.mixer.music.stop()
