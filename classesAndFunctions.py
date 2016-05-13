import pygame
import random
# Creates a function that when called will return an x
pygame.init()
def getX():
    xTempApple = random.randrange(1, 9)
    if(xTempApple == 1):
        xValue = 700
    elif(xTempApple == 2):
        xValue = 750
    elif(xTempApple == 3):
        xValue = 800
    elif(xTempApple == 4):
        xValue = 850
    elif(xTempApple == 5):
        xValue = 900
    elif(xTempApple == 6):
        xValue = 950
    elif(xTempApple == 7):
        xValue = 1000
    elif(xTempApple == 8):
        xValue = 1050
    elif(xTempApple == 9):
        xValue = 1100

    return xValue

def getY():

    yTempApple = random.randrange(1, 7)

    if(yTempApple == 1):
        yValue = 0
    elif(yTempApple == 2):
        yValue = 50
    elif(yTempApple == 3):
        yValue = 100
    elif(yTempApple == 4):
        yValue = 150
    elif(yTempApple == 5):
        yValue = 200
    elif(yTempApple == 6):
        yValue = 250
    elif(yTempApple == 7):
        yValue = 300

    return yValue

#**********************************
#/////////////////////////////////////////////////////////////////////////////////////////////////////
class Sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, pictureName):

        self.x = x

        self.y = y

        self.width = w

        self.height = h

        self.i1 = pygame.image.load(pictureName)
        self.rect = self.i1.get_rect()

    def render(self, window):

        window.blit(self.i1, (self.x,self.y))

#////////////////////////////////////////////////////////////////////////////////////////////////////
class SpecialItem(pygame.sprite.Sprite):

    def __init__(self, x,y,pictureName):

        self.x = x

        self.y = y

        self.width = 50

        self.height = 50

        self.i1 = pygame.image.load(pictureName)
        self.rect = self.i1.get_rect()

    def render(self, window):

        window.blit(self.i1, (self.x,self.y))

#///////////////////////////////////////////////////////////////////////////////////////////////////
'''
def drawGrid():
     for x in range(0, 700, TILESIZE): # draw vertical lines
         pygame.draw.line(window, WHITE, (x, 0), (x, 300))
     for y in range(0, 300, TILESIZE): # draw horizontal lines
         pygame.draw.line(window, WHITE, (0, y), (700, y))
'''
#///////////////////////////////////////////////////////////////////////////////////////////////////
