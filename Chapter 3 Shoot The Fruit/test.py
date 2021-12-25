import pygame
import pgzero
import pgzrun
from random import randint
apple = Actor('apple')
def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        number1= randint (1, 3)
        if number1 == 1:
            print('Good Shot! Do another one and maybe then I will be proud!') 
        if number1 == 2:
            print('I guess we all get lucky sometimes')
        if number1 == 3:
            print('Yeah Yeah you can stop showing off now')
        place_apple()
    else:
        number2= randint (1,3)
        if number2 == 1:
            print('You Missed, Game Over Stupid!')
        if number2 == 2 :
            print('Just click the apple its not that hard')
        if number2 == 3 :
            print('Great.  Now we have to restart.')
        quit()

pgzrun.go()


