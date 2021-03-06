import pygame
import random
from classesAndFunctions import *
pygame.init()
window = pygame.display.set_mode((700,300))
#added a score on the caption
pygame.display.set_caption("Hungry Doge     Score: 0     Speed: 10     Burgers dodged: 0")
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (125,0,0)
LRED = (255,0,0)
GREEN = (0,125,0)
LGREEN = (0,255,0)
#**************var for manipulating speed of the burgers, apples, and mushrooms

#**Vars used in the menu****
display_width = 700
display_height = 200

numDoge = 0
#*******Score to display in the caption since the screen is all used.
##score = 0 #lets say that apples are worth 5 pnts and donuts are worth 1.
##brgrsDgd = 0 #count of burgers dodged.

#How large you want each square in the grid to be
TILESIZE = 50
#moveX, moveY = 0,0
isOnApple = True
#************I'm making a donut for the slow down item
isOnDonut = True
#*********************
#Sets the background variable to desired background image
background_image = pygame.image.load("map.png").convert()

#/////////////////////////////////////////////////////////////////////////////////////////////////////
font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):
    screen_text = font.render(msg,True,color)
    window.blit(screen_text,[150,100])
#////////////////////////////////////////////////////////////////////////////////////////////////
clock = pygame.time.Clock()


#function for creating text
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)#render the font
    return textSurface, textSurface.get_rect()

##    #lights up the button when the cursor hovers over it.
##
##    #if the x position of the mouse is greater than the x position
##    #of the rectangle and less than (the x position of the
##    #rectangle plus the width of the rectangle)
##    #and if the y position of the mouse is greater than the y position
##    #of the rectangle and less than (the y position of the
##    #rectangle plus the width of the rectangle):
##    if x+w > mouse[0] > x and y+h > mouse[1] > y:
##        #draw the rectangle a lightGreen this is for an interactive effect
##        #with the "buttons"
##        pygame.draw.rect(window, ac, (x,y,w,h))
##    else:
##        #draws a colored rectangle on the menu for a button
##        pygame.draw.rect(window, nc,(x,y,w,h))
##
##    smallText = pygame.font.Font("freesansbold.ttf", 20)#a small font
##    #add text to the button
##    textSurf, textRect = text_objects(msg, smallText)#write on button
##    textRect.center = ((x+(w/2)),(y+(h/2)))
##    window.blit(textSurf, textRect)

#quits game
def quitGame():
    pygame.quit()
    quit()



#********BUTTONS function

#button function
def button(msg,x,y,w,h,nc,ac,action=None):#(message,x,y,width,height,normal color, active color)
    #gets the position of the mouse
    mouse = pygame.mouse.get_pos()

    #gets mouse clicks
    click = pygame.mouse.get_pressed()

    #lights up the button when the cursor hovers over it.

    #if the x position of the mouse is greater than the x position
    #of the rectangle and less than (the x position of the
    #rectangle plus the width of the rectangle)
    #and if the y position of the mouse is greater than the y position
    #of the rectangle and less than (the y position of the
    #rectangle plus the width of the rectangle):
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        #draw the rectangle a lightGreen this is for an interactive effect
        #with the "buttons"
        pygame.draw.rect(window, ac, (x,y,w,h))
        #react to if the go button is clicked
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()
            elif action == "quit":
                pygame.quit()
                quit()

    else:
        #draws a colored rectangle on the menu for a button
        pygame.draw.rect(window, nc,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)#a small font
    #add text to the button
    textSurf, textRect = text_objects(msg, smallText)#write on button
    textRect.center = ((x+(w/2)),(y+(h/2)))
    window.blit(textSurf, textRect)



#*****************************
#*****************MENU***************

def game_menu():

    menu = True

    while menu:
        for event in pygame.event.get():
            #asks for a quit event basically
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #fill up the window for the menu background
        window.fill(WHITE)
        #specify the large txt for the menu title
        largeText = pygame.font.Font('freesansbold.ttf', 110)
        TextSurf, TextRect = text_objects("Hungry Doge", largeText)
        #Center the title according to the height and width of the window
        #and cutting each in half
        TextRect.center = ((display_width/2),(display_height/2))
        #blit puts an object over another object
        window.blit(TextSurf, TextRect)

        #draw buttons so they interact with the mouse by changing color
        button("Start",150,200,100,50,GREEN,LGREEN, "play")
        button("Quit",430,200,100,50,RED,LRED, "quit")

        pygame.display.update()
        clock.tick(15)


#******GAME LOOP FUNC

def gameLoop():
    pygame.mixer.music.load("GameSong.wav")
    pygame.mixer.music.play(-1)
    objectSpd = 5 #speed that objects will travel
    # Create an empty array
    burger_list = []
    numberOfBurgers = 10
    # Loop # of times depending on number of burgers wanted and sets [x,y]
    for i in range(numberOfBurgers):
        x = getX()
        y = getY()
        burger_list.append([x, y])
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
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

    #Creating the player (X position, Y Position)
    # x, y, w, h, pictureName)
    player = Sprite(50,150,50,50,"doge.png")
    player2 = Sprite(50,100,30,30, "superDoge.png")
    #Creating the burger (Doesnt matter, will be re-written)
    burger = Item(0,0)
    #Creating the apple boot and its spawn chance
    apple = SpecialItem(-10,-10, "apple.png")
    #************Creating the donut too#CHECK iF ERRoRs
    donut = SpecialItem(-10,-10, "donut.png")
    #Creating the instance of the treat
    treat = SpecialItem(-10,-10, "treat.png")
    #Creating the instance of the dogBowl
    bowl = SpecialItem(-10,-10, "dogbowl.png")
    #Creates gameloop and will be true untill game is over or use quits
    gameLoop = True
    gameOver = False
    isOnApple = True
    isOnDonut = True
    isOnTreat = True
    isOnBowl = True
    isBeginning = True
    isThereTwoSprites = True
    score = 0 #lets say that apples are worth 5 pnts and donuts are worth 1.
    brgrsDgd = 0 #count of burgers dodged.
    #Main Game Loop will be true untill game is over
    while gameLoop:
        appleDropChance = random.randrange(1, 5)
        donutDropChance = random.randrange(1, 7)
        treatDropChance = random.randrange(1, 10)
        bowlDropChance = random.randrange(1, 5)

        while gameOver:
            window.fill(BLACK)
            pygame.mixer.pause()
            message_to_screen("Game over, to play again press c, to quit press q.", RED)
            pygame.display.update()

            for event in pygame.event.get():

                if(event.type == pygame.KEYDOWN):
                #This will quit the game when the user wants to with the exit button in the top  left corrner of the screen
                    if(event.type == pygame.QUIT):

                        gameLoop = False
                    if(event.key == pygame.K_c):
                        print("C")
                        gameOver = False
                        gameLoop = True
                        game_menu()

                    if(event.key == pygame.K_q):
                        print("Q")
                        pygame.quit()

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
                    if(isThereTwoSprites):
                        player2.y = player2.y -50
                if(event.key==pygame.K_DOWN and player.y < 240):
                    player.y = player.y + 50
                    if(isThereTwoSprites):
                        player2.y = player2.y +50
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
            if((player.x+30 == burger_list[i][0]) and player.y == burger_list[i][1] and isThereTwoSprites == False):
                gameOver = True
            elif ((player.x+30 == burger_list[i][0]) and player.y == burger_list[i][1] and isThereTwoSprites):
                isThereTwoSprites = False
            # If the Item has moved off the bottom of the screen
            if burger_list[i][0] < 0:
                # Reset it just above the top
                burger_list[i][1] = getY()
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
        #***************************************************
        if(4 == treatDropChance and treat.x < 0):
            x = getX()
            y = getY()
            while isOnTreat:
                for i in range(numberOfBurgers):
                    if(x != burger_list[i][0] or y != burger_list[i][1]):
                        treat.x = x
                        treat.y = y
                        isOnTreat = False

        treat.x -= objectSpd

        if(((player.x+30 == treat.x) or (player.x == treat.x)) and player.y == treat.y):
            pygame.mixer.music.load('realPlusImag.wav')
            pygame.mixer.music.play(-1)
            treat.x = -1000
            treat.y = -1000
            player2.x = player.x
            player2.y = player.y
            isThereTwoSprites = True
            isBeginning = False
        #***************************************************
        if(1 == bowlDropChance and bowl.x < 0):
            x = getX()
            y = getY()
            while isOnBowl:
                for i in range(numberOfBurgers):
                    if(x != burger_list[i][0] or y != burger_list[i][1]):
                        bowl.x = x
                        bowl.y = y
                        isOnBowl = False

        bowl.x -= objectSpd

        if(((player.x+30 == bowl.x) or (player.x == bowl.x)) and player.y == bowl.y):
            pygame.mixer.music.load('GameSong.wav')
            pygame.mixer.music.play(-1)
            bowl.x = -1000
            bowl.y = -1000
            objectSpd = 5
        #***************************************************
        if(3 == appleDropChance and apple.x < 0):
            while isOnApple:
                x = getX()
                y = getY()
                for i in range(numberOfBurgers):
                    if(x != burger_list[i][0] or y != burger_list[i][1]):
                        apple.x = x
                        apple.y = y
                        isOnApple = False
                   #********the apples' speed can be manipulated
        apple.x -= objectSpd
        #***************************************************
        #collision with apple.
        if(((player.x+30 == apple.x) or (player.x == apple.x)) and player.y == apple.y):
            pygame.mixer.music.load('fast.wav')
            pygame.mixer.music.play(-1)
            apple.x = -1000
            apple.y = -1000
            #add to score
            score += 5
            #print score at the top of screen, and yeah overwrite the title
            #*************Increment the speed of the items
            if objectSpd <= 50:
                if objectSpd == 1:
                    objectSpd = 5
                elif objectSpd == 5:
                    objectSpd = 10
                elif objectSpd == 10:
                    objectSpd = 25
                elif objectSpd == 25:
                    objectSpd = 50
            else:
                print("well, I think you've won or something")#should we make a
                                                              #certain speed
                                                              #cap and have the
                                                              #player win
                                                              #if it is reached?
            #well we want to make that apple we collided with disapear,
            #so lets put it bellow the screen(left)
            #burger_list[i][0] = 0
    #************************************and for donut...
        if(2 == donutDropChance and donut.x < 0):
            while isOnDonut:
                x = getX()
                y = getY()
                for i in range(numberOfBurgers):
                    if(x != burger_list[i][0] or y != burger_list[i][1]):
                        donut.x = x
                        donut.y = y
                        isOnDonut = False

        donut.x -= objectSpd
        #collision with donut.
        if(((player.x+30 == donut.x) or (player.x == donut.x)) and player.y == donut.y):
            #print('Donut')
            pygame.mixer.music.load('slow.wav')
            pygame.mixer.music.play(-1)
            donut.x = -1000
            donut.y = -1000
            #add to score
            score += 1

            #*****THIS PART OF THE CODE MAY HAVE ISSUES WITH MATH AND STUFF
            #*************Increment the speed of the items
            if objectSpd > 0:
                if objectSpd == 5:
                    objectSpd = 1
                elif objectSpd == 10:
                    objectSpd = 5
                elif objectSpd == 25:
                    objectSPd = 10
                elif objectSpd == 50:
                    objectSpd = 25
            else:
                print("well, I think you've won or something")
        #***************************************************
        #to add the score to the caption we have to set the value of the score
        #which is an int to a string uing str()
        #print score at the top of screen, and yeah overwrite the title
        #*******************
        #IT'S NOT READING THE "SPEED...."
        pygame.display.set_caption("Hungry Doge     Score: " + str(score) +
                                   "     Speed: " + str(objectSpd)+
                                   "     Burgers dodged: " + str(brgrsDgd))

        player.render(window)
        if(isThereTwoSprites and isBeginning == False):
            player2.render(window)
        isOnApple = True
        #***
        isOnDonut = True
        #***
        isOnTreat = True
        #***
        isOnBowl = True
        #This calls a fucntion that draws a grid on the map for referance
        #drawGrid()
        treat.render(window)
        apple.render(window)
        donut.render(window)
        bowl.render(window)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(30)
        #print(appleDropChance)
        #pygame.display.flip()

#call game menu
game_menu()
#call game loop function
#gameLoop()
pygame.quit()
