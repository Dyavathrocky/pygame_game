import pygame
from pgzero.actor import Actor
from pygame import draw
#from pgzero import screen
from pgzero.screen import *
from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 250)
    apple.y = randint(10 , 250)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("good shot!")
        place_apple()
    else:
        print("you missed it")
        quit()

