import pygame 
import random

pygame.init()

window = pygame.display.set_mode((680,240))     

pygame.display.set_caption("Hungry Doge")

black = (0,0,0)
WHITE = (255,255,255)

#moveX, moveY = 0,0

# Create an empty array
snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(20):
    x = random.randrange(200, 680)
    y = random.randrange(0, 240)
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
    
        self.x = x
        
        self.y = y
        
        self.width = 50
        
        self.height = 50
        
        self.i1 = pygame.image.load("burger1.png")
        self.rect = self.i1.get_rect()
        
    def render(self):
    
        window.blit(self.i1, (snow_list[i][0],snow_list[i][1]))

player = Sprite(50,140)
tennisBall = Item(0,0)
gameLoop = True 
while gameLoop: 
    for event in pygame.event.get():
                
        if(event.type == pygame.QUIT):
        
            gameLoop = False
            
        if(event.type==pygame.KEYDOWN):
        
            if(event.key==pygame.K_UP and player.y > 0):
                player.y = player.y -20
                print(player.y)
            print(player.y)
                
            if(event.key==pygame.K_DOWN and player.y < 180):
                player.y = player.y + 20
        if(event.type == pygame.KEYUP):
            
            if(event.key==pygame.K_RIGHT):
                moveX = 0
        
            if(event.key==pygame.K_UP):
                moveY = -0
            
            if(event.key==pygame.K_DOWN):
                moveY = 0
    window.fill(black)
    # Process each Item in the list
    for i in range(len(snow_list)):
     
        # Draw the Item
        tennisBall.render()   
     
        # Move the Item down one pixel
        snow_list[i][0] -= 1
     
        # If the Item has moved off the bottom of the screen
        if snow_list[i][0] < 0:
            # Reset it just above the top
            y = random.randrange(0,240)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(690,710)
            snow_list[i][0] = x    
            
    
  #  player.x += moveX
  #  player.y += moveY
   # print(player.y)
    #pygame.sprite.collide_rect(player,tennisBall)
    hit_list = pygame.sprite.spritecollide(player,tennisBall, True)
    for block in hit_list:
        score += 1
    player.render()
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    
    clock.tick(30)
    
    pygame.display.flip()
        
pygame.quit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
