#Karimn Daniel Hernández Castorena
#Programa que dibuja círculos.

import pygame
import math
import random

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def adquirirColor():
    rojo = random.randrange(0, 255)
    verde = random.randrange(0, 255)
    azul = random.randrange(0, 255)
    colorX = (rojo, verde, azul)
    return colorX

def dibujar(r,R,l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(NEGRO)
        for angulo in range(0, (360*(r//math.gcd(r, R))+1)):

            color = adquirirColor()
            a = math.radians(angulo)
            k = r / R
            x = int(R * ((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a)))
            y = int(R * ((1 - k) * math.sin(a) + l * k * math.sin(((1 - k) / k) * a)))

            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():
    r = int(input("Por favor introduce r: "))
    R = int(input("Ahora introduce la R: "))
    l = float(input("Y por último introduce la l : "))


    dibujar(r,R,l)


main()