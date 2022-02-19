from game_variables import*

class button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    
    def draw(self):
        #get mouse position 
        pos =pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                print(1)
        #draw button 
        screen.blit(self.image,self.rect) 

    
