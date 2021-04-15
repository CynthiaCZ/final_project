import pygame as pg
import time

#Importing key inputs that will be used for sprite navigation
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Initializing imported modules
pg.init()

#Defining colors to be used to create background and sprites
black = (0,0,0)
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)
darkgreen = (0,128,0)
grey = (128,128,128)
red = (255,0,0)
blue = (0,0,255)

#Defining dimensions of the screen
screen = pg.display.set_mode((750,550))

#Creating list of all sprites in the game (cars, player sprite, and finish line)
fullspritelist = pg.sprite.Group()

#Creating a class "mysprite" and then using __init__ to create an object from this class and initializing its attributes
#Making a circular object that will be called later when making the player's sprite
class mysprite(pg.sprite.Sprite):
    def __init__(self, color, x, y, radius):
        super().__init__() #Calling parent class
        self.image = pg.Surface([x, y])
        self.image.fill(white)
        self.image.set_colorkey(white) #Used to make the rectangle behind the circle transparent
        pg.draw.circle(self.image, color, (x/2, y/2), radius) #Actually drawing the circle
        self.rect = self.image.get_rect() #Getting rectangular object

#Making the sprite using the previously made mysprite class and positioning its starting position
mysprite = mysprite(yellow, 50, 50, 20)
mysprite.rect.x = 0
mysprite.rect.y = 250
fullspritelist.add(mysprite)
