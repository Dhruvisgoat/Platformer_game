from enum import Flag
from operator import truediv
from World import*
from game_variables import *


class Player():
    def __init__(self,x,y):
        self.reset(x,y) 
    
    def reset(self,x,y):
    
        self.image=pygame.image.load('img/guy1.png')
        self.image=pygame.transform.scale(self.image,(40*0.8,80*0.8))
        self.dead_image=pygame.image.load('img/ghost.png')

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        self.vel_y=0
        self.jumped=False
        self.i=0
        self.counter=0
        self.in_air=True

        self.images_right=[]
        self.images_left=[]  
        self.index=0
        self.counter=0
        #loading imgages for animation
        for num in range(1,5):
            img_right=pygame.image.load(f'img/guy{num}.png')
            img_right=pygame.transform.scale(img_right,(40*0.8,80*0.8))
            img_left=pygame.transform.flip(img_right,True,False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

    
    def update(self,game_over):
        self.counter+=1

        dx=0
        dy=0
        if game_over==0:
            #get key presses
            key=pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                dx-=5
                if self.counter>5 :   
                #animation 
                    self.counter=0
                    if(self.i>=4):
                        self.i=0
                    self.image=self.images_left[self.i]
                    self.i+=1
            if key[pygame.K_RIGHT]:
                dx+=5
                if self.counter>5 :   
                    #animation 
                    self.counter=0
                    if(self.i>=4):
                        self.i=0
                    self.image=self.images_right[self.i]
                    self.i+=1
            if key[pygame.K_SPACE]   and (self.jumped ==False) and self.in_air==False:
                jump_fx.play()
                self.vel_y=-15
                self.jumped=True       
            if key[pygame.K_SPACE]==False :
                self.jumped=False

            #add gravity
            self.vel_y+=1
            if self.vel_y>10:
                self.vel_y=10
            dy+=self.vel_y
            #check for collision
            self.in_air=True
            for tile in WORLD.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                    dx=0
                #Check for collision in y direction
                if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                    if self.vel_y<0:
                        dy=tile[1].bottom-self.rect.top
                        self.vel_y=0
                    elif self.vel_y>=0:
                        dy=tile[1].top-self.rect.bottom
                        self.vel_y=0
                        self.in_air=False

            if pygame.sprite.spritecollide(self,WORLD.blob_group,False):
                game_over=-1
                game_over_fx.play()
            if pygame.sprite.spritecollide(self,WORLD.lava_group,False):
                game_over=-1
                game_over_fx.play()
            
            #draw player onto screen 
            self.rect.x+=dx
            self.rect.y+=dy
            #falling limit on screen bottom
        elif game_over==-1:
            self.image=self.dead_image
            if self.rect.y>200:
                self.rect.y-=5
        screen.blit(self.image,self.rect)

        return game_over

