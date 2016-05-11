import pygame 
import random

pygame.init()

window = pygame.display.set_mode((700,300))     

pygame.display.set_caption("Hungry Doge")

BLACK = (0,0,0)
WHITE = (255,255,255)

TILESIZE = 50

#moveX, moveY = 0,0
numberOfBurgers = 1

background_image = pygame.image.load("map.png").convert()
# Create an empty array
snow_list = []


 
# Loop # of times depending on number of burgers wanted and sets [x,y]
for i in range(numberOfBurgers):
    x = random.randrange(200, 680)
    yTemp = random.randrange(1, 6)
    
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

    snow_list.append([x, y])
    

 

clock = pygame.time.Clock()

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
        
class Item(pygame.sprite.Sprite):

    def __init__(self,x,y,): 
    
        self.x = snow_list[i][0]
        
        self.y = snow_list[i][1]
        
        self.width = 50
        
        self.height = 50
        
        self.i1 = pygame.image.load("burger1.png")
        self.rect = self.i1.get_rect()
        
    def render(self):
    
        window.blit(self.i1, (snow_list[i][0],snow_list[i][1]))
        
def drawGrid():
     for x in range(0, 700, TILESIZE): # draw vertical lines
         pygame.draw.line(window, WHITE, (x, 0), (x, 300))
     for y in range(0, 300, TILESIZE): # draw horizontal lines
         pygame.draw.line(window, WHITE, (0, y), (700, y))

player = Sprite(100,150)
burger = Item(0,0)
gameLoop = True 
while gameLoop: 
    for event in pygame.event.get():
                
        if(event.type == pygame.QUIT):
        
            gameLoop = False
            
        if(event.type==pygame.KEYDOWN):
        
            if(event.key==pygame.K_UP and player.y > 0):
                player.y = player.y -50
                print(player.y)
            print(player.y)
                
            if(event.key==pygame.K_DOWN and player.y < 240):
                player.y = player.y + 50
                print(player.y)
        if(event.type == pygame.KEYUP):
            
            if(event.key==pygame.K_RIGHT):
                moveX = 0
        
            if(event.key==pygame.K_UP):
                moveY = -0
            
            if(event.key==pygame.K_DOWN):
                moveY = 0
    
    window.blit(background_image, [0, 0])
    #window.fill(black)
    # Process each Item in the list
    for i in range(len(snow_list)):
     
        # Draw the Item
        burger.render()   
     
        # Move the Item down one pixel
        snow_list[i][0] -= 50
        
     
        # If the Item has moved off the bottom of the screen
        if snow_list[i][0] < 0:
            # Reset it just above the top
            y = random.randrange(0,240)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(690,710)
            snow_list[i][0] = x    
    
    #print(burger.x)
    #print(burger.y)
    print(player.x)
    player.render()
    drawGrid()
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    clock.tick(10)
    
    pygame.display.flip()
        
pygame.quit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
