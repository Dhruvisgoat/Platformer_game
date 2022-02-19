#creating background
from calendar import c
from operator import truediv
from re import S
import time
import pygame
from pygame.locals import*
from game_variables import*
from player import*
from World import*
from Enemy import* 
from lava import*

pygame.init()

class button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.clicked=False
    
    def draw(self): 
        action=False
        #get mouse position 
        pos =pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                action=True
                self.clicked==True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked==False
        #draw button 
        screen.blit(self.image,self.rect) 
        
        return action

    


restart_button=button(screen_width//2 -(50*0.8),screen_height//2+(100*0.8),restart_img)


mario=Player(100*0.8,screen_height-(130*0.8)) # CREATING A PLAYER_CLASS OBJECT MARIO
def game():
    background_music.play()
    run =True
    global game_over
    while run:   ## GAME LOOP ##
        clock.tick(fps)

        screen.blit(bg_img,(0,0))
        screen.blit(sun_img,(100*0.8,100*0.8))

        WORLD.draw()

        WORLD.blob_group.draw(screen)
        WORLD.lava_group.draw(screen)

        game_over=mario.update(game_over)
        #if player dies 
        if game_over==-1:
            if restart_button.draw():
                mario.reset(100*0.8,screen_height-(130*0.8))
                game_over=0
            restart_button.draw()
        if game_over==0:
            WORLD.blob_group.update()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:  
                run=False
        pygame.display.update()

game()
pygame.quit()#the game will get quit using this function

        
