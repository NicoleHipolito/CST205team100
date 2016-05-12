import pygame
import random

pygame.init()
window = pygame.display.set_mode((700,300))
#added a score on the caption
pygame.display.set_caption("Hungry Doge     Score: 0     Speed: 10     Burgers dodged: 0")
BLACK = (0,0,0)
WHITE = (255,255,255)
#**************var for manipulating speed of the burgers, apples, and mushrooms
objectSpd = 10 #speed that objects will travel


#*******Score to display in the caption since the screen is all used.
score = 0 #lets say that apples are worth 5 pnts and donuts are worth 1.
brgrsDgd = 0 #count of burgers dodged.

#How large you want each square in the grid to be
TILESIZE = 50
#moveX, moveY = 0,0
numberOfBurgers = 1
isOnApple = True

#************I'm making a donut for the slow down item
isOnDonut = True
#*********************
#Sets the background variable to desired background image
background_image = pygame.image.load("map.png").convert()

# Creates a function that when called will return an x
def makeAppleX():
    xTempApple = random.randrange(1, 9)
    if(xTempApple == 1):
        xApple = 700
    elif(xTempApple == 2):
        xApple = 750
    elif(xTempApple == 3):
        xApple = 800
    elif(xTempApple == 4):
        xApple = 850
    elif(xTempApple == 5):
        xApple = 900
    elif(xTempApple == 6):
        xApple = 950
    elif(xTempApple == 7):
        xApple = 1000
    elif(xTempApple == 8):
        xApple = 1050
    elif(xTempApple == 9):
        xApple = 1100

    return xApple

def makeAppleY():

    yTempApple = random.randrange(1, 7)

    if(yTempApple == 1):
        yApple = 0
    elif(yTempApple == 2):
        yApple = 50
    elif(yTempApple == 3):
        yApple = 100
    elif(yTempApple == 4):
        yApple = 150
    elif(yTempApple == 5):
        yApple = 200
    elif(yTempApple == 6):
        yApple = 250
    elif(yTempApple == 7):
        yApple = 300

    return yApple

#******************And the same for dunut

def makeDonutX():
    xTempDonut = random.randrange(1, 9)
    if(xTempDonut == 1):
        xDonut = 700
    elif(xTempDonut == 2):
        xDonut = 750
    elif(xTempDonut == 3):
        xDonut = 800
    elif(xTempDonut == 4):
        xDonut = 850
    elif(xTempDonut == 5):
        xDonut = 900
    elif(xTempDonut == 6):
        xDonut = 950
    elif(xTempDonut == 7):
        xDonut = 1000
    elif(xTempDonut == 8):
        xDonut = 1050
    elif(xTempDonut == 9):
        xDonut = 1100

    return xDonut

def makeDonutY():

    yTempDonut = random.randrange(1, 7)

    if(yTempDonut == 1):
        yDonut = 0
    elif(yTempDonut == 2):
        yDonut = 50
    elif(yTempDonut == 3):
        yDonut = 100
    elif(yTempDonut == 4):
        yDonut = 150
    elif(yTempDonut == 5):
        yDonut = 200
    elif(yTempDonut == 6):
        yDonut = 250
    elif(yTempDonut == 7):
        yDonut = 300

    return yDonut


#**********************************

# Create an empty array
burger_list = []

# Loop # of times depending on number of burgers wanted and sets [x,y]
for i in range(numberOfBurgers):
    xTemp = random.randrange(1, 9)
    yTemp = random.randrange(1, 7)

    if(yTemp == 1):
        y = 0
    elif(yTemp == 2):
        y = 50
    elif(yTemp == 3):
        y = 100
    elif(yTemp == 4):
        y = 150
    elif(yTemp == 5):
        y = 200
    elif(yTemp == 6):
        y = 250
    elif(yTemp == 7):
        y = 300

    if(xTemp == 1):
        x = 700
    elif(xTemp == 2):
        x = 750
    elif(xTemp == 3):
        x = 800
    elif(xTemp == 4):
        x = 850
    elif(xTemp == 5):
        x = 900
    elif(xTemp == 6):
        x = 950
    elif(xTemp == 7):
        x = 1000
    elif(xTemp == 8):
        x = 1050
    elif(xTemp == 9):
        x = 1100

    burger_list.append([x, y])

clock = pygame.time.Clock()
#/////////////////////////////////////////////////////////////////////////////////////////////////////
class Sprite(pygame.sprite.Sprite):

    def __init__(self,x,y):

        self.x = x

        self.y = y

        self.width = 50

        self.height = 50

        self.i1 = pygame.image.load("doge.png")
        self.rect = self.i1.get_rect()

    def render(self):

        window.blit(self.i1, (self.x,self.y))

#////////////////////////////////////////////////////////////////////////////////////////////////////
class Item(pygame.sprite.Sprite):

    def __init__(self,x,y):

        self.x = burger_list[i][0]

        self.y = burger_list[i][1]

        self.width = 50

        self.height = 50

        self.i1 = pygame.image.load("burger1.png")
        self.rect = self.i1.get_rect()

    def render(self):

        window.blit(self.i1, (burger_list[i][0],burger_list[i][1]))

#///////////////////////////////////////////////////////////////////////////////////////////////////
class SpecialItem(pygame.sprite.Sprite):
    def __init__(self,x,y):

        self.x = x

        self.y = y

        self.width = 30

        self.height = 30

        self.i1 = pygame.image.load("apple.png")
        self.rect = self.i1.get_rect()

    def render(self):
        window.blit(self.i1, (self.x,self.y))

#//////////////////////////////////////////////////////////Class for Donut/////////

class SpecialItem1(pygame.sprite.Sprite):
    def __init__(self,x,y):

        self.x = x

        self.y = y

        self.width = 30

        self.height = 30

        self.i1 = pygame.image.load("donut.png")
        self.rect = self.i1.get_rect()

    def render(self):
        window.blit(self.i1, (self.x,self.y))

#///////////////////////////////////////////////////////////////////////////////////////////////////
def drawGrid():
     for x in range(0, 700, TILESIZE): # draw vertical lines
         pygame.draw.line(window, WHITE, (x, 0), (x, 300))
     for y in range(0, 300, TILESIZE): # draw horizontal lines
         pygame.draw.line(window, WHITE, (0, y), (700, y))

#///////////////////////////////////////////////////////////////////////////////////////////////////


#Creating the player (X position, Y Position)
player = Sprite(50,150)
#Creating the burger (Doesnt matter, will be re-written)
burger = Item(0,0)
#Creating the apple boot and its spawn chance
apple = SpecialItem(0, 0)
#************Creating the donut too#CHECK iF ERRoRs
donut = SpecialItem1(0,0)

#Creates gameloop and will be true untill game is over or use quits
gameLoop = True

#Main Game Loop will be true untill game is over
while gameLoop:
    appleDropChance = random.randrange(1, 5)
    
    #*****donut will drop at the same frequency as apple
    donutDropChance = random.randrange(1, 5)
    
#These will detect an event and use the approtpeate IF to give an action
    for event in pygame.event.get():

        #This will quit the game when the user wants to with the exit button in the top left corrner of the screen
        if(event.type == pygame.QUIT):

            gameLoop = False

        #Will move the player 50 pixils whenever an arrow button is pressed
        #Only reads the Up and Down key
        if(event.type==pygame.KEYDOWN):

            if(event.key==pygame.K_UP and player.y > 0):
                player.y = player.y -50


            if(event.key==pygame.K_DOWN and player.y < 240):
                player.y = player.y + 50

    #This sets the background using the background_image variable set at the top
    window.blit(background_image, [0, 0])


    # Process each Item in the list
    for i in range(len(burger_list)):

        # Draw the Item
        burger.render()

        # Move the Item down one pixel
                             #****
        burger_list[i][0] -= objectSpd #speed is used so that it can be changed uniformly
                             #**** #in a collision event with a speed altering item
        #print(burger_list[i][0])
        #print(burger_list[i][1])

        #Collision for the player and the burger
        if(player.x == burger_list[i][0] and player.y == burger_list[i][1]):
            print("*********************************You lose")
            print("*********************************Have you tried the command git gud?")
            pygame.quit()

        # If the Item has moved off the bottom of the screen
        if burger_list[i][0] < 0:
            # Reset it just above the top
            yTemp = random.randrange(1,7)
            if(yTemp == 1):
                y = 0
            elif(yTemp == 2):
                y = 50
            elif(yTemp == 3):
                y = 100
            elif(yTemp == 4):
                y = 150
            elif(yTemp == 5):
                y = 200
            elif(yTemp == 6):
                y = 250
            elif(yTemp == 7):
                y = 300
            burger_list[i][1] = y
            # Give it a new x position
            xTemp = random.randrange(1,3)

            if(xTemp == 1):
                x = 800
            elif(xTemp == 2):
                x = 850
            elif(xTemp == 3):
                x = 900

            burger_list[i][0] = x

            #increment burgers dodged count
            brgrsDgd += 1

            #refresh the caption mainly for the new burgers dodged count
            pygame.display.set_caption("Hungry Doge     Score: " + str(score) +
                                   "     Speed: " + str(objectSpd) +
                                   "     Burgers dodged: " + str(brgrsDgd))
     #end of burger for loop


    if(3 == appleDropChance and apple.x < 0):

        while isOnApple:

            x = makeAppleX()
            y = makeAppleY()
            for i in range(numberOfBurgers):
                if(x != burger_list[i][0] or y != burger_list[i][1]):
                    apple.x = x
                    apple.y = y
                    isOnApple = False

    print('x: ', apple.x)
    print('y: ', apple.y)
               #********the apples' speed can be manipulated
    apple.x -= objectSpd

    



    #***************************************************
    #collision with apple.
    if(player.x == apple.x and player.y == apple.y):
        print('APPLE')
        #add to score
        score += 5
        #print score at the top of screen, and yeah overwrite the title


        
        #*************Increment the speed of the items
        if objectSpd <= 50:
            objectSpd += 10
        else:
            print("well, I think you've won or something")#should we make a
                                                          #certain speed
                                                          #cap and have the
                                                          #player win
                                                          #if it is reached?
        #well we want to make that apple we collided with disapear,
        #so lets put it bellow the screen(left)
        #burger_list[i][0] = 0

        
        #to add the score to the caption we have to set the value of the score
        #which is an int to a string uing str()
        pygame.display.set_caption("Hungry Doge     Score: " + str(score) +
                                   "     Speed: " + str(objectSpd) +
                                   "     Burgers dodged: " + str(brgrsDgd))

#************************************and for donut...
    if(3 == donutDropChance and donut.x < 0):

        while isOnDonut:

            x = makeDonutX()
            y = makeDonutY()
            for i in range(numberOfBurgers):
                if(x != burger_list[i][0] or y != burger_list[i][1]):
                    donut.x = x
                    donut.y = y
                    isOnDonut = False

    print('x: ', donut.x)
    print('y: ', donut.y)
               
    donut.x -= objectSpd

    



    
    #collision with donut.
    if(player.x == donut.x and player.y == donut.y):
        print('Donut')

        #add to score
        score += 1
        


        #*****THIS PART OF THE CODE MAY HAVE ISSUES WITH MATH AND STUFF
        #*************Increment the speed of the items
        if objectSpd >= 11: #I dont want the speed to reach 0 lol
            objectSpd -= 10
        elif objectSpd > 0:
            objectSpd = 5
        else:
            print("well, I think you've won or something")

        #print score at the top of screen, and yeah overwrite the title
        #*******************
        #IT'S NOT READING THE "SPEED...."
        pygame.display.set_caption("Hungry Doge     Score: " + str(score) +
                                   "     Speed: " + str(objectSpd)+
                                   "     Burgers dodged: " + str(brgrsDgd))
        



    #***************************************************
    #print(player.x)
    player.render()
    isOnApple = True

    #***
    isOnDonut = True
    #***
    
    #This calls a fucntion that draws a grid on the map for referance
    drawGrid()
    apple.render()

    #*****
    donut.render()
    #*****



    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(30)
    #print(appleDropChance)
    #pygame.display.flip()

pygame.quit()
