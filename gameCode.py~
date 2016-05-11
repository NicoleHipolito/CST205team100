import pygame 
import random

pygame.init()

window = pygame.display.set_mode((700,300))     

pygame.display.set_caption("Hungry Doge")

BLACK = (0,0,0)
WHITE = (255,255,255)

TILESIZE = 50

#moveX, moveY = 0,0
numberOfBurgers = 7

#Sets the background variable to desired background image
background_image = pygame.image.load("map.png").convert()


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
        x = 300
    elif(xTemp == 2):
        x = 350    
    elif(xTemp == 3):
        x = 400
    elif(xTemp == 4):
        x = 450 
    elif(xTemp == 5):
        x = 500
    elif(xTemp == 6):
        x = 550 
    elif(xTemp == 7):
        x = 600 
    elif(xTemp == 8):
        x = 650
    elif(xTemp == 9):
        x = 700 
        
    burger_list.append([x, y])
    

 

clock = pygame.time.Clock()
#/////////////////////////////////////////////////////////////////////////////////////////////////////
class Sprite(pygame.sprite.Sprite):

    def __init__(self,x,y,): 
    
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

    def __init__(self,x,y,): 
    
        self.x = burger_list[i][0]
        
        self.y = burger_list[i][1]
        
        self.width = 50
        
        self.height = 50
        
        self.i1 = pygame.image.load("burger1.png")
        self.rect = self.i1.get_rect()
        
    def render(self):
    
        window.blit(self.i1, (burger_list[i][0],burger_list[i][1]))
     
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

#Creates gameloop and will be true untill game is over or use quits
gameLoop = True 

#Main Game Loop will be true untill game is over
while gameLoop: 

#These will detect an event and use the approtpeate IF to give an action
    for event in pygame.event.get():
                
        #This will quit the game when the user wants to with the exit button in the top left corrner of the screen
        if(event.type == pygame.QUIT):
        
            gameLoop = False
            
        #Will move the player 50 pixils whenever a arrow button is pressed
        #Only reads the Up and Down key
        if(event.type==pygame.KEYDOWN):
        
            if(event.key==pygame.K_UP and player.y > 0):
                player.y = player.y -50
               
                
            if(event.key==pygame.K_DOWN and player.y < 240):
                player.y = player.y + 50
         
    #This sets the background using the background_image variable set at the top 
    window.blit(background_image, [0, 0])
    #window.fill(black)
    # Process each Item in the list
    for i in range(len(burger_list)):
     
        # Draw the Item
        burger.render()   
     
        # Move the Item down one pixel
        burger_list[i][0] -= 10
        #print(burger_list[i][0])
        #print(burger_list[i][1])
        
        if(player.x == burger_list[i][0] and player.y == burger_list[i][1]):
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
            xTemp = random.randrange(690,710)
            
            if(xTemp == 1):
                x == 800
            elif(xTemp == 2):
                x == 850
            elif(xTemp == 3):
                x == 900
                
            burger_list[i][0] = x    
    
        
            
    #print(player.x)
    player.render()
    
    #This calls a fucntion that draws a grid on the map for referance
    #drawGrid()
    
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    clock.tick(30)
    
    pygame.display.flip()
        
pygame.quit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
